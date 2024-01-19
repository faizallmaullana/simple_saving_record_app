from flask import jsonify
from flask_restful import Resource
from app import db
from app.models.data import Incomes, Outcomes

class GetSumIncomeResource(Resource):
    def get(self):
        total_income = db.session.query(db.func.sum(Incomes.income)).scalar() or 0
        total_outcome = db.session.query(db.func.sum(Outcomes.outcome)).scalar() or 0

        net_income = total_income - total_outcome

        return jsonify(
            total=net_income,
            income=total_income,
            outcome=total_outcome
        )
            
