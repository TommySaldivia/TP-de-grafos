#existe_paso(grafo, vértice origen, vértice destino). Devuelve verdadero (true) si es 
# posible ir desde el vértice origen hasta el vértice destino, caso contrario retornará 
# falso (false);

def existe_paso(grafo, origen, destino):
    # 1. Verificamos si los vértices dados existen en el grafo
    if origen not in grafo or destino not in grafo:
        return False

    # 2. Si el origen es igual al destino, ya llegamos
    if origen == destino:
        return True

    # 3. Conjunto para rastrear por dónde ya pasamos y evitar bucles infinitos
    visitados = set()
    
    # 4. Pila para guardar la ruta que estamos explorando
    pila = [origen]

    while pila:
        actual = pila.pop()

        if actual == destino:
            return True

        if actual not in visitados:
            visitados.add(actual)

            vecinos = grafo.get(actual, [])
            
            for vecino in vecinos:
                if vecino not in visitados:
                    pila.append(vecino)

    return False
