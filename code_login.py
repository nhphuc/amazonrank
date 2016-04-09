from flask import (Flask, render_template,request)
app = Flask(__name__)

from mongoengine import *
connect('amazon_rank',host='mongodb://amazon:mlab1234@ds015740.mlab.com:15740/amazon_rank')
class user(Document):
    username = StringField()
    password = StringField()

# ten= input('Nhap username : ')
# mk = input('nhap mk: ')
#viet ham kiem tra:
# for user in user.objects():
#     if ten == user.username and mk==user.password:
#         print('abc')
#     else:
#         print('Bạn đa nhập sai username : ')


@app.route('/', methods=['GET', 'POST'])
def template():
    if request.method == 'POST':   # neu phuong thuc la gui du lieu len thi cho phep chay
        x=request.form['username']
        y=request.form['password']
        print(x) #kiem tra thu thoi
        print(y)

        # duyet nguoi dung co tren mang trong danh sach
        for nguoi_dung in user.objects():
        # so sanh :
            if x == nguoi_dung.username and y == nguoi_dung.password :
            #     return "Ôi ra rồi sướng quá anh "+ x +" ơi "
            # else:
            #     return "không phải anh Hào, không sướng"
                return "trang chu"
            else:
                return render_template('login1.html')
    return render_template('login1.html')

if __name__ == '__main__':
    app.run()

