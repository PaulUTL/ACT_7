import pytest
from tienda import calculo_envio

@pytest.mark.parametrize("subtotal, expected", [
    (300, 80),
    (499, 80),
    (500, 0),
    (501, 0),
    (600, 0),])
def test_calculo_envio(subtotal, expected):
    assert calculo_envio(subtotal) == expected

def test_calculo_envio_negativo():
    with pytest.raises(ValueError):
        calculo_envio(-100)