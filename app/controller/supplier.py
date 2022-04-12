from flask_restful import Resource
from app import db
from .dto.response import Response
from app.model.supplier_dao import SupplierDao
from flask_restful import reqparse

from .dto.supplier_dto import SupplierDTO
from .utils import supplier_mapper

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, default=None)
parser.add_argument('id', type=str, default=None)


class Supplier(Resource):
    def get(self):
        args = parser.parse_args()
        id = args['id']

        if id is None:
            suppliers = SupplierDao.query.all()
            res = []
            for supplier in suppliers:
                res.append(SupplierDTO(supplier.id, supplier.name).__json__())
        else:
            supplier = SupplierDao.query.get(id)
            res = SupplierDTO(supplier.id, supplier.name).__json__()
        if res is None:
            return Response(message=f"No supplier was found with id {id}").__json__(), 404

        return Response(object=res).__json__(), 201

    def post(self):
        args = parser.parse_args()
        supplier = SupplierDao(name=args['name'])
        db.session.add(supplier)
        db.session.commit()
        return Response(message='Created',
                        object=supplier_mapper.supplier_dao_to_dto(supplier).__json__()).__json__(), 201

    def delete(self):
        args = parser.parse_args()
        name = args['name']
        if name is None:
            return Response(message=f"Name is needed").__json__(), 400

        supplier = SupplierDao.query.filter_by(name=name).first()
        if supplier is None:
            return Response(message=f"No supplier was found with name {name}").__json__(), 404

        db.session.delete(supplier)
        db.session.commit()
        return Response(message=f"Supplier {name} deleted").__json__(), 200
