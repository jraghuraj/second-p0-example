from custom_exception.custom_problem import CustomProblem
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

def test_create_customer_operational_error_caught():
    try:
        pass
    except CustomProblem as e:
        pass

def test_delete_customer_operational_err0r_caught():
    try:
        customer_dao.delete_from_customers_table_by_id(0)
        assert False
    except CustomProblem as e:
        pass
