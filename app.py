from flask import Flask,render_template,request
from firebase import Firebase
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact',methods=["GET","POST"])
@app.route('/contact1',methods=["GET","POST"])
def contact():
    if request.method=="POST":
        return render_template('contact1.html')
    return render_template('contact.html')

@app.route('/game1')
def game1():
    return render_template('game1.html')
@app.route('/game2')
def game2():
    return render_template('game2.html')
@app.route('/game3')
def game3():
    return render_template('game3.html')
@app.route('/game4')
def game4():
    return render_template('game4.html')
@app.route('/game5')
def game5():
    return render_template('game5.html')
@app.route('/game6')
def game6():
    return render_template('game6.html')
@app.route('/game7')
def game7():
    return render_template('game7.html')
@app.route('/game8')
def game8():
    return render_template('game8.html')
@app.route('/game9')
def game9():
    return render_template('game9.html')

@app.route('/all_games',methods=["GET","POST"])
@app.route('/all_games1',methods=["GET","POST"])
def allgames():
    if request.method=="POST":
        return render_template('all_games1.html',dislplay=True)
    return render_template('all_games.html',display=False)

@app.route('/surprise')
def sursprise():
    return render_template('surprise.html')


if __name__=="__main__":
    app.run(debug=True)
