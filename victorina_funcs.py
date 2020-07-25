import pymysql, ast
from pymysql.cursors import DictCursor


def get_last_index():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='vk',
        charset='utf8mb4',
        cursorclass=DictCursor
    )

    with connection.cursor() as cursor:
        query = """SELECT COUNT(*) FROM tests;"""
        cursor.execute(query)
        for row in cursor:
            connection.close()
            return row['COUNT(*)']


def update_test(id, q_a):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='vk',
        charset='utf8mb4',
        cursorclass=DictCursor,
        autocommit=True
    )
    cursor = connection.cursor()
    cursor.execute(f"""UPDATE tests SET q_a='{str(q_a)}' WHERE id={int(id)}""")
    cursor.close()


def get_question(test_id, question_id):
    questions_and_answers = []
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
        if str(row['id']) == str(test_id):
            questions_and_answers = ast.literal_eval(row['q_a'])
            break
    connection.close()
    for q_a in questions_and_answers:
        if str(q_a['question_id']) == str(question_id):
            question_and_answer = q_a
            break
    question_and_answer['count_of_questions'] = len(questions_and_answers)
    return question_and_answer


update_test(10, '{"test_info": {"logo": "https://sun9-13.userapi.com/c853428/v853428960/22dcd5/4Xolgz3aO74.jpg", "desc": "Данный тест поможет вам определиться гей ли вы...", "statistic": {"viewes": 0, "likes": 0, "dislikes": 0}, "name": "Натурал или гей?"}, "q_a": [{"test_id": 1, "question_id": 1, "question": "Who is GAY?", "answers": ["timofey", "timogey", "timoleg", "timodayn"], "right_answer": "timoleg", "image_link": ""}, {"test_id": 1, "question_id": 2, "question": "Who is not GAY?", "answers": ["oleg", "olegsandr", "olegavr", "neoleg"], "right_answer": "oleg", "image_link": "https://sun9-72.userapi.com/c855432/v855432089/24e755/FcWiasXz2GE.jpg"}]}')
