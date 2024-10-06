from flask import Flask, render_template as rt
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
    return rt('home.html')

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



if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')