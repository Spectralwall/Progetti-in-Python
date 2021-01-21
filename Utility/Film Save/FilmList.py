#Script allo scopo di avere una lista di film con voto salvata su dispositivo, che verra richiamata in ordine di voto

def spezza(frase):



    None

class filmClass:
    def __init__(self,voto,nome):#costruttore della classe film
        self.votoC = voto
        self.nomeC = nome

    def __repr__(self):
        return self.writeFilm()

    def __str__(self):
        return self.writeFilm()

    def writeFilm(self):
        return self.nomeC +","+ self.votoC

print("Che operazione vuoi svolgere ?")
print("1) inserire un nuovo film ?")
print("2) vedere la lista dei film")
print("3) terminare l'app")

while(True):
    scelta = input()
    if(scelta == "1"):
        nome = input("Come si chiama il film : ")
        voto = input("Che voto gli dai : ")
        film = filmClass(voto,nome)#prendo i dati e creo un oggetto film

        #scrittura su file
        writer = open("Film","a")
        writer.write("\n" + film.writeFilm())
        writer.close()

        print("vuoi fare qualcos'altro ?")
    elif(scelta == "2"):
        Films = []#lista dei film
        reader = open("Film","r")#leggo da file
        l = reader.readlines()
        for x in l:
            nome,voto = x.split(",")
            f = filmClass(voto,nome)
            Films.append(f)

        Films.sort(key=lambda x: x.votoC)#ordino per voto
        for x in Films:
            print(x)

        print("vuoi fare qualcos'altro ?")
    elif(scelta == "3"):
        print("Goodbye")
        break
    else:
        print("scelta non riconosciuta")
None
