class robot:
    def __init__(self):
        self.pila_tareas = []
        self.tarea_actual = None
        self.ejecutando = False

    def agregar_tarea(self, tarea):
        self.pila_tareas.append(tarea)

    def hay_tareas(self):
        if len(self.pila_tareas) > 0:
            return True
        else:
            return False

    def sacar_tarea(self):
        if self.hay_tareas():
            self.tarea_actual = self.pila_tareas.pop()
            return True
        else:
            return False

    def terminar_tarea(self):
        self.tarea_actual = None
