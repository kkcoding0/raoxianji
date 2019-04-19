from app import *
import json
import pymysql
from flask import request
import traceback
from flask import flash,session

@app.route('/test',methods=['GET','POST'])
def datashow():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='opcdata', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM rtdata"
    cur.execute(sql)
    u = cur.fetchmany(20)
    conn.close()
    jsondata = []
    for i in u:
        tem = {}
        tem['user_id'] = session.get('username')
        tem['tag_id'] = i[1]
        tem['tag_value'] = i[2]
        tem['tag_type'] = i[3]
        tem['tag_quality'] = i[4]
        tem['value_time'] = i[5]
        jsondata.append(tem)
    # print(jsondata)
    return json.dumps(jsondata)
    # return render_template('index.html',u=u)

@app.route('/yonghuming',methods=['GET','POST'])
def yonghuming():
   jsondata = []
   tem = {}
   tem['username'] = session.get('username')
   jsondata.append(tem)
   return json.dumps(jsondata)

@app.route('/log',endpoint='log')
def log():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "select * from user where username=" + repr(request.args.get('username')) + " and password=" + repr(request.args.get('password'))
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(request.args.get('password'))
        if len(results) == 1:
            # flash('登录成功')
            username = request.args.get('username')
            session['username'] = username
            return render_template('index.html')
        else:
            flash('用户名或密码不正确')
            return render_template('index0.html')
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()

@app.route('/regist',endpoint='regist')
def regist():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "insert into user(username,password,email,phone) values" +\
          '('+repr(request.args.get('username'))+','+\
          repr(request.args.get('password'))+','+\
          repr(request.args.get('email'))+','+\
          repr(request.args.get('email'))+')'
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        return render_template('index0.html')
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        flash('注册失败，该用户已存在')
        return render_template('index0.html')
    # 关闭数据库连接
    db.close()

# @user.before_request
# def before_user():
#     if 'username' in session:
#         return '已登录'
#         pass
#     else:
#         return render_template('index0.html')