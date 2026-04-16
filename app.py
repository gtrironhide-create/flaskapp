import sqlite3
from flask import Flask, render_template,request

app = Flask(__name__)



@app.route("/")
def home():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row   
    cursor = conn.cursor()
    products = conn.execute("SELECT * FROM products").fetchall()
    data = conn.execute('''
        SELECT category, SUM(quantity) as total
        FROM products
        GROUP BY category
    ''').fetchall()
    conn.close()
    categories = [row['category'] for row in data]
    stock = [row['total'] for row in data]
    
    return render_template("index.html",dat=products,categories=categories, stock=stock)



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route("/message",methods=['GET','POST'])
def message():
    username = request.form.get('username')
    email = request.form.get('gmail')
    msg = request.form.get('msg')
    return render_template("about.html",data=username)



if __name__ == "__main__":
    app.run(debug=True)