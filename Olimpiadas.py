print("Ejercicio # 2")
usuarios=[]
usuarios.append(input("Ingrese un nombre (Ej:camilo):").lower())
usuarios.append(input("Ingrese un nombre (Ej:sara):").lower())
usuarios.append(input("Ingrese un nombre (Ej:luisa):").lower())
dispositivos=[]
dispositivos.append(input("Ingrese un dispositivo (Ej:laptop):").lower())
dispositivos.append(input("Ingrese un dispositivo (Ej:tablet):").lower())
dispositivos.append(input("Ingrese un dispositivo (Ej:smartphone):").lower())

#punto 1
if "luisa" in usuarios[2]:
    usuarios.append("david")
else:
    print(f"{usuarios[2]} no está en la lista no se puede agregar a David")
print(usuarios)
#punto 2
if "smartphone" in dispositivos[2]:
    dispositivos.append("smartwatch")
else:
    print(f"{dispositivos[2]} no está en la lista no se puede agregar a smartwatch")
print(dispositivos)

# punto 3
if "sara" in usuarios[1]:
    usuarios.remove("sara")
else:
    print(f"{usuarios[1]} no está en la lista, no se puede eliminar")
print(usuarios)
#punto 4
elem=len(dispositivos)
if elem>=3:
    dispositivos.remove(dispositivos[0])
else:
    print(f"{dispositivos} tienen menos de 3 elementos")
print(dispositivos)

#punto 5
if "camilo" in usuarios[0]:
    usuarios.remove("camilo")
    usuarios.append("andres")
    usuarios.remove("luisa")
    usuarios.remove("david")
    usuarios.append("luisa")
    usuarios.append("david")
    
else:
    print(f"{usuarios} no está camilo")
print(usuarios)

# #punto 6
soporte_tecnico=[usuarios[0],usuarios[1]]
print(soporte_tecnico)
# #punto 7
dispositivos_moviles=[dispositivos[1],dispositivos[2]]
print(dispositivos_moviles)

# #punto 8
if "smartwatch" in dispositivos_moviles[1]:
    nuevo_dispositivo=("smartwatch","disponible")
else:
    print(f"{dispositivos_moviles[1]} no está disponible")
print(nuevo_dispositivo)
# punto 9
if "andres" in soporte_tecnico[0]:
    soporte_tecnico.append("nivel avanzado")
else:
    print(f"En la lista no se encuentra a {soporte_tecnico[0]}")
# punto 10
if "nivel avanzado" in soporte_tecnico[2]:
    registro_usuario={"nombre":"andres","equipo":"tablet","estado":"activo"}
else:
    print(f"{soporte_tecnico[2]} no está en la lista")
# punto-11
# if registro_usuario in global:
#     {"Ultimo_ingreso":"18/06/2025"}
# else:
#     print("No se encontró la existencia de un diccionario")
# #punto 12
if "impresora" in dispositivos:
     print("Ya está en la lista")
else:
    dispositivos.append("impresora")
print(dispositivos)
 #punto 13
if "sara" in usuarios:
    print("Ya está en la lista")
else:
    usuarios.append("sara")
print(usuarios)

print(dispositivos)

print(soporte_tecnico)

print(dispositivos_moviles)

print(nuevo_dispositivo)

print(registro_usuario)
