from app.helper.validator.schema.details import *
from app.services.details_service import Details
from flask_sqlalchemy import SQLAlchemy
from app.utils.db import *
from flask_json_schema import JsonSchema, JsonValidationError
#from app.helper.validator.schema.details import *
from flask import jsonify, request, Response, session , g

import sys

@app.route('/status',methods=['GET'])
def get_datetime():
    try:
        return (Details.get_date_time())
    except:
        return sys.exc_info()[0]


@app.route('/read',methods=['GET'])
def get_all():
    try:
        return jsonify({"Details":Details.get_all_details()})
    except:
        return sys.exc_info()[0]

@app.route('/update/<int:id>',methods=['PUT'])
def update(id):
    request_data=request.get_json()
    response = Details.update_detail(id,request_data['Status'])
    try:
        if response:
            return Response("Detail updated", 200, mimetype='application/json')
        else:
            return {"MSG":"Status is accepted / rejected can not change"}
    except:
        return sys.exc_info()[0]
