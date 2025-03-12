import sys
if __name__ == '__main__':
    sys.stdout.write("Proporciona un numero del dia de la semana")
num=int(input())
semana=""
match num:
    case 1:semana="lunes"
    case 2:semana="martes"
    case 3:semana="miercoles"
    case 4: semana= "jueves"
    case 5: semana= "viernes"
    case 6: semana = "sabado"
    case 7: semana = "domingo"
    case _:semana ="numero no valido"

if num>=1 and num <=7:
    sys.stdout.write(f"el dia de la semana indicado es {semana}")
else:
    sys.stdout.write(f"{semana}")

