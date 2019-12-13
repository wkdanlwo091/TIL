from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # return "Hello World"
    return render_template('index.html')
@app.route('/t4ir')
def t4ir():
    return 'This is T4IR'
@app.route('/ssafy')
def ssafy():
    return 'SSAFY'
@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end = datetime.datetime(2020, 4, 21)
    td = end - today
    return f'{td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>HAHAHAHAHAHAHAHAH</h1>'

@app.route('/html_line')
def html_line():
    return """ #여러 줄 보내기 
    <h1>여러줄을 보내봅시다. </h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>   
    """
@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다. ! {name}님'
    return render_template('greeting.html', html_name = name) ##html_name을 일반적으로 html_name이라고 사용 

@app.route('/cube/<int:number>') ## 기본이 스트링이라서 정수가 들어오면 int로 
def cube(number):
    # return f'{number}의 3제곱 {number**3} 입니다. '
    result = number **3 
    return render_template("cube.html", result = result, number = number )

@app.route('/movie')
def movie():
    movies = ['겨울왕국', '미니게임', '백두산', '블랙위도우']
    return render_template('movie.html', movies = movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age_in_html = age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/isitbirth')
def isitbirth():
    today =  datetime.now()

    if today.month == 8 and today.day == 17:
        result = True
    else:
        result = False
    return render_template('isitbirth.html', result = result)

@app.route('/vonvon/<name>')
def vonvon(name):
    return render_template('vonvon.html', html_name = name)##이름 받아오기

@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    print(name)
    first_list = ['잘생김', '못생김', '어중간']
    second_list = ['착함', '나쁨', '어중간']
    third_list = ['강함', '약함', '어중간']
    a = random.choice(first_list)
    b = random.choice(second_list)
    c = random.choice(third_list)
    return render_template('godmademe.html', first_list = a , second_list = b, third_list = c)



if __name__=="__main__":
    app.run(debug=True)


