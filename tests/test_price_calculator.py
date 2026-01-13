import pytest
from src.price_calculator import PriceCalculator

@pytest.fixture(scope="module")
def calculator():
    return PriceCalculator()

def test_normal_calculation(calculator):
    # 普通情况
    assert calculator.calculate_final_price(100, 20, 10) == 70

def test_zero_discount(calculator):
    # 没有优惠
    assert calculator.calculate_final_price(50, 0, 0) == 50

def test_exact_discount(calculator):
    # 优惠正好等于价格 -> 0
    assert calculator.calculate_final_price(30, 10, 20) == 0

def test_discount_exceeds_price(calculator):
    # 优惠合计超过价格，应该返回 0 而不是负数
    assert calculator.calculate_final_price(50, 30, 30) == 0

def test_negative_price_input(calculator):
    # 负数参数应抛出异常
    with pytest.raises(ValueError):
        calculator.calculate_final_price(-100, 10, 20)
