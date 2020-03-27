import sys
import re 


class Validar:
    def __init__(self, expresion):
        self.expresion = expresion


    def ValidarExpresiones(self):
       lenguaje = re.match('(?=\w*[A-Z])(?=\w*\d){3}(?=\w*[a-z]){3}',self.expresion) 
       if lenguaje is None:
            print("No valida ") 


       else:

            print("Valida") 

sys.argv 
palabra = sys.argv[1]

print(palabra)     


clase = Validar(palabra)
clase.ValidarExpresiones()      
