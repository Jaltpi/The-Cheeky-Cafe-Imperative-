# from module import get_product_name, validate_product_price, select_item_delete, select_item_update # Products
# from module import get_courier_name, validate_phone_number
import builtins
from unittest import mock
import pytest
from unittest.mock import Mock, patch
import unittest

def get_product_name() -> str:
        """This function checks to make sure products name isn't an empty string. It returns a string."""

        try:
            product_name = input("What is the name of this product?: ").title()
            if product_name == "":
                raise ValueError()
        except ValueError:
            print(f"Error: No name was detected in the input.")
        else:
            return product_name
        
@patch("builtins.input")
@patch("builtins.print")       
def test_get_product_name_with_blank(mock_print, mock_input):
    # Assemble
    mock_input = Mock()
    mock_input.return_value = ""
    # Act
    get_product_name()
    # Assert
    mock_print.assert_called_with("Error: No name was detected in the input.")
    

class TestProducts(unittest.TestCase):
    @patch("builtins.input")
    def test_get_product_name_with_no_entry(self):
        with self.assertRaises(ValueError):
            get_product_name()
############################################################################################################
# class TestCourier(unittest.TestCase):
#     pass
#############################################################################################################
# class TestOrders(unittest.TestCase):
#     pass

# if __name__ == "__main__":
#     unittest.main()