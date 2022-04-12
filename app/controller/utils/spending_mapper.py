from app.controller.dto.spending_dto import SpendingDTO
from app.controller.dto.spending_type_dto import SpendingTypeDTO
from app.controller.dto.supplier_dto import SupplierDTO
from app.controller.utils.supplier_mapper import supplier_dao_to_dto


def spending_dao_to_dto(spending_dao) -> SpendingDTO:
    spending_type = spending_type_dao_to_dto(spending_dao.type)
    supplier = supplier_dao_to_dto(spending_dao.supplier)
    return SpendingDTO(spending_dao.id, spending_type, spending_dao.amount,
                       supplier, spending_dao.description, spending_dao.purchase_date)


def spending_type_dao_to_dto(spending_type_dao) -> SpendingTypeDTO:
    return SpendingTypeDTO(spending_type_dao.id, spending_type_dao.name)
