from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_japones = Restaurante('Japa', 'Japonês')

bebida_suco = Bebida('Suco de Morango', 10, 'Grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Pãozinho', 4, 'O melhor pão da região')
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
