def ejercicio_1(dni):

    #Diccionario de numeeros
    ltrs = {
        '0': 'Cero',
        '1': 'Uno',
        '2': 'Dos',
        '3': 'Tres',
        '4': 'Cuatro',
        '5': 'Cinco',
        '6': 'Seis',
        '7': 'Siete',
        '8': 'Ocho',
        '9': 'Nueve'
    }
    
    #Cantidad total de numeros 
    Tt = []
    
    #Validacion
    if dni.isdigit() and len(dni) == 8:
        
        #Hace Iteraciones
        for dgt in dni:
        
            #coge las palabras para el numero del diccionario
            ltr = ltrs[dgt]
            Tt.append(ltr)

        #Espacio entre palabra
        ltr = " ".join(Tt)
        return ltr 
    else:
        return "DNI inválido."

while True:
    dni = input("Ingresa un DNI (8 dígitos): ")

    #Llama funcion y guarda
    ltr = ejercicio_1(dni)

    print(ltr)


    rspst = input("¿Deseas continuar? (si/no): ")
    if rspst.lower() == "no":
        print("Usted saldrá del programa.")
        break