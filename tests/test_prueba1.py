import pytest
from src.prueba1 import suma 

def test_suma():
    assert suma(1, 1) == 2 
    assert suma(0, 0) == 0
    assert suma(100, -100) == 0

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (1, 1, 2),
    (0, 0, 0),
    (100, -100, 0),
    (-15, -1, -16),
    (-3, 8, 5),
    (9, suma(-1, -2), 6)
    ]
)


def test_suma_params(input_n1, input_n2, expected):
    assert suma(input_n1, input_n2) == expected
from src.prueba1 import mayor


def test_mayor():
    assert mayor(1, 2) == 2 
    assert mayor(2, 1) == 2
    assert mayor(1, 1) == 0

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (1, 2, 2),
    (1, 0, 1),
    (100, -100, 100),
    (-15, -1, -1),
    (-3, 8, 8),
    (9, suma(-1, -2), 9)
    ]
)


def test_mayor_params(input_n1, input_n2, expected):
    assert mayor(input_n1, input_n2) == expected