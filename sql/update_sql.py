import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='laxian',
    db='mysite',
    charset='utf8'
)

cursor = conn.cursor()

sql_insert = 'insert into blog_article(title,content) values("下班别走","一起吃饭")'
sql_update = r"update blog_article set title = '我是标题' where id = 16"
sql_delete = 'delete from blog_article where id = 14'

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

all = cursor.fetchall()

print('all %s' % all.__str__())

cursor.close()
conn.close()