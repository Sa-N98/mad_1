from flask import Flask, render_template as rt, request, redirect, url_for
from model import *
import os


current_dir = os.path.abspath(os.path.dirname(__file__))

app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ \
os.path.join(current_dir,"Database.sqlite3")

db.init_app(app)
app.app_context().push() # programming stack


@app.route('/', methods=['GET','POST'] )
def home():
    if request.method == "POST":
        user_email = request.form['EMAIL']
        user_password = request.form['PASSWORD']
        
        user = users.query.filter_by(email = user_email).first()

        if user:
            if user_password == user.password:
                if user.user_type == 'admin':
                    return redirect(url_for('admin'))
                elif user.user_type == 'customer':
                    return redirect(url_for('customer'))
                else:
                    return redirect(url_for('theater'))
    return rt('home.html')



@app.route('/admin', methods=['GET','POST'] )
def admin():
    return rt('admin.html')

@app.route('/customer', methods=['GET','POST'] )
def customer():
    return rt('customer.html')

@app.route('/theater', methods=['GET','POST'] )
def theater():
    return rt('theater.html')








@app.route('/sqldemo', methods=['GET','POST'] )
def sqldemo():
    #basic:

    # data = users.query.all()
    # print( 'id', 'name' ,'email', 'user_type')
    # for i in data:
    #     print(i.id, i.name , i.email, i.user_type)
    
    
    #filter:

    data = users.query.filter(users.user_type == 'customer', users.name.like("a%")).all()
    print( 'id', 'name' ,'email', 'user_type')
    for i in data:
        print(i.id, i.name , i.email, i.user_type)

    #like:

    # data = users.query.filter(users.name.like('a%')).first()
    # # print( 'id', 'name' ,'email', 'user_type')
    # # for i in data:
    # print( data.id,  data.name ,  data.email,  data.user_type)

    
    return "sql_demo check vs_code terminal for output"




@app.route('/datashow', methods=['GET','POST'] )
def datashow():
    data = users.query.filter(users.user_type == 'customer').all()
    return rt('data.html', var= data)









if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')