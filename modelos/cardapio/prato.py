from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): # Prato herda ItemCardapio
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    @property
    def descricao(self):
        return self._descricao
    
    def aplicar_desconto(self):
        self.preco -= self.preco * 0.08