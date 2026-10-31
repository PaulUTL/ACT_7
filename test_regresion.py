import pytest
from tienda import calcular_precio

@pytest.mark.parametrize("precio, descuento, expected", [
    (100, 10, 90),
    (200, 20, 160),
    (50, 0, 50),
    (100, 100, 0)])
def test_calcular_precio(precio, descuento, expected):
    assert calcular_precio(precio, descuento) == pytest.approx(expected)