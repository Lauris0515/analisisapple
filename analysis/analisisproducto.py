from generators.generadoproductos import generarDatosProductos
import pandas as pd

def analizarDatos():
    datos=generarDatosProductos()
    tabla=pd.DataFrame(datos,columns=["Tipo Producto","categoria"])
    tabla.to_csv("./data/tablaproductos.csv",index=False)
analizarDatos()