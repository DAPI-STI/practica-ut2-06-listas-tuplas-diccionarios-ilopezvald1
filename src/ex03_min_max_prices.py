"""
EX03 (Tuplas)
Devolver el mínimo y el máximo de una lista.
"""

def min_max_prices(prices: list[float]) -> tuple[float, float]:
    """
    Devuelve una tupla (mínimo, máximo).

    - Si prices está vacía, lanza ValueError.
    """
    minimo = min(prices)
    maximo = max(prices)
    if not prices:
        raise ValueError("lista vacia")
    return (minimo, maximo)
    raise NotImplementedError("Implementa min_max_prices(prices)")
