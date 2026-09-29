"""
Eliminar el segundo elemento de lista repedito
fruta = ["uva", "pera", "uva", "naranja"]
                          ! (Eliminar este)
"""

fruta = ["uva", "pera", "uva", "naranja"]

idx = fruta.index("uva")

extraerPrimCoin = fruta.pop(0)

fruta.remove("uva")

fruta.insert(idx, extraerPrimCoin)

print(fruta)