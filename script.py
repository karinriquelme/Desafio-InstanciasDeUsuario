import json
from usuario import Usuario
from datetime import datetime
import os

lista=[]



try:
    with open("usuarios.txt") as usuarios:
        # linea = usuarios.readline()
        for linea in usuarios:
            try:
                usuario=json.loads(linea)
                nuevo_usuario=Usuario(usuario["nombre"], usuario["apellido"],usuario["email"],usuario["genero"])
                lista.append(nuevo_usuario)
            except Exception as e:
                fecha_hora=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                texto_error=str(e)
                linea_error=f"{fecha_hora}- error detectado!!!: {texto_error}\n"
                with open ("error.log","a+") as log:
                    log.write(linea_error)
                    log.close
    os.system("cls") if os.name=="nt" else os.system("clear")  
    for persona in lista:
        print(persona)
    
        
        
except FileNotFoundError:
    print("no se ha encontrado el archivo")