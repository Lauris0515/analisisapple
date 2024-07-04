import random

def generarDatosProductos():
    productos=["Musica","TV","Aplicaciones","PC","Celulares","Tablets","Accesorios"]
    datos=[]    
    for producto in productos: 
        categoria=random.choice(["Plus","Mega","Basic"])
        
        productoarreglo=[producto,categoria]
        datos.append(productoarreglo)        
    return datos    
    