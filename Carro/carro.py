class Carro:
    def __init__(self,request) :
      self.request = request 
      self.session = request.session
      carro = self.session.get('carro')
      if not carro :
         carro = self.session['carro'] = {}
      
      self.carro = carro
    
    def agrega(self,producto):
        if str(producto.id) not in self.carro.keys():
           self.carro[str(producto.id)] = {
              "producto_id":producto.id,
              "nombre":producto.nombre,
              "precio":str(producto.precio),
              "cantidad": 1,
              "imagen":producto.imagen.url
           }
        else:
           for key,value in self.carro.items():
              if key == str(producto.id):
                value['cantidad']+=1
                value['precio'] = float(value['precio']) + producto.precio
                break

        self.guarda_carro()

    def guarda_carro(self):
       self.session['carro'] = self.carro
       self.session.modified = True
    
    def elimina(self,producto):
       producto_id = str(producto.id)
       if producto_id in self.carro:
          del self.carro[producto_id]
          self.guarda_carro()
    
    def resta_producto(self,producto):
        for key,value in self.carro.items():
              if key == str(producto.id):
                value['cantidad']-=1
                value['precio'] = float(value['precio']) - producto.precio
                if value['cantidad']<1:
                   self.elimina(producto)
                break
        self.guarda_carro()
    
    def limpia_carro(self):
       self.session['carro'] = {}
       self.session.modified = True