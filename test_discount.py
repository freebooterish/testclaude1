import pytest
from hello import calculate_discount


class TestCalculateDiscount:
    """测试 calculate_discount 函数的各种场景"""

    def test_normal_discount(self):
        """测试正常折扣情况：100元打20%折扣应为80元"""
        result = calculate_discount(100, 20)
        assert result == 80

    def test_zero_discount(self):
        """测试零折扣情况：100元打0%折扣应为100元"""
        result = calculate_discount(100, 0)
        assert result == 100

    def test_full_discount(self):
        """测试全额折扣情况：100元打100%折扣应为0元"""
        result = calculate_discount(100, 100)
        assert result == 0

    def test_float_price_discount(self):
        """测试浮点数价格：99.99元打10%折扣应近似89.991"""
        result = calculate_discount(99.99, 10)
        expected = 89.991
        assert abs(result - expected) < 0.001

    def test_negative_percentage_raises_error(self):
        """测试负数百分比应抛出ValueError"""
        with pytest.raises(ValueError, match="折扣百分比不能为负数"):
            calculate_discount(100, -10)

    def test_percentage_over_100_raises_error(self):
        """测试超过100%的百分比应抛出ValueError"""
        with pytest.raises(ValueError, match="折扣百分比不能超过100%"):
            calculate_discount(100, 150)

    def test_zero_price(self):
        """测试价格为0的边界情况"""
        result = calculate_discount(0, 20)
        assert result == 0

    def test_small_discount(self):
        """测试小额折扣的精度"""
        result = calculate_discount(10.50, 5)
        expected = 9.975
        assert abs(result - expected) < 0.001