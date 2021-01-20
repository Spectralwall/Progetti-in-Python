#Script allo scopo di avere una lista di film con voto salvata su dispositivo, che verra richiamata in ordine di voto

def spezza(frase):



    None

class filmClass:
    def __init__(self):#costruttore della classe film
        self.votoC = voto
        self.nomeC = nome

    def writeFilm(self):
        return self.nomeC +" ,"+ self.votoC

print("Che operazione vuoi svolgere ?")
print("1) inserire un nuovo film ?")
print("2) vedere la lista dei film")
scelta = input()

if(scelta == "1"):
    nome = input("Come si chiama il film : ")
    voto = input("Che voto gli dai : ")
    film = filmClass()#prendo i dati e creo un oggetto film

    #scrittura su file
    writer = open("Film","a")#file dove scriver e tipo di scrittura(a append to file , w overwrite file)
    writer.write(film.writeFilm())
    writer.close()
    None
elif(scelta == "2"):
    Films = []#lista dei film
    reader = open("Film","r")#leggo da file
    l = reader.readlines()
    for x in l:

    None
else:
    print("scelta non riconosciuta")
