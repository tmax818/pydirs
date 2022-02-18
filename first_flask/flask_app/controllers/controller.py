from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.table_name import table_name

@app.route('/table_name')
@app.route('/')
def index():
    return render_template('index.html', table_name=Model.get_all())

@app.route('/table_name/new')
def new():
    return render_template("new.html")

@app.route('/table_name/create', methods=['post'])
def create():
    print(request.form)
    model.save(request.form)
    return render_template("new.html")

@app.route('/table_name/<int:id>')
def show(id):
    data = {
        'id': id
    }
    return render_template('show.html', model=Model.get_one(data))

@app.route('/table_name/<int:id>/edit')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit.html', model=Model.get_one(data))

@app.route('/table_name/<int:id>/update', methods=['post'])
def update():
    Model.update(request.form)
    return redirect('/table_name')

@app.route('/table_name/<int:id>/delete')
def delete():
    data = {
        'id': id
    }
    Model.destroy(data)
    return redirect('/')