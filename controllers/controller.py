from re import sub
from flask import render_template
from app import app
from modules.calculator import Calculator

@app.route('/add')
def add_numbers(num1, num2):
    return render_template('index.html', title='Add', add_numbers=add_numbers(num1, num2))

@app.route('/subtract')
def subtract_numbers(num1, num2):
    return render_template('index.html', title='Subtract', subtract_numbers=subtract_numbers(num1, num2))