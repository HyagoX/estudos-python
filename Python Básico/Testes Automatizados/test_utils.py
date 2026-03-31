# Toda função que vai executar um teste, tambem precisa do prefixo test_...
from utils import dar_oi, somar

# Quanto mais cenários de teste criados, melhor
def test_dar_oi():
    assert dar_oi('Hyago') == 'Oi, meu nome é Hyago'

def test_somar_normal():
    assert somar(10, 5)==15
def test_somar_igual():
    assert somar(1, 1) == 2
def test_somar_negativo():
    assert somar(-5, 7) == 2

# Para realizar os testes automaticamente, basta digitar pytest no terminal, e ele retornará os erros