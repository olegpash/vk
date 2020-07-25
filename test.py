import pymysql, ast
from pymysql.cursors import DictCursor


d = {'test_info': {'logo': 'https://sun9-13.userapi.com/c853428/v853428960/22dcd5/4Xolgz3aO74.jpg',
                   'desc': 'Данный тест поможет вам определиться гей ли вы...',
                   'statistic': {'viewes': 0, 'likes': 0, 'dislikes': 0},
                   'name': 'Натурал или гей?'},
     'q_a': [{'test_id': 1,
               'question_id': 1,
               'question': 'Who is GAY?',
               'answers': ['timofey', 'timogey', 'timoleg', 'timodayn'],
               'right_answer': 'timoleg',
               'image_link': ''},
              {'test_id': 1,
               'question_id': 2,
               'question': 'Who is not GAY?',
               'answers': ['oleg', 'olegsandr', 'olegavr', 'neoleg'],
               'right_answer': 'oleg',
               'image_link': 'https://sun9-72.userapi.com/c855432/v855432089/24e755/FcWiasXz2GE.jpg'}]}
d = {"test_info": {"logo": "https://sun9-13.userapi.com/c853428/v853428960/22dcd5/4Xolgz3aO74.jpg", "desc": "Данный тест поможет вам определиться гей ли вы...", "statistic": {"viewes": 0, "likes": 0, "dislikes": 0}, "name": "Натурал или гей?"}, "q_a": [{"test_id": 1, "question_id": 1, "question": "Who is GAY?", "answers": ["timofey", "timogey", "timoleg", "timodayn"], "right_answer": "timoleg", "image_link": ""}, {"test_id": 1, "question_id": 2, "question": "Who is not GAY?", "answers": ["oleg", "olegsandr", "olegavr", "neoleg"], "right_answer": "oleg", "image_link": "https://sun9-72.userapi.com/c855432/v855432089/24e755/FcWiasXz2GE.jpg"}]}



def add_test():
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
    cursor.execute(f'''INSERT INTO tests (id, q_a) VALUES (10, "{str(d)}")''')
    cursor.close()

#print(str(d).replace("'", '"'))
add_test()