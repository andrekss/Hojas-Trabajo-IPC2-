from nodo import *

class ListaDoble:
    def __init__(self):
         self.primero = None
         self.ultimo = None

    def modificar(self, receta0, receta1):
         actual = self.primero
         encontrar = False
         while actual != None and not encontrar:
             if actual.receta == receta0:
                  actual.receta = receta1
                  encontrar = True
             else:
                 actual = actual.siguiente
         if not encontrar:
             print("sin encontrar")     

    def Agregar(self, receta):
         newNodo = Nodo(receta)
         if self.primero == None:
             self.primero = newNodo
             self.ultimo = newNodo
         else:
             newNodo.anterior = self.ultimo
             self.ultimo.siguiente = newNodo
             self.ultimo = newNodo

    def recorrer(self):
         actual = self.primero
         while actual != None:
            print(actual.receta)
            actual = actual.siguiente

    def busqueda(self, receta):
         actual = self.primero
         encontrar = False
         while actual != None and not encontrar:
             if actual.receta == receta:
                encontrar = True
             else:
                 actual = actual.siguiente
         return encontrar

    def eliminar(self, receta):
        actual = self.primero
        encontrar = False
        while actual is not None and not encontrar:
             if actual.receta == receta:
                 encontrar = True
             else:
                 actual = actual.siguiente
        if actual != None:
            if actual.anterior == None:
                self.primero = actual.siguiente
                if actual.siguiente != None:
                     actual.siguiente.anterior = None
                else:
                    self.ultimo = None
            elif actual.siguiente == None:
                  self.ultimo = actual.anterior
                  actual.anterior.siguiente = None
            else:
                  actual.anterior.siguiente = actual.siguiente
                  actual.siguiente.anterior = actual.anterior