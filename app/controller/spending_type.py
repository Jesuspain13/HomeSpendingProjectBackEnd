from typing import Tuple

from flask_restful import Resource
from app import db
from .dto.response import Response
from app.model.spending_type_dao import SpendingTypeDao
from flask_restful import reqparse

from .utils.spending_mapper import spending_type_dao_to_dto

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, default=None)
parser.add_argument('id', type=str, default=None)


class SpendingType(Resource):
    def get(self) -> Tuple[dict, int]:
        args = parser.parse_args()
        id = args['id']

        if id is None:
            spending_types = SpendingTypeDao.query.all()
            res = []
            for spending_type in spending_types:
                res.append(spending_type_dao_to_dto(spending_type).__json__())
        else:
            spending_type = SpendingTypeDao.query.get(id)
            res = spending_type_dao_to_dto(spending_type).__json__()
        if res is None:
            return Response(message=f"No supplier was found with id {id}").__json__(), 404

        return Response(object=res).__json__(), 201

    def post(self):
        args = parser.parse_args()
        spending_type = SpendingTypeDao(name=args['name'])
        db.session.add(spending_type)
        db.session.commit()
        return Response(message='Created',
                        object=spending_type_dao_to_dto(spending_type).__json__()).__json__(), 201

    def delete(self):
        args = parser.parse_args()
        name = args['name']
        if name is None:
            return Response(message=f"Name is needed").__json__(), 400

        spending_type = SpendingTypeDao.query.filter_by(name=name).first()
        if spending_type is None:
            return Response(message=f"No spending type was found with name {name}").__json__(), 404

        db.session.delete(spending_type)
        db.session.commit()
        return Response(message=f"Spending type {name} deleted").__json__(), 200
