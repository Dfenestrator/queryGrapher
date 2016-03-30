from flask.ext.mysql import MySQL
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
from contextlib import closing

# configuration
DEBUG = True

# variables for database access
HOST = 'sql3.freemysqlhosting.net'
USER = 'sql3112872'
PASSWD = 'QMWVSEkv1r'
DATABASE = 'sql3112872'

# create application
app = Flask(__name__)
mysql = MySQL()

app.config.from_object(__name__)
app.config['MYSQL_DATABASE_HOST'] = HOST
app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWD
app.config['MYSQL_DATABASE_DB'] = DATABASE
mysql.init_app(app)

def connect_db():
    return mysql.connect()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

#Custom query
@app.route('/getData', methods=['GET'])
def getData():

    result = None

    cursor = g.db.cursor()

    #get all interesting queries in one shot, divide them up later
    query=request.args.get('query')

    cursor.execute(query)

    # Get column headers
    result = [[word[0] for word in cursor.description]]

    #get data
    queryRows = cursor.fetchall()
    for row in queryRows:
        result.append(row)
        
    return jsonify(result=result)

@app.route('/')
def mainPg():
    return render_template('customQuery.html')

if __name__ == '__main__':
    app.run()
