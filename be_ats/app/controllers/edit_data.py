from flask import request, jsonify
from flask_restful import Resource
from app import db
from sqlalchemy import desc

from app.models.data import Incomes, Outcomes

class Incomes_Resource(Resource):
    def get(self):
        datas = Incomes.query.order_by(desc(Incomes.created_at)).all()
        result = []
        for data in datas:
            result.append({
                'income': data.income,
                'keterangan': data.keterangan,
                'tanggal': data.created_at.strftime("%d %B %Y")
            })
        return jsonify(result=result)
    
    def post(self):
        income = request.json.get('income')
        keterangan = request.json.get('keterangan')
        value = Incomes(
            income=income,
            keterangan=keterangan,
        )
        db.session.add(value)
        db.session.commit()

        return {
            'message': 'Income'
    }


class Outcomes_Resource(Resource):
    def get(self):
        datas = Outcomes.query.order_by(desc(Outcomes.created_at)).all()
        result = []
        for data in datas:
            result.append({
                'outcome': data.outcome,
                'keterangan': data.keterangan,
                'tanggal': data.created_at.strftime("%d %B %Y")
            })
        return jsonify(result=result)

    def post(self):
        outcome = request.json.get('outcome',None)
        keterangan = request.json.get('keterangan',None)
        value = Outcomes(
            outcome=outcome,
            keterangan=keterangan,
        )
        db.session.add(value)
        db.session.commit()
