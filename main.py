from flask import Flask, jsonify, request
import victorina_funcs, main_page

app = Flask(__name__)
site_url = 'http://127.0.0.1:5000/api'


def get_inputs(method_name):
    test_id, question_id, vk_user_id, user_answer = -1, -1, -1, -1
    input_data = str(request).replace("<Request '", '').replace("' [GET]>", '').strip().replace(
        site_url + f'/{method_name}?', '').split('&')
    for i in input_data:
        if 'test_id=' in i:
            test_id = i.replace('test_id=', '')
        if 'question_id=' in i:
            question_id = i.replace('question_id=', '')
        if 'vk_user_id=' in i:
            vk_user_id = i.replace('vk_user_id=', '')
        if 'user_answer=' in i:
            user_answer = i.replace('user_answer', '')
    return test_id, question_id, vk_user_id, user_answer


@app.route('/api/get_question', methods=['GET'])
def get_question():
    test_id, question_id, nothing, nothing_x2 = get_inputs('get_question')
    if test_id == -1 or question_id == -1:
        return f'Data transmission error!'
    question = victorina_funcs.get_question(test_id, question_id)
    return question


@app.route('/api/update_test_user_statistics', methods=['GET'])
def update_test_user_statistics():
    test_id, question_id, vk_user_id, user_answer = get_inputs('update_test_user_statistics')
    if test_id == -1 or question_id == -1 or vk_user_id == -1 or user_answer == -1:
        return f'Data transmission error!'
    return f'This method updates user test stats.'


@app.route('/api/get_test_user_statistics', methods=['GET'])
def get_test_user_statistics():
    test_id, nothing, vk_user_id, nothing_x2 = get_inputs('update_test_user_statistics')
    if test_id == -1 or vk_user_id == -1:
        return f'Data transmission error!'
    return f'This method returns user test stats.'


@app.route('/api/main_page/top_ten', methods=['GET'])
def top_ten():
    return main_page.get_first_10_pages()


if __name__ == '__main__':
    app.run(debug=True)
