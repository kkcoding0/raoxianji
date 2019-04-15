from app import *
import json
import pymysql

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
    print(jsondata)
    return json.dumps(jsondata)
    # return render_template('index.html',u=u)