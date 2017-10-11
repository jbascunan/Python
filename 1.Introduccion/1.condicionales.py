fruta = "manzana"
#fruta = "kiwi"

if fruta == "kiwi":
    print("el valor es kiwi")
elif fruta == "manzana":
    print("es manzana")
else:
    print("no es kiwi")

# if en una sola linea
mensaje = "kiwi" if fruta == "kiwis" else "nooo"

print(mensaje)
