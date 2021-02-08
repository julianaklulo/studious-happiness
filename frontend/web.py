import sys
sys.path.append('.')

from flask import Flask, render_template, request, redirect, url_for
from backend.controller.category_controller import CategoryController
from backend.models.category import Category


app = Flask(__name__)
category_controller = CategoryController()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/categories/create', methods=['GET'])
def new_category():
    return render_template('create_category.html')


@app.route('/categories', methods=['GET'])
def list_categories():
    categories = category_controller.read_all()
    return render_template('list_categories.html', categories=categories)


@app.route('/categories', methods=['POST'])
def create_category():
    name = request.form.get('name')
    description = request.form.get('description')
    category = Category(name, description)
    category_controller.save(category)
    return redirect(url_for('list_categories'))


@app.route('/categories/<int:id>', methods=['GET', 'POST'])
def edit_category(id: int):
    category = category_controller.read_by_id(id)
    if request.method == "POST":
        category.name = request.form.get('name')
        category.description = request.form.get('description')
        category_controller.update(category)
        return redirect(url_for('list_categories'))
    return render_template('edit_category.html', category=category)


@app.route('/categories/<int:id>/delete', methods=['GET'])
def delete_category(id: int):
    category = category_controller.read_by_id(id)
    category_controller.delete(category)
    return redirect(url_for('list_categories'))


app.run(debug=True)
