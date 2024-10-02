class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, elemento):
        self.pila.append(elemento)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()  # Elimina y devuelve el último elemento agregado
        else:
            return "La pila está vacía"

    def esta_vacia(self):
        return len(self.pila) == 0  # Verifica si la pila está vacía

    def ver_pila(self):
        return self.pila  # Muestra el contenido de la pila

# Ejemplo de uso
p = Pila()
p.apilar('hola')
p.apilar(21)
print(p.ver_pila())  # Resultado: ['hola', 21]
p.desapilar()  # Elimina el 21
print(p.ver_pila())  # Resultado: ['hola']
