class Produto:
    def __init__(self, name, price):
        self.name = name
        self._price = price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price += float(new_price)
            return True
        else:
            return False

p1 = Produto('Mouse Brabo', 100)
print(p1.price)
nwpr = float(input('Type how much you want to save: '))
p1.price = nwpr
print(f'{p1.name} - {p1.price}')

# Isto nao seria a forma ideal de mudar o preço, pois a propriedade nao pode ter um preço negativo, ou um preço em formato de string. Para evitar isso, nós vamos usar o método setter 'oficial'
