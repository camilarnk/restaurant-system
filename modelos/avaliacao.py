class Avaliacao:
    def __init__(self, cliente, nota):
        if nota < 0 or nota > 5:
            raise ValueError("Nota deve estar entre 0 e 5")
        
        self._cliente = cliente
        self._nota = nota

    def __str__(self):
        return f'{self._cliente} | {self._nota}'
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def nota(self):
        return self._nota