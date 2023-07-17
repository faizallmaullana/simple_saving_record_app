from flask import request, jsonify
from flask_restful import Resource
from app import db

from app.models.data import Incomes, Outcomes

# Sisa Bersih
class GetSumIncomeResource(Resource):
    def get(self):
        incomess = Incomes.query.all()
        result1 = 0
        for amount in incomess:
            result1 += amount.income

        outcomess = Outcomes.query.all()
        result2 = 0
        for amount in outcomess:
            result2 += amount.outcome

        result3 = result1 - result2
        return jsonify(total=result3)