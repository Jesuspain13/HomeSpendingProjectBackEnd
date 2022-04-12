from flask_restful import Resource
from app import db
from .dto.response import Response
from app.model.spending_dao import SpendingDao
from flask_restful import reqparse

from .utils import spending_mapper

parser = reqparse.RequestParser()
parser.add_argument('description', type=str, default=None)
parser.add_argument('supplier_id', type=str, default=None)
parser.add_argument('type_id', type=str, default=None)
parser.add_argument('amount', type=str, default=None)
parser.add_argument('name', type=str, default=None)
parser.add_argument('id', type=str, default=None)


class Spending(Resource):
    def get(self) -> (Response, int):
        args = parser.parse_args()
        id = args['id']

        if id is None:
            spendings = SpendingDao.query.all()
            res = []
            for spending in spendings:
                print(spending)
                res.append(spending_mapper.spending_dao_to_dto(spending).__json__())
        else:
            spending = SpendingDao.query.get(id)
            res = spending_mapper.spending_dao_to_dto(spending).__json__()
        if res is None:
            return Response(message=f"No spending was found with id {id}").__json__(), 404

        return Response(object=res).__json__(), 201

    def post(self):
        args = parser.parse_args()
        spending = SpendingDao(description=args['description'], amount=args['amount'],
                               type_id=args['type_id'], supplier_id=args['supplier_id'])
        db.session.add(spending)
        db.session.commit()
        return Response(message='Created',
                        object=spending_mapper.spending_dao_to_dto(spending).__json__()).__json__(), 201

    def delete(self):
        args = parser.parse_args()
        id = args['id']
        if id is None:
            return Response(message=f"Id is needed").__json__(), 400

        spending = SpendingDao.query.filter_by(id=id).first()
        if spending is None:
            return Response(message=f"No spending was found with id {id}").__json__(), 404

        db.session.delete(spending)
        db.session.commit()
        return Response(message=f"Spending {id} deleted").__json__(), 200
