"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general

    Reglas:
    - Si units < 0 -> ValueError
    - Si un producto no existe en PRICES -> ValueError
    - Si un producto aparece varias veces, se acumulan unidades

    Ejemplo:
    [("Pan", 2), ("Huevos", 1), ("Pan", 1)] ->
      ({"Pan": 4.2, "Huevos": 2.3}, 6.5)
    """
    coste_producto ={}
    total = 0.0
    for producto, unidades in cart:
        if unidades < 0:
            raise ValueError("no se pueden negativos")
        if producto not in PRICES:
            raise ValueError(f"producto {producto} no existe")
        coste_actual = PRICES[producto] * unidades
        if producto in coste_por_producto:
            coste_por_producto[producto] = coste_por_producto[producto] + coste_actual
        else:
            coste_por_producto[producto] = coste_actual
          total_general = total_general + coste_actual
    return (coste_por_producto, total_general)



    raise NotImplementedError("Implementa checkout(cart)")
