from flask import Flask,render_template
from flask import request


from mongoengine import *

app = Flask(__name__)

connect('amazon_rank',host='mongodb://amazon:mlab1234@ds015740.mlab.com:15740/amazon_rank')

class data_rank(Document):
    username=StringField()
    id_sanpham=StringField()
    group=StringField()
    rank=StringField()
    time=StringField()
rank_list=data_rank.objects

# for rank in rank_list:
#     print(rank.rank)

@app.route('/testsanpham', methods=['GET', 'POST'])
def sanpham():
    # return "hello"
    if request.method == 'POST':
        x=request.form['group']
        y=request.form['rank']
        z=request.form['time']
        return "Ôi ra rồi sướng quá anh "+ x +" ơi " +" rank " +y +" time "+ z
    return render_template("user_sanpham.html",rank_list=rank_list)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
