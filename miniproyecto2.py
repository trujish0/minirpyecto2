#Nombres
nombres_jugadores= input("Ingresa los nombres de los jugadores separados por un espacio: " )
lista_jugadores= nombres_jugadores.split()

jugador1= lista_jugadores[0] [0:3] .upper ()
jugador2= lista_jugadores[1] [0:3] .upper ()

if jugador1== jugador2:
   jugador2= jugador2+"2"

#Puntajes
puntaje_inicial1= [501,0,0,0]   
puntaje_inicial2= [501,0,0,0]

print(jugador1 + " " + str(puntaje_inicial1[0]))
print(jugador2 + " " + str(puntaje_inicial1[0]))

#Errores
error=0

#Ciclo Juego
while puntaje_inicial1[0] != 0 and puntaje_inicial2[0] != 0:

    print("Ingresen sus 3 jugadas realizadas: SINGLE BULL, DOUBLE BULL, NULL o multiplicador más puntaje.")
    
    for i in range (1,4):
        jugada= input() .upper ()

        if jugada == "SINGLE BULL":
            jugada=25
                   
        elif jugada == "DOUBLE BULL":
            jugada=50
            
        elif jugada == "NULL":
            jugada=0

        else:
            lista_jugada=jugada.split()
            if int(lista_jugada[0])<1 or int(lista_jugada[0])>3 or int(lista_jugada [1]) > 20:
                error = 1

            jugada=int(lista_jugada[0]) * int(lista_jugada [1])
    
        puntaje_inicial1[i]=jugada

    puntaje_inicial1[0]= (puntaje_inicial1[0]-(puntaje_inicial1[1] + puntaje_inicial1[2] + puntaje_inicial1[3]))
    if puntaje_inicial1[0] < 0:
        puntaje_inicial1[0]=abs(puntaje_inicial1[0])
    
    for i in range (1,4):
        jugada= input() .upper ()

        if jugada == "SINGLE BULL":
            jugada=25
              
        elif jugada == "DOUBLE BULL":
            jugada=50
            
        elif jugada == "NULL":
            jugada=0

        else:
            lista_jugada=jugada.split()
            if int(lista_jugada[0])<1 or int(lista_jugada[0])>3 or int(lista_jugada [1]) > 20:
                error = 1 

            jugada=int(lista_jugada[0]) * int(lista_jugada [1])
            
        
        puntaje_inicial2[i] = jugada

    puntaje_inicial2[0]= puntaje_inicial2[0]-(puntaje_inicial2[1] + puntaje_inicial2[2] + puntaje_inicial2[3])
    if puntaje_inicial2[0] < 0:
        puntaje_inicial2[0]=abs(puntaje_inicial2[0])

    print((jugador1) + " " + str(puntaje_inicial1[0]))
    print((jugador2) + " " + str(puntaje_inicial2[0]))

    if error == 1:
        print ("Datos erroneos, el programa se cerrará.")
        break

    if puntaje_inicial1[0] == 0: 
        print("¡Felicitaciones " + lista_jugadores[0] + " eres el ganador!")

    elif puntaje_inicial2[0] == 0:
        print("¡Felicitaciones " + lista_jugadores[1] + " eres el ganador!")

    elif puntaje_inicial1[0]==0 and puntaje_inicial2[0]==0:
        print("Empate!")
   
