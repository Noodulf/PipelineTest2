from app import calculate_discount

def test_discount():
    # If price is 100 and discount is 20, result should be 80
    assert calculate_discount(100, 20) == 80
