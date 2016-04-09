from flask import Flask, render_template
from flask import request
app = Flask(__name__)

from mongoengine import *
connect('test',host = 'mongodb://nguyenhao120691:nguyenhao120691@ds019470.mlab.com:19470/nguyenhao120691')
class user(Document):
    username = StringField()
    password = StringField()
#data = user(username ='xa_lach_boy',password = 'hello')
# data.save()
# print(data.username)
# print(data.password)
# print(data.user)
# print(data.id)
ten= input('Nhap username : ')
mk = input('nhap mk: ')

#viet ham kiem tra:


# for user in user.objects():
#     if ten == user.username and mk==user.password:
#         print('abc')
#     else:
#         print('Bạn đa nhập sai username : ')




if __name__ == '__main__':
    app.run()
