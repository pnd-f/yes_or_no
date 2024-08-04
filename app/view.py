import requests
from flask import Flask, render_template, request, redirect, url_for
from app.utils import generate_answer


def include_views(app: Flask) -> None:
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            return render_template('index.html')
        elif request.method == 'POST':
            question = request.form['question']
            if question == '':
                return redirect(url_for('index'))
            url = app.config['ANSWER_API_URL']

            try:
                response = requests.get(url, timeout=1)
            except requests.Timeout:
                result_dict = generate_answer()
            except Exception as e:
                print(e)
                result_dict = generate_answer()
            else:
                result_dict = response.json()

            answer = {
                'question': question,
                'value': result_dict['answer'],
                'gif': result_dict['image'],
            }
            return render_template('answer.html', answer=answer)

    @app.route('/about', methods=['GET'])
    def about():
        return render_template('about.html')
