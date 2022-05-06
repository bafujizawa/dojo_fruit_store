from email.mime import image
from fileinput import filename
from re import A
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

fruit_options = [
{'apple': 'An edible fruit produced on a tree, known for its sweet taste.  Great for cooking, baking, and ciders!'},
{'blackberry': 'A bush fruit identified by its juicy, clustered berries.  Once ripe, it has a sweet and savory flavor!'},
{'raspberry': 'While not as sweet as blackberries, these tart but sweet treats pack a punch of flavor!'},
{'strawberry': 'The king of berries.  These berries boast a fruit, sweet and juicy flavor that everyone in the family will love!'}
]


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberries = request.form['strawberry']
    raspberries = request.form['raspberry']
    apples = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    id = request.form['student_id']
    print("Charging John Doe for 5 fruit")
    print(request.form)
    return render_template("checkout.html", strawberries=strawberries, raspberries = raspberries, apples = apples, first_name=first_name, last_name=last_name , id=id)

@app.route('/fruits')         
def fruits(fruit_options=fruit_options):
    return render_template("fruits.html", fruit_options = fruit_options)

if __name__=="__main__":   
    app.run(debug=True)    