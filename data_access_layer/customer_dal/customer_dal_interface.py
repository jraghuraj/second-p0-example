from abc import ABC, abstractmethod


class CustomerDAOInterface(ABC):

    @abstractmethod
    def insert_into_customers_table(self, customer_obj):
        pass

    @abstractmethod
    def delete_from_customers_table_by_id(self, customer_id: int) -> bool:
        pass
