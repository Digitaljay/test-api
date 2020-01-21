from flask import Flask
from firebase import firebase
app = Flask(__name__)
firebase = firebase.FirebaseApplication("https://phases-b3adc.firebaseio.com/phase", None)


@app.route('/')
def hello_world():
    d=firebase.get("https://phases-b3adc.firebaseio.com","phase")
    return str(d)


app.run(debug=True)
