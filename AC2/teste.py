#from "nome arquivo(animais.py)" import "nome classe"


# ------------------------- #
# Testando Classes Mães #
# ------------------------- #

#Reptil
from animais import Reptil
reptil1 = Reptil("NomeReptil", "CorReptil", 3)
print (reptil1.nome, reptil1.cor, reptil1.idade)
print (reptil1.tomar_sol()) 
print (reptil1.botar_ovo()) 

print("")

#Mamifero
from animais import Mamifero
mamifero1 = Mamifero("NomeMamifero", "CorMamifero", 2, "PataMamifero")
print (mamifero1.nome, mamifero1.cor_pelo, mamifero1.idade, mamifero1.tipo_pata)
print (mamifero1.correr()) 
print (mamifero1.mamar())

print("")

# ------------------------- #
# Testando Classes Filhas #
# ------------------------- #

#Camaleao (Reptil)
from animais import Camaleao
camaleao1 = Camaleao("NomeCamaleao", "CorCamaleao", 3, 4)
print (camaleao1.nome, camaleao1.cor, camaleao1.idade, camaleao1.inseto_favorito)
print (camaleao1.mudar_de_cor())
print (camaleao1.comer_inseto())
print (camaleao1.tomar_sol()) #Função da Classe Mãe
print (camaleao1.botar_ovo()) #Função da Classe Mãe

print("")

#Cavalo (Mamifero)
from animais import Cavalo
cavalo1 = Cavalo("NomeCavalo", "CorCavalo", 1, "PataCavalo", "CorCrinaCavalo")
print (cavalo1.nome, cavalo1.cor_pelo, cavalo1.idade, cavalo1.tipo_pata, cavalo1.cor_crina)
print (cavalo1.galopar()) 
print (cavalo1.relinchar())
print (cavalo1.correr()) #Função da Classe Mãe
print (cavalo1.mamar()) #Função da Classe Mãe

print("")

#Cachorro (Mamifero)
from animais import Cachorro
cachorro1 = Cachorro("NomeCachorro", "CorCachorro", 8, "PataCachorro", "RacaCachorro")
print (cachorro1.nome, cachorro1.cor_pelo, cachorro1.idade, cachorro1.tipo_pata, cachorro1.raca)
print (cachorro1.latir())
print (cachorro1.rosnar())
print (cachorro1.correr()) #Função da Classe Mãe
print (cachorro1.mamar()) #Função da Classe Mãe

print("")

##Gato 1 (Mamifero)
from animais import Gato
gato1 = Gato("NomeGato1", "CorGato1", 5, "PataGato1")
print (gato1.nome, gato1.cor_pelo, gato1.idade, gato1.tipo_pata, gato1.vidas)
print (gato1.miar())
print (gato1.morrer())
print (gato1.morrer())
print (gato1.morrer())
print (gato1.morrer())
print (gato1.morrer())
print (gato1.morrer())
print (gato1.morrer())
print (gato1.correr()) #Função da Classe Mãe
print (gato1.mamar()) #Função da Classe Mãe

print("")

##Gato 2 (Mamifero)
gato2 = Gato("NomeGato2", "CorGato2", 1, "PataGato2")
print (gato2.nome, gato2.cor_pelo, gato2.idade, gato2.tipo_pata, gato2.vidas)
print (gato2.miar())
print (gato2.morrer())
print (gato2.morrer())
print (gato2.morrer())
print (gato2.morrer())
print (gato2.morrer())
print (gato2.morrer())
print (gato2.morrer())
print (gato2.correr()) #Função da Classe Mãe
print (gato2.mamar()) #Função da Classe Mãe

print("")

#Cobra (Reptil)
from animais import Cobra
cobra1 = Cobra("NomeCobra", "CorCobra", 2, True)
print (cobra1.nome, cobra1.cor, cobra1.idade, cobra1.veneno)
print (cobra1.rastejar())
print (cobra1.trocar_pele())
print (cobra1.tomar_sol()) #Função da Classe Mãe
print (cobra1.botar_ovo()) #Função da Classe Mãe

print("")

#Jacare (Reptil)
from animais import Jacare
jacare1 = Jacare("NomeJacare", "CorJacare", 2, 10)
print (jacare1.nome, jacare1.cor, jacare1.idade, jacare1.num_dentes)
print (jacare1.atacar())
print (jacare1.dormir())
print (jacare1.tomar_sol()) #Função da Classe Mãe
print (jacare1.botar_ovo()) #Função da Classe Mãe


