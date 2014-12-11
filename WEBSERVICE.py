import sqlite3
from bottle import route, run, debug,  template ,  request

@route('/todo')
def todo_list():
    conn = sqlite3.connect('sessions.db')
    c = conn.cursor()
    c.execute("SELECT id, data FROM DATA")
    result = c.fetchall()
    c.close()
    output = template('templates/maketable', rows = result)
    return output

run(port = 8989, host = '178.62.102.58' )
