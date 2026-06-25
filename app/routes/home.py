# app/routes/home.py
from flask import Blueprint, render_template
from app.models.complaint import Complaint
from app import db
from sqlalchemy import func

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    total_traumas = db.session.query(func.count(Complaint.id)).scalar() or 0
    total_members = db.session.query(func.count(func.distinct(Complaint.username))).scalar() or 0
    
    return render_template('home.html', 
                        total_traumas=total_traumas, 
                        total_members=total_members + 12)