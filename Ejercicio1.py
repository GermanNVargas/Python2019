Num1=(int(input("Introduce el primer numero: ")))

Num2=(int(input("Introduce el segundo numero: ")))

def DevuelveMax (n1, n2): 
	if n1 < n2:
		print (n2)
	elif n2 < n1:
		print (n1)
	else: 
		print ("Son Iguales")

print ("El numero mas alto es: ")

DevuelveMax(Num1, Num2)

