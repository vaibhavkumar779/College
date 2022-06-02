from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('KNNmodel.pkl','rb'))


@app.route('/')
def hello():
    return render_template("frontend.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    
    return render_template('frontend.html',pred='The Possibility of Crime is {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
