import numpy as np 
from flask import *
import pickle 
from tensorflow.keras.models import load_model
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("D:\\Pyenv\\Submit\\University_Admission_Predication\\Flask\\templates"))

app = Flask(__name__)

model = pickle.load(open("D:\\Pyenv\\Submit\\University_Admission_Predication\\Training\\university.pkl", "rb"))

@app.route('/')
def index():
    template = env.get_template('home.html')
    return render_template(template)

@app.route('/details')
def home():
    template = env.get_template('details.html')
    return render_template(template)

@app.route("/predict", methods = ["POST","GET"])
def predict():
    min1 = [290.0, 92.0, 1.0, 1.0, 1.0, 6.8, 1]
    max1 = [340.0, 120.0, 5.0, 5.0, 5.0, 9.92, 2]

    values_list = list(request.form.values()) 
    fname = values_list[0]
    req_values = values_list[1:8]

    k = [float(x) for x in req_values]
    print(k)
    p = []
    for i in range(7):
        l = (k[i]-min1[i])/(max1[i]-min1[i])
        p.append(l)
    prediction = model.predict([p])
    print(prediction)
    output = prediction[0]
    if output== False:
        template = env.get_template('noChance.html')
        return render_template(template, name=fname)
    else:
        template = env.get_template('chance.html')
        return render_template(template, name=fname)

if __name__ == "__main__":
    app.run(debug=True)