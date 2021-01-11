from flask import Flask, request,jsonify
import sqlite3

app= Flask(__name__)

def db_connection():
    db = None
    try:
        db=sqlite3.connect('TODO.db')
    except sqlite3.error as e:
        print(e)
    return db

#  Fetch all data using GET
@app.route('/all', methods=['GET'])
def all():
    db = sqlite3.connect('TODO.db')
    cursor = db.cursor()
    cursor.execute('SELECT *FROM TODO')
    data=cursor.fetchall()
    db.close()
    return jsonify(data)

#  add data in table using POST
@app.route('/add', methods=['POST'])
def create():
    db = sqlite3.connect('TODO.db')
    cursor = db.cursor()
    item_description = request.json['item_description']
    time = request.json['time']
    sql = """INSERT INTO TODO (item_description, time) values( ?,?)"""
    cursor.execute(sql,(item_description, time))
    db.commit()
    return'</p> Database is update </p>'

# Search data using serial number
@app.route('/all/<int:serial>', methods=['GET'])
def search_serial(serial):
    db = sqlite3.connect('TODO.db')
    cursor = db.cursor()
    cursor.execute("""SELECT *FROM TODO WHERE serial=?""", (serial,))
    rows=cursor.fetchall()
    db.commit()
    return jsonify(rows)


# update the table using PUT
@app.route('/all/<int:serial>', methods=['PUT'])
def update_serial(serial):
    db = sqlite3.connect('TODO.db')
    cursor = db.cursor()
    sql = """UPDATE TODO SET item_description=?, time=? WHERE serial=?"""
    item_description=request.json["item_description"]
    time=request.json["time"]
    updated_TODO={
        "item_description":item_description,
        "time":time,
    }
    cursor.execute(sql, (item_description,time))
    db.commit()
    return jsonify(updated_TODO)


#  Delete data using particular serial number
@app.route('/all/<int:serial>', methods=['DELETE'])
def delete_serial(serial):
    db = sqlite3.connect('TODO.db')
    cursor = db.cursor()
    sql="""DELETE FROM TODO WHERE serial=?"""
    cursor.execute(sql,(serial,))
    db.commit()
    return "Id is deleted"

if __name__=='__main__':
    app.run(debug=True, threaded=True)

