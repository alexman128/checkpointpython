from flask import Flask, redirect, url_for, request
import json
import files
import databases
from app_config import config

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'you-will-never-guess'

users = []

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      #request.data
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('nm')
      users.append(user)
      return redirect(url_for('success', name=user))

@app.route('/listusers')
def list_users():
   return f"Los usuarios que se han loggeado hasta este momento han sido: {users}"

@app.route('/escribearchivo')
def escribearchivo():
   nombre = config['users_csv']
   #archivo = files.CSVFile(config['users_csv'], {'test1': 1, 'test2': 2}, 'w')
   archivo = files.CSVFile(config['users_csv'], users, 'w')
   archivo.write_content()
   return f'Se escribio en el archivo{nombre}'

@app.route('/leedelabd')
def leedelabd():
   q = databases.Test()
   q.connect()
   q.setQuery("select * from Sales")
   q.do_query()
   q.format_results()
   r = q.output_results()
   return f"Los resultados son: {r}"


if __name__ == '__main__':
   app.run(debug=True)
