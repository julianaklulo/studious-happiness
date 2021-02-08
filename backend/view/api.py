import sys
sys.path.append('.')

from flask import Flask
from flask_restful import Api
from backend.resources.category_resource import CategoryResource


app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, '/api/categories/', endpoint='categories')
api.add_resource(
    CategoryResource,
    '/api/categories/<int:id>/',
    endpoint='category'
)


@app.route('/')
def index():
    return 'Hello World!'


app.run(debug=True)
