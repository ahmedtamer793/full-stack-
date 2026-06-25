from flask import Blueprint, request, jsonify
from app import db
from sqlalchemy import text
from app.models.query_corpse import QueryCorpse
from app.utils.logger import push_log_event

graveyard_bp = Blueprint('graveyard', __name__)

@graveyard_bp.route('/autopsy', methods=['POST'])
def perform_autopsy():
    """
    بياخد الـ SQL من اليوزر، بيحط قبله EXPLAIN QUERY PLAN 
    عشان يرجع خطة التنفيذ في SQLite ويفضح الـ Performance.
    """
    data = request.get_json() or {}
    raw_query = data.get('query', '').strip()

    if not raw_query.upper().startswith("SELECT"):
        return jsonify({"error": "We only autopsy SELECT queries here. No dropping tables, hacker."}), 400

    explain_sql = f"EXPLAIN QUERY PLAN {raw_query}"
    
    try:
        result = db.session.execute(text(explain_sql))
        plan_steps = [row[3] for row in result]
        plan_text = "\n".join(plan_steps)
        
        sarcasm = "Clean execution."
        if "SCAN" in plan_text:
            sarcasm = "SCAN TABLE detected. You just read the whole dictionary to find one word. A true N+1 artist."
            
        corpse = QueryCorpse(bad_query=raw_query, execution_plan=plan_text, sarcastic_comment=sarcasm)
        db.session.add(corpse)
        db.session.commit()

        push_log_event("SQL_AUTOPSY", "200 OK", "Analyzed terrible query")
        return jsonify({
            "plan": plan_text,
            "sarcasm": sarcasm
        }), 200

    except Exception as e:
        push_log_event("SQL_AUTOPSY", "500 ERROR", "Syntax so bad it crashed the analyzer")
        return jsonify({"error": f"SQL Error: {str(e)}"}), 400