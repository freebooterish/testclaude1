# hello.py
print("After small update,Hello, GitHub!")


def calculate_discount(price, percentage):
    """
    计算折扣后的价格
    
    Args:
        price (float): 原价
        percentage (float): 折扣百分比 (0-100)
    
    Returns:
        float: 折扣后的价格
    
    Raises:
        ValueError: 当折扣百分比无效时
    """
    if not 0 <= percentage <= 100:
        if percentage < 0:
            raise ValueError("折扣百分比不能为负数")
        raise ValueError("折扣百分比不能超过100%")
    
    return price * (1 - percentage / 100)
