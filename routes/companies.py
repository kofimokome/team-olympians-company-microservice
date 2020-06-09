from flask import Blueprint, request

companies = Blueprint('companies', __name__, template_folder='templates')


@companies.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return {'message': 'ok', 'method': 'POST'}
    else:
        return {'message': 'ok', 'method': 'GET'}


@companies.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def create(id):
    if request.method == 'POST':
        return {'message': 'ok', 'method': 'POST'}
    elif request.method == 'DELETE':
        return {'message': 'ok', 'method': 'DELETE'}
    else:
        return {'message': 'ok', 'method': 'GET'}
