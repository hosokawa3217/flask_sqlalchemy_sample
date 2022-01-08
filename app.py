from flask import Flask, config, render_template,redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy #←追加

import config
Config = config.Config
# print(Config.SQLALCHEMY_DATABASE_URI)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  Config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

class ToDo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	todo = db.Column(db.String(128), nullable=False)

@app.route('/')
def index():
      db.create_all()
      data = ToDo.query.all()
      for d in data:
            print(d.id,d.todo)
      return render_template('todo.html', data=data)

# @app.route('/add')
# def add():
#       newtodo = ToDo(todo="牛乳と卵を買う")
#       db.session.add(newtodo)
#       db.session.commit()
#       return redirect(url_for('index'))
      
# #以下追加↓	
@app.route('/add', methods=['POST'])
def add():
	todo = request.form['todo']
	new_todo = ToDo(todo=todo)
	db.session.add(new_todo)
	db.session.commit()
	return redirect(url_for('index'))
      
@app.route('/init')
def init():
     db.drop_all()
     db.create_all()
     return redirect(url_for('index'))

@app.route('/del_todo/<int:id>')
def del_todo(id):
	del_data = ToDo.query.filter_by(id=id).first()
	db.session.delete(del_data)
	db.session.commit()
	return redirect(url_for('index'))
      
if __name__ == '__main__':
	app.run()


      
      # db.drop_all()
      # db.create_all()
      # # db.session.add(newtodo)
      # db.session.commit()