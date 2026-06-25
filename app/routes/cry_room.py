from flask import Blueprint, request, jsonify
from app.models.complaint import Complaint
from app.utils.logger import push_log_event
from app import db
from sqlalchemy import func

cry_room_bp = Blueprint('cry_room', __name__)

@cry_room_bp.route('/trending', methods=['GET'])
def get_trending():
    trending = db.session.query(
        Complaint.css_property, 
        func.count(Complaint.id).label('total')
    ).group_by(Complaint.css_property).order_by(func.count(Complaint.id).desc()).limit(5).all()
    
    push_log_event("GET /api/cry-room/trending", "200 OK", "Fetched CSS nightmares")
    return jsonify([{'property': t.css_property, 'count': t.total} for t in trending])

@cry_room_bp.route('/submit', methods=['POST'])
def submit_complaint():
    data = request.get_json() or {}
    story = data.get('story')
    raw_tag = data.get('css_property', 'Other')

    if not story:
        push_log_event("POST /api/cry-room/submit", "400 BAD REQUEST", "Empty story payload")
        return jsonify({'error': 'Payload cannot be empty.'}), 400

    clean_tag = Complaint.validate_tag(raw_tag)
    
    new_complaint = Complaint(
        username=data.get('username', 'Anonymous Backend Chad'),
        css_property=clean_tag,
        story=story
    )
    db.session.add(new_complaint)
    db.session.commit()

    push_log_event("POST /api/cry-room/submit", "201 CREATED", f"New complaint against {clean_tag}")
    return jsonify({'success': True, 'complaint': new_complaint.to_dict()}), 201

@cry_room_bp.route('/<int:complaint_id>/upvote', methods=['PATCH'])
def upvote(complaint_id):
    new_votes = Complaint.atomic_upvote(complaint_id)
    if new_votes is not None:
        push_log_event(f"PATCH /api/cry-room/{complaint_id}/upvote", "200 OK", f"Emotional damage: {new_votes}")
        return jsonify({'success': True, 'new_votes': new_votes}), 200
    
    return jsonify({'error': 'Complaint not found'}), 404