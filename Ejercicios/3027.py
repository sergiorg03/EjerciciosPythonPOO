'''

    Ejercicio 3027

'''

class CarritoCompra:

    def __init__(self):

        self. articulos_cantidad = {} # {articulo: cantidad} 

        self.articulos_precio = {} # {articulo: precio}


    def agregar_articulo(self, articulo, precio, cantidad):
        if articulo in self.articulos_cantidad:

            self.articulos_cantidad[articulo] += cantidad
        else:

            self.articulos_cantidad[articulo] = cantidad

            self.articulos_precio[articulo] = precio
    

    def eliminar_articulo(self, articulo):
        if articulo in self.articulos_cantidad:

            self.articulos_cantidad.pop(articulo, None) # Devolvemos None si el artículo no existe

            self.articulos_precio.pop(articulo, None) # Devolvemos None si el artículo no existe
        else:

            print("El artículo indicado no existe. ")

    def precio_total(self):

        return sum(self.articulos_precio[i] * self.articulos_cantidad[i] for i in self.articulos_cantidad)

    def listar_articulos(self):

        return list(self.articulos_cantidad.keys())
    
    def listar_carrito(self):

        return [(i, self.articulos_precio[i], self.articulos_cantidad[i]) for i in self.articulos_cantidad]


    def costo_total_articulo(self,articulo):
        if articulo in self.articulos_cantidad:

            return self.articulos_cantidad[articulo] * self.articulos_precio[articulo]
        else:

            print("El artículo introducido no existe. ")

            return 0


    def obtener_cantidad(self, articulo):

        return self.articulos_cantidad.get(articulo, 0)
    
    def contar_articulos_distintos(self):
        return len(self.articulos_cantidad)

    def __str__(self):
        carrito = "Carrito de compra:\n"

        for a, precio, cantidad in self.listar_carrito():
            carrito += f"- {a}: {cantidad} unidades x {precio:.2f} € = {precio*cantidad:.2f} €\n"
        carrito += f"Precio total: {self.precio_total():.2f} €"
        return carrito

## pruebas / casos de uso
carrito1 = CarritoCompra()
print("Listar carrito: ",carrito1.listar_carrito())
print("- "*20)
print("Agregamos 2 articulos")
carrito1.agregar_articulo(articulo="zumo naranja", cantidad=2, precio=4)
carrito1.agregar_articulo(articulo="pan", cantidad=1.5, precio=3)
carrito1.agregar_articulo(articulo="manzana", cantidad=2, precio=5)
print("Listar carrito: ",carrito1.listar_carrito())
print("- "*20)
print("La cantidad de zumo naranja seleccionado es:",carrito1.obtener_cantidad("zumo naranja"))

print("El costo total del pan:",carrito1.costo_total_articulo("pan"))
print("- "*20)
print("Eliminamos el pan del carrito")
carrito1.eliminar_articulo("pan")
print("Listar carrito: ",carrito1.listar_carrito())
print("- "*20)
print("El número de artículos distintos en el carrito:",carrito1.contar_articulos_distintos())
print("Estado del carrito:")
print(carrito1)
