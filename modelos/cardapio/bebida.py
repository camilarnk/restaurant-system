from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
    
    @property
    def tamanho(self):
        return self._tamanho
    
    def aplicar_desconto(self):
        self.preco -= self.preco * 0.05
