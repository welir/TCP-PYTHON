#!%/usr/bin/python3.4

import sqlite3
from bottle import route, run, debug,  template ,  request
from gmaps import Geocoding

@route('/todo')
def todo_list():
    conn = sqlite3.connect('sessions.db')
    c = conn.cursor()
    c.execute("SELECT id, dt, data FROM DATA")
    result = c.fetchall()
    c.close()
    output = template('templates/maketable', rows = result)
    return output

@route('/map')
def todo_list():
    conn = sqlite3.connect('sessions.db')
    c = conn.cursor()
    c.execute("SELECT id, dt, data FROM DATA")
    result = c.fetchall()
    c.close()
    output = template('templates/maps', rows = result)
    return output
api = Geocoding()

api.geocode("somwhere")

print(api.reverse(51.123, 21.123))
print(api.base)
run(port = 8989, host = '192.168.0.156' )



