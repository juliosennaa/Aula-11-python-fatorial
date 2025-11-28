import pytest 
from fatorial import fatorial

casos_teste = [
    (0, 1),      
    (1, 1),      
    (2, 2),      
    (3, 6),      
    (4, 24),     
    (5, 120),    
    (8, 40320) 
]

@pytest.mark.parametrize("n, esperado", casos_teste)
def test_fatorial_casos_validos(n, esperado):
    assert fatorial(n) == esperado