from flask import render_template, request, redirect, url_for

from app import app

data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        name2 = request.form.get('name2')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        if name and name2 and age and city and hobby:
            data.append({'name': name, 'name2': name2, 'age': age, 'city': city, 'hobby': hobby})
            return redirect(url_for('index'))
    return render_template('profile.html', data=data)