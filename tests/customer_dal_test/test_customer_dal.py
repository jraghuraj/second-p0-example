from data_access_layer.customer_dal.customer_dal_imp import CustomerDAOImp
from entities.customer_class import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_entry_success():
    test_customer = Customer(0, "tired", "boy")
    return_customer = customer_dao.insert_into_customers_table(test_customer)
    assert return_customer != 0


def test_delete_customer_entry_success():
    result = customer_dao.delete_from_customers_table_by_id(-1)
    assert result
