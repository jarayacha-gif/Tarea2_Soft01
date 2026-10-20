# Tarea 2 - Semana 8 - Jehidam Araya Chaves - Soft01
# Facturacion de un restaurante

# Declaracion de variables
producto = input("Ingrese el nombre del producto: ")
valorUnitario = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))
tipoPlato = input("Ingrese el tipo de plato: Bebida(B) o Plato Fuerte(P): ").upper()

# Calculo del precio de la orden y conteo de tipos de platos
precioOrden = valorUnitario * cantidad
bebidas = 0
platosFuertes = 0

if tipoPlato == "B":
    bebidas = bebidas + cantidad
else:
    platosFuertes = platosFuertes + cantidad

cuentaTotal = precioOrden

# Bucle para agregar mas productos
Continuar = input("Desea agregar otro producto? (S/N): ").upper()

while Continuar == "S":
    producto = input("Ingrese el nombre del producto: ")
    valorUnitario = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))
    tipoPlato = input("Ingrese el tipo de plato: Bebida(B) o Plato Fuerte(P): ").upper()

    precioOrden = valorUnitario * cantidad

    if tipoPlato == "B":
        bebidas = bebidas + cantidad
    else:
        platosFuertes = platosFuertes + cantidad

    cuentaTotal = cuentaTotal + precioOrden

    Continuar = input("Desea agregar otro producto? (S/N): ").upper()

# Calculo del descuento y el IVA
if cuentaTotal >= 20000:
    descuento = cuentaTotal * 0.10
else:
    descuento = 0

subtotalConDescuento = cuentaTotal - descuento
iva = subtotalConDescuento * 0.13
montoConIVA = subtotalConDescuento + iva

# Calculo de propina opcional del 10 %
deseaPropina = input("Desea agregar una propina del 10%? (S/N): ").upper()

if deseaPropina == "S":
    propina = montoConIVA * 0.10
else:
    propina = 0

# Calculo del total a pagar
totalPagar = montoConIVA + propina

# Resumen de la orden
print(f"""
        ===== RESUMEN DE LA ORDEN =====
Bebidas: {bebidas}
Platos Fuertes: {platosFuertes}
Subtotal: ₡{cuentaTotal:.2f}
Descuento: ₡{descuento:.2f}
IVA: ₡{iva:.2f}
Propina: ₡{propina:.2f}
Total a pagar: ₡{totalPagar:.2f}
""")


