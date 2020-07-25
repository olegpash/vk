import pymysql, ast
from pymysql.cursors import DictCursor


def get_first_10_pages():
    sp = []
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='vk',
        charset='utf8mb4',
        cursorclass=DictCursor
    )
    cursor = connection.cursor()
    cursor.execute("""SELECT id, q_a FROM tests""")
    for row in cursor:
        row = ast.literal_eval(row['q_a'])['test_info']
        sp.append(row)
        if len(sp) == 10:
            connection.close()
            return {'answer': sp}
