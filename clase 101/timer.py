import time

def contador(seconds):
    #Es un ciclo que se repite mientras se cumpla la condicion
    while seconds > 0:
       mins=int(seconds/60)
       secs=int(seconds%60)
       #eEs una cadena formateada
       timer=f'{mins}:{secs}'
       print(timer,end='\r')
       #sleep sirve para hacer una pausa antes del siguiente valor
       time.sleep(1)
       seconds -= 1
    print("se acabo el tiempo")

seconds=input("Ingresa los segundos: ")

contador(int(seconds))
