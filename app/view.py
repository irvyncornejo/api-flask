import json
import re
from flask import Blueprint
from flask import request

from .models.task import Task
from .response import response
from .response import not_found
from .response import bad_request
from .schemas import task_schema
from .schemas import tasks_schema
from .schemas import params_task_schema

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

@api_v1.route('/tasks', methods=['GET'])
def get_task():
    page = int(request.args.get('page', 1))#dic
    order = request.args.get('order', 'desc')
    print(page)

    tasks = Task.get_by_page(order, page)
    
    return response(tasks_schema.dump(tasks))

@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task_id(id):
    task = Task.query.filter_by(id=id).first()
    if task is None:
        return not_found()
    return response(task_schema.dump(task))

@api_v1.route('/tasks', methods=['POST'])
def create_task():
    json = request.get_json(force=True)

    #Error
    error = params_task_schema.validate(json)
    if error:
        print(error)
        return bad_request()
    
    task = Task.new(json['title'], json['description'], json['deadline'])

    if task.save():
        return response(task_schema.dump(task))
    return bad_request()

@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    
    task = Task.query.filter_by(id=id).first()
    if task is None:
        return not_found()
    json = request.get_json(force=True)

    task.title = json.get('title', task.title)
    task.description = json.get('description', task.description)
    task.deadline = json.get('deadline', task.deadline)
    if task.save():
        return response(task_schema.dump(task))
    return bad_request()


@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    if task is None:
        return not_found()

    if task.delete():
        return response(task_schema.dump(task))
    return bad_request()