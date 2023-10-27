import pytest
from src.prueba2_1_3 import division
from src.prueba2_1_4 import par_impar


def test_division():
    assert division(8 , 2) == 4
    assert division(10, 0) == "Error, no se puede dividir entre cero"
    assert division(9, 3) == 3   

def test_par_impar():
    assert par_impar(8) == "Es par"
    assert par_impar(1) == "Es impar"
    assert par_impar(9) == "Es impar"
