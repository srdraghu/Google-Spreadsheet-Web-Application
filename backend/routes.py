 
from flask import Blueprint
routes = Blueprint('routes', __name__)

@routes.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong"}