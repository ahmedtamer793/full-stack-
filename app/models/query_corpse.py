from app import db
from datetime import datetime

class QueryCorpse(db.Model):
    """جدول لتخزين كوارث الـ SQL اللي هتتبعت للمقبرة"""
    __tablename__ = 'query_corpses'

    id = db.Column(db.Integer, primary_key=True)
    bad_query = db.Column(db.Text, nullable=False)
    execution_plan = db.Column(db.Text, nullable=False)
    sarcastic_comment = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)