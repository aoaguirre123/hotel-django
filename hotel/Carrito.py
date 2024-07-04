class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            
    def agregar(self, servicio):
        id = str(servicio.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "servicio_id": servicio.id,
                "nombre": servicio.nombre,
                "precio" : float(servicio.precio),
                "acumulado": float(servicio.precio),
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += float(servicio.precio)
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, servicio):
        id = str(servicio.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, servicio):
        id = str(servicio.id)
        if id in self.carrito.keys():
            if self.carrito[id]["cantidad"] > 1:
                self.carrito[id]["cantidad"] -= 1
                self.carrito[id]["acumulado"] -= float(servicio.precio)
            else:
                self.eliminar(servicio)
        self.guardar_carrito()
    
    def limpiar_carrito(self):
        self.session["carrito"] = {}
        self.session.modified = True