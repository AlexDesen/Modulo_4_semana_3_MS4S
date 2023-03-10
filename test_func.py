

"""
OLÁ PROFESSOR, NÃO CONSIGO GERAR UM TESTE
"POSITIVO" MESMO INSERINDO OS VALORES CORRETOS NA FUNÇÃO, APONTA O MEU ERRO, OBRIGADO.
"""
'''
NÃO ACISTIR A TUA AULA AO VIVO POIS A MESMA 
SÓ FICA DISPONÍVEL APÓS EVIARMOS O DESAFIO DA SEMANA
'''
def teste(valor_unitario, quantidade):
  
    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    # No desconto o completo de até 1 é o valor do desconto.
    # Ex: 0,85 tem 15% de desconto. -> 1 - 0,85 = 0.15

    return valor_unitario * desconto * quantidade
  

def test_teste():
        
    assert teste(100,10) == 9500
    