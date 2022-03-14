from abc import ABC

from data_access_layer.customer_dal.customer_dal_interface import CustomerDAOInterface


class CustomerDAOImp(CustomerDAOInterface, ABC):
    pass
