import pytest
from src.item import Item


@pytest.fixture
def item1():
    item = Item("Смартфон", 10000, 20)
    return item

@pytest.fixture
def item2():
    item = Item("Ноутбук", 20000, 5)
    return item

def test_all_items(item1, item2):
    assert Item.all == [item1, item2]

def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount(item1, item2):
    Item.pay_rate = 0.8
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000