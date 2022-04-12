from app.model.spending_type_dao import SpendingTypeDao
from app.controller.dto.supplier_dto import SupplierDTO


def supplier_dao_to_dto(supplier_dao) -> SupplierDTO:
    return SupplierDTO(supplier_dao.id, supplier_dao.name)
