from flask import Blueprint

student_bp = Blueprint("student", __name__)

@student_bp.route("/")
def home():
    return "Student route works"