from flask import Blueprint, render_template

pages_bp = Blueprint('pages_bp', __name__)

@pages_bp.route('/', methods = ['GET'])
def default():
    return render_template('index.html')