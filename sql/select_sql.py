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

sql = 'select * from blog_article'

cursor.execute(sql)

one = cursor.fetchone()

all = cursor.fetchall()

print('one %s' % one.__str__())
print('all %s' % all.__str__())

cursor.close()
conn.close()