import zipfile
import os

print("Demo 11: Comprimir archivos usando la librería zipfile")
directorioOrigen = input("Ingresa directorio con los archivos a comprimir: ")
if(os.path.isdir(directorioOrigen)):
    archivos = os.listdir(directorioOrigen)
    #archivoComprimir = "C:/Users/Ander/Documents/Python Scripts/Clases/Practicas/Archivos/Comprimidos/Comprimidos.zip"
    archivoComprimir = "C:/Users/Ander/Documents/Python Scripts/Clases/Practicas/Archivos/Comprimidos/Comp2.zip"
    zipC = zipfile.ZipFile(archivoComprimir,"w",zipfile.ZIP_DEFLATED)
    for nombre in archivos:
        archivo = os.path.join(directorioOrigen,nombre)
        print("Comprimiendo: ", nombre)
        zipC.write(archivo)
    zipC.close()
    print("Se comprimio: {0}".format(len(archivos)))
    input("Pulsa enter para Descomprimir")
    rutaDescomprimir = "../Archivos/Descomprimidos"
    zipD = zipfile.ZipFile(archivoComprimir,"r",zipfile.ZIP_DEFLATED)
    zipD.extractall(rutaDescomprimir)
    listaComprimida = zipD.namelist()
    #for archivo in listaComprimida:
    #    print("Descomprimiendo ", os.path.basename(archivo))
    zipD.close()
    print("Se descomprimio: {0}".format(len(listaComprimida)))
else:
    print("No existe el Directorio")
