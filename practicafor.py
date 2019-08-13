email=False
MiEmail=input("Introduzca una dirección de Email: ")


for i in MiEmail: 

	if (i=="@"): 
		email=True

if email==True: 
	print ("Email correcto")
else: 
	print ("Email no correcto")