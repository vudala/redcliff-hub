from flask import Blueprint
from flask import request as FlaskRequest
api_bp = Blueprint('api_bp', __name__)

from .db import queries

@api_bp.route('/api/scaling', methods = ['GET'])
def get_scaling():
    start = int(FlaskRequest.args.get('start'))
    end = int(FlaskRequest.args.get('end'))
    result = { 'result' : queries.scaling(start, end) }
    return result