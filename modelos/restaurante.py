from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'NOME'.ljust(20)} | {'CATEGORIA'.ljust(20)} | {'AVALIAÇÃO'.ljust(20)} | STATUS")

        for restaurante in cls.restaurantes:
            print(
                f'{restaurante.nome.ljust(20)} | '
                f'{restaurante.categoria.ljust(20)} | '
                f'{str(restaurante.media_avaliacoes).ljust(20)} | '
                f'{restaurante.status}'
            )   

    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria

    @property
    def ativo(self):
        return self._ativo
    
    @property
    def avaliacao(self):
        return self._avaliacao

    @property
    def status(self):
        return 'Ativo' if self._ativo else 'Inativo'

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        
        soma_notas = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)

        return media
    
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')

        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome: {item.nome} | Preço: R${item.preco} | Descrição: {item.descricao}'
            else:
                mensagem = f'{i}. Nome: {item.nome} | Preço: R${item.preco} | Tamanho: {item.tamanho}' 
            print(mensagem)
    
    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)