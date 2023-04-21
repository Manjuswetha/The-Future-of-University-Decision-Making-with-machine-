import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
app=Flask(__name__)
#Import necessary libraries
from tensorflow.keras.models import load_model

#model=pickle.load(open('university.pkl','rb'))
#load model trained model
#load your trained model
model=load_model('model.h5')
@app.route('/')
def home():
     return render_template('index.html')
@app.route('/y_predict',methods=['POST'])
def y_predict():
					
    #min max scaling
    min1=[290.0,92.0,1.0,1.0,1.0,6.8,0.0]
    max1=[340.0,120,.0,5.0,5.0,9.92,1.0]
    k=[float(x) for x in request.form.valuse()]
    p=[]
    for i in range(7):
        l=(k[i]-min1[i])/(max1[i]-min1[i])
        p.append(1)
    prediction=model.predict([p])
    print(prediction)
    output=prediction[0]
    if(output==False):
         return render_template('nochance.html', predition_test='you Dont have a chance of getting')   
    else:
         return render_template('chance.html',predition_test='you have a chance of gettting admission')

if _name_=="_main_":
   app.run(debug=False)
 