from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Staff')
def Staff():
    return render_template("Staff.html")


@app.route('/Customer')
def Customer():
    return render_template("Customer.html")

@app.route('/Allergens')
def Allergens():
    return render_template("add_allergens.html")

@app.route('/Allergens_result',methods =['POST'])
def Allergens_success():
    a =request.form["customer_id"]
    b= request.form["a"]
    conn = sqlite3.connect('parlor_management.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO allergens VALUES (?,?)', (a,b))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("add_allergens_success.html",y=b)

@app.route('/Cart')
def Cart():
    return render_template("cart.html")

@app.route('/add_items')
def add_items():
    return render_template("add_items.html")

@app.route('/add_items_result',methods=['POST'])
def add_items_result():
    a =request.form["customer_id"]
    b= request.form["fav"]
    conn = sqlite3.connect('parlor_management.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO Cart VALUES (?,?)', (a,b))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("cart.html")

@app.route('/view_cart')
def view_cart():
    conn = sqlite3.connect('parlor_management.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Cart')
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("view_cart.html",results=items)

@app.route('/Search')
def search():
    return render_template("search.html")

@app.route('/Search_result',methods=['POST'])
def search_results():
    key = request.form['key']
    conn = sqlite3.connect('parlor_management.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM flavors where flavor_name like ?',('%'+ key +'%',))
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("search_result.html",results=items)

@app.route('/Filter')
def Filter():
    return render_template("filter.html")

@app.route('/Suggestion')
def Feedback():
    return render_template("suggestions.html")

@app.route('/Suggestions_result',methods =['POST'])
def Suggestions_success():
    a =request.form["customer_id"]
    b= request.form["s"]
    conn = sqlite3.connect('parlor_management.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO Suggestions VALUES (?,?)', (a,b))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("suggestions_success.html")


if __name__ == '__main__' :
    app.run(debug=False)
    
