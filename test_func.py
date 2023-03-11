'''Testando a funcionlidade de valor do desconto.
Introduzir valores fixos para as variáveis da função e comentei 
algumas partes da mesma para a realização do teste. 
'''

def desafio():
    # if __name__ == '__main__':
    # valor_unitario = float(input('Valor unitário do produto: '))
    # quantidade = int(input('Quantidade: '))
        valor_unitario = 100
        quantidade = 10
        desconto = 1

        if quantidade >= 10 and quantidade <= 99:
            desconto = 0.95
        elif quantidade >= 100 and quantidade <= 999:
            desconto = 0.90
        elif quantidade >= 1000:
            desconto = 0.85

        # No desconto o completo de até 1 é o valor do desconto.
        # Ex: 0,85 tem 15% de desconto. -> 1 - 0,85 = 0.15

        valor_com_desconto = valor_unitario * desconto * quantidade
        return valor_com_desconto

        # print(f'Valor total sem desconto: {valor_com_desconto} R$')
        # print(f'Valor total com desconto: {valor_com_desconto:.2f} R$')

def test_desafio():
    assert desafio() == 950
    
 

