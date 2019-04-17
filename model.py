from app import *
import json
import pymysql
from flask import request
import traceback
from flask import flash

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
        tem['user_id'] = i[0]
        tem['tag_id'] = i[1]
        tem['tag_value'] = i[2]
        tem['tag_type'] = i[3]
        tem['tag_quality'] = i[4]
        tem['value_time'] = i[5]
        jsondata.append(tem)
    # print(jsondata)
    return json.dumps(jsondata)
    # return render_template('index.html',u=u)

@app.route('/log',endpoint='log')
def log():
    # 查询用户名及密码是否匹配及存在
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from user where username=" + repr(request.args.get('username')) + " and password=" + repr(request.args.get('password'))
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(request.args.get('password'))
        if len(results) == 1:
            flash('登录成功')
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
    # 查询用户名及密码是否匹配及存在
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
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