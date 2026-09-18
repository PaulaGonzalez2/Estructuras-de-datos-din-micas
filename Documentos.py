
class Documento:
    tiempo_pag=1.0

    def __init__(self,nombre,n_paginas):
        self.nombre=nombre
        self.n_paginas= n_paginas
        self.pagina_actual=0

    def imprimir_pag(self):
        if self.pagina_actual<self.n_paginas:
            self.pagina_actual += 1

    def completado(self):
        return self.pagina_actual>=self.n_paginas
    
    def __str__(self):
        return f"{self.nombre}-{self.n_paginas} páginas"

    
