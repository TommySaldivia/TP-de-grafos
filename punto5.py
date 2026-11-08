# eliminar_arista(vértice, destino). Elimina y devuelve del vértice si encuentra una
# arista que coincida con el destino dado –el primero que encuentre–, si devuelve None
# significa que no se encontró la arista destino en el vértice, y por ende no se elimina 
# ningún elemento

class Grafo:
    def __init__(self):
        # Diccionario para almacenar los vértices y sus listas de adyacencia
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, origen, destino):
        # Aseguramos que ambos vértices existan antes de conectarlos
        if origen in self.adyacencia and destino in self.adyacencia:
            self.adyacencia[origen].append(destino)

    def eliminar_arista(self, vertice, destino):
        # 1. Verificamos que el vértice de origen exista en el grafo
        if vertice in self.adyacencia:
            lista_aristas = self.adyacencia[vertice]
            
            # 2. Comprobamos si existe la arista hacia el destino
            if destino in lista_aristas:
                lista_aristas.remove(destino)
                return destino
                
        return None
