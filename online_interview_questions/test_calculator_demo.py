from calculator_demo import Calculator


def test_add():
    obj = Calculator()
    assert obj.add(1, 3) == 4