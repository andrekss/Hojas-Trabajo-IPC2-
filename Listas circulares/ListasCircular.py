from nodo import *

class listaCircular:
    def __init__(self):

        self.primero = None

    def insertar(self, receta):

      if self.primero is None:
            self.primero = Nodo(receta)
            self.primero.siguiente = self.primero
      else:
            actual = Nodo(receta,self.primero.siguiente)
            self.primero.siguiente = actual

    def recorrer(self):
        if self.primero is None:
            return 
        actual = self.primero
        print('Paciente: ', actual.receta.paciente, 'Fecha de nacimiento: ', actual.receta.fechaNac, ' Doctor: ', actual.receta.doctor, 'Colegiado: ', actual.receta.colegiado, ' Fecha de cita: ', actual.receta.fechaCita, 'Hora de cita: ', actual.receta.horaCita, 'Tipo de consulta: ', actual.receta.tipoConsulta, ' Tratamiento: ', actual.receta.tratamiento)
        
        while actual.siguiente != self.primero:
         actual = actual.siguiente
         print('Paciente: ', actual.receta.paciente, 'Fecha de nacimiento: ', actual.receta.fechaNac, ' Doctor: ', actual.receta.doctor, 'Colegiado: ', actual.receta.colegiado, ' Fecha de cita: ', actual.receta.fechaCita, 'Hora de cita: ', actual.receta.horaCita, 'Tipo de consulta: ', actual.receta.tipoConsulta, 'Tratamiento: ', actual.receta.tratamiento)
    
    def eliminar(self, colegiado,  horaCita,fechaCita):
    
       actual = self.primero
       anterior = None
       noEncontrado = False

       while actual and actual.receta.colegiado != colegiado and actual.receta.fechaCita != fechaCita and actual.receta.horaCita != horaCita:
           
            anterior = actual
            actual = actual.siguiente

            if actual == self.primero:
                noEncontrado = True
                print('No econtrado')
                break

            if not noEncontrado:
             if anterior is not None:
                    anterior.siguiente = actual.siguiente
                    actual.siguiente = None
            else:
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente
    # Hoja de trabajo
    def Modificar(self, paciente, fechaCita, nuevoTratamiento ,horaCita):

      noEncontrado = False
      actual = self.primero

      while actual and (actual.receta.paciente != paciente or actual.receta.fechaCita != fechaCita or actual.receta.horaCita != horaCita):
            actual = actual.siguiente

            if actual == self.primero:
                noEncontrado = True
                break

      if not noEncontrado:
            actual.receta.tratamiento = nuevoTratamiento

