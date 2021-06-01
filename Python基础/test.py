import requests
import json
import time
import pymysql
import datetime
import traceback

def get_conn():
    # 建立连接
    conn = pymysql.connect(host="127.0.0.1", user="root", password="201314", db="data", charset="utf8")
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def update_vac():
    cursor = None
    conn = None
    try:
        li = get_vac()
        conn, cursor = get_conn()
        sql = "insert into vac(update_time, country, num) values(%s, %s, %s)"
        sql_query = "select %s=(select update_time from vac order by id desc limit 1)"  # 对比当前最大时间戳
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新数据")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新到最新数据")
        else:
            print(f"{time.asctime()}已是最新数据！")

    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

    pass



def get_vac():
    url3 = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=VaccineSituationData'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }
    r3 = requests.get(url3, headers)
    res3 = json.loads(r3.text)
    # print(res3, type(res3))
    data_all3 = res3["data"]
    # print(data_all3, type(data_all3))
    vac = []
    update_time = datetime.datetime.now().strftime('%Y-%m-%d')
    for n in data_all3['VaccineSituationData']:
        country = n['country']
        num = n['total_vaccinations']
        vac.append([update_time, country, num])

    # print(vac)
    return vac


get_vac()
update_vac()
