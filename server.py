from flask import Flask, render_template

app = Flask(__name__)

@app.route('/lists')
def render_lists():
    
    users = [
       {'first_name' : 'Michael', 'last_name' : 'Choi'},
       {'first_name' : 'John', 'last_name' : 'Supsupin' },
       {'first_name' : 'Mark', 'last_name' : 'Guillen'},
       {'first_name' : 'KB', 'last_name' : "tonel"}
    ]
    return render_template("index.html", user_info = users)

   

if __name__=="__main__":
    app.run(debug=True)