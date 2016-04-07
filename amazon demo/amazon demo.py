from flask import Flask,render_template
from flask import request


from mongoengine import *

app = Flask(__name__)

connect('amazon_rank',host='mongodb://amazon:mlab1234@ds015740.mlab.com:15740/amazon_rank')

# class data_rank(Document):
#     username=StringField()
#     id_sanpham=StringField()
#     group=StringField()
#     rank=StringField()
#     time=StringField()
# rank_list=data_rank.objects

# for rank in rank_list:
#     print(rank.rank)

#http://docs.mongoengine.org/guide/defining-documents.html#embedded-documents
class Xephang(EmbeddedDocument):
    rank = StringField()
    time = StringField()

class Nhom(EmbeddedDocument):
    ten_nhom = StringField()
    xephang = ListField(EmbeddedDocumentField(Xephang))

class Sanpham(EmbeddedDocument):
    ten_sanpham = StringField()
    nhom = ListField(EmbeddedDocumentField(Nhom))

class Username(Document):
    username= StringField()
    sanpham = ListField(EmbeddedDocumentField(Sanpham))



# comment1 = Comment(content='Good work!')
# comment2 = Comment(content='Nice article!')
# page = Page(comments=[comment1, comment2])

xephang1 = Xephang(rank='123',time='130116')
nhom1 = Nhom(ten_nhom='kitchen',xephang=[xephang1])
sanpham1= Sanpham(ten_sanpham="ABCD",nhom=[nhom1])
username = Username(username="testsanpham",sanpham=[sanpham1])

username.save()

@app.route('/testsanpham', methods=['GET', 'POST'])
def sanpham():
    # return "hello"
    if request.method == 'POST':
        x=request.form['group']
        y=request.form['rank']
        z=request.form['time']
        return "Ôi ra rồi sướng quá anh "+ x +" ơi " +" rank " +y +" time "+ z
    # return render_template("user_sanpham.html",rank_list=rank_list)
    return 'Hello World!'

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
