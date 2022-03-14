from abc import ABC

from custom_exception.custom_problem import CustomProblem
from data_access_layer.customer_dal.customer_dal_interface import CustomerDAOInterface
from entities.customer_class import Customer


class CustomerDAOImp(CustomerDAOInterface, ABC):

    def create_customer_entry(self, customer: Customer) -> Customer:
        try:
            sql = ""
        except CustomProblem as e:
            pass
