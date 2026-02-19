from app import safe_add

def test_add():
    assert safe_add(2, 3) == 5
