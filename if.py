print ("Asignaturas optativas 2019")
print ("Asignaturas optativas: Informatica - Cine y video - Artes performáticas")

Opcion=input ("Escribe la asignatura escogida: ")

Asignatura=Opcion.lower()

if Asignatura in ("informatica", "cine y video", "artes performáticas"): 
	print ("Asignatura elegida: " + Asignatura)

else: 
	print ("La asignatura escogida no está contemplada")