from paquete import Gato, Leon
from paquete import CONSTANTES
from paquete import creador_gato

gato = Gato("nuevo gato por paquete")
leon = Leon("nuevo leon por paquete")
gato2 = creador_gato("nada")

print(gato.nombre)
print(leon.nombre)
print(CONSTANTES)
print(gato2.nombre)
