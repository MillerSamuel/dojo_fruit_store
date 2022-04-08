from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fruit_data=[request.form['strawberry'],request.form['raspberry'],request.form['apple']]
    user_data=[request.form['first_name'],request.form['last_name'],request.form['student_id']]
    print(f"charging {user_data[0]+user_data[1]} for {int(fruit_data[0])+int(fruit_data[1])+int(fruit_data[2])} fruits")
    return render_template("checkout.html",fruit_data=fruit_data,user_data=user_data)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    