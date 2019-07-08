class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions
    print(self.__class__)

class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40
    #print(self.__class__)

raisin_salad = SpecialPotatoSalad("potatoes", "celery", "onions")
print(raisin_salad.raisins)

#Notes on: Method Resolution Order
#class Foo(object):
#  def __init__(self):
#    self.x = 40
#
#f1 = Foo()
#f2 = Foo()
#print(f1.x)
#print(f2.x)
#f2.x = 50
#print(f1.x)
#print(f2.x)
#print(f1)
#print(f2)
