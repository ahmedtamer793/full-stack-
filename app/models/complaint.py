from app import db
from datetime import datetime

class Complaint(db.Model):
    __tablename__ = 'complaints'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), default='Anonymous Backend Chad')
    css_property = db.Column(db.String(50), nullable=False)
    story = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    VALID_CSS_TAGS = ['z-index', 'flexbox', 'margin', 'position', 'grid', 'float']

    @classmethod
    def validate_tag(cls, tag):
        if tag not in cls.VALID_CSS_TAGS:
            return "Other"
        return tag

    @classmethod
    def atomic_upvote(cls, complaint_id):
        """
        Atomic Update لحل مشكلة الـ Race Conditions
        UPDATE complaints SET votes = votes + 1 WHERE id = X
        """
        complaint = cls.query.get(complaint_id)
        if complaint:
            complaint.votes = cls.votes + 1
            db.session.commit()
            db.session.refresh(complaint) 
            return complaint.votes
        return None

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'css_property': self.css_property,
            'story': self.story,
            'votes': self.votes,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }