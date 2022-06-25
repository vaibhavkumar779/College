from flask import Flask,request, url_for, redirect, render_template, Response
# import pickle
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io



def graph_data(year = '', age = '', gender = '', crime = ''):
    if year == '' and age == '' and gender == '' and crime == '' :
        return 0
    with open('FinalDataSet.csv', 'r') as file:
        data = file.readlines()
        file.close()
    c_data = [[x.strip() for x in line.replace('\n', '').split(',')] for line in data]
    required = []
    for line in c_data[1:]:
        if year == line[1] and age == line[2] and gender == line[3]:
            required.append(line)
    return [[line[0], line[int(crime)]] for line in required]





app = Flask(__name__)

# model=pickle.load(open('KNNmodel.pkl','rb'))


@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    return render_template('home.html')

@app.route('/output',methods=['POST'])
def output():    
    # print(request.form['year'])
    fig = plt.Figure()
    # ax = fig.subplots()
    # ax.plot([1, 2])
    input_data = graph_data(year = request.form['year'], age = request.form['age'], gender = request.form['gender'], crime = request.form['crime'])
    print(input_data,"\n\n")
    x = [i[0] for i in input_data] 
    y = [int(i[1]) for i in input_data]

    # Plot the figure.
    plt.figure(figsize=(15,10))
    freq_series = pd.Series(y)
    ax = freq_series.plot(kind="bar")
    ax.set_title("Crime Rate Comparision")
    ax.set_xlabel("State / UT")
    ax.set_ylabel("Crime Rate")
    ax.set_xticklabels(x)

    rects = ax.patches

    # Make some labels.
    labels = [i for i in y]

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, height + 1, label, ha="center", va="bottom"
        )
    
    # plt.bar([i for i in range(max(map(lambda x: x[1], input_data)))],[i[1] for i in input_data], bottom = [i[0] for i in input_data], width = 0.4, color ='blue')
    # fig.show()
    plt.show()
    # output = io.BytesIO()
    # FigureCanvas(fig).print_png(output)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
    # return render_template('output.html', name = plt.show())
    # return render_template('output.html')
    # return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
