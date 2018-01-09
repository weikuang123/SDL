from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField

app = Flask(__name__)


@app.route('/individual')
def individual():
    return render_template('IndividualSummary.html')


@app.route('/recipient')
def recipient():
    return render_template('Recipient.html')


@app.route('/maincustomise')
def maincustomise():
    return render_template('MainCustomise.html')




if __name__ == '__main__':
    app.run()

