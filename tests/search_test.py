import pytest
from unittest.mock import patch
from contextlib import nullcontext as does_not_raise
from find_items import search_product


@pytest.fixture(scope='session', autouse=True)
def get_search_product_list():
    names_list = search_product()
    return names_list

@pytest.mark.parametrize(
    "item_name, value, expectation",
    [
        ('Худи', True, does_not_raise()),
        ('Толстовка', True, does_not_raise()),
        ('Футболка', False, does_not_raise()),
    ]
)

def test_search_product(item_name, value, expectation, get_search_product_list):
    with expectation:
        assert (item_name in get_search_product_list) == value