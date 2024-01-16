import pandas as pd
from pyswip import Prolog

def writefile(fileName: str, mod: str):
    prolog = Prolog()
    prolog.consult(f"./Dataset/rules.pl")
    prolog.consult(f"./Dataset/kb.pl")

    with open(fileName,mod) as file:
        print("scrivendo file...")
        
        file.write('-' * 50 + '\n')  
        file.write("I seguenti pc hanno un peso basso:\n")
        for result in prolog.query("pcLeggero(ID, Peso)"):
            file.write(f"pcID: {result['ID']}, peso: {result['Peso']} kg\n")
        
        file.write('-' * 50 + '\n')   
        file.write("I seguenti pc hanno Prezzo inferiore a 300 euro:\n")
        for result in prolog.query("pcEconomico(ID, Prezzo)"):
            file.write(f"pcID: {result['ID']}, prezzo: {result['Prezzo']} euro\n")
            
        file.write('-' * 50 + '\n')
        for result in prolog.query("perc_4k(Perc)"):
            file.write("percentuale di pc 4k: {:.2f} % \n".format(result['Perc']))
        
        file.write('-' * 50 + '\n')
        for result in prolog.query("max_Price(Prezzo)"):
            file.write(f"costo pc maggiore: {result['Prezzo']} euro \n")

        file.write('-' * 50 + '\n')
        for result in prolog.query("min_Price(Prezzo)"):
            file.write(f"costo pc minore: {result['Prezzo']} euro \n")
            
        file.write('-' * 50 + '\n')
        for result in prolog.query("pc_apple_schermo_piu_piccolo(ID, MinDimensioni)"):
            file.write(f"Pc Apple con schermo piu' piccolo: ID:{result['ID']}, {result['MinDimensioni']} pollici \n")
        
        file.write('-' * 50 + '\n')
        for result in prolog.query("perc_ultrabook(Perc)"):
            file.write("percentuale di Ultrabook presente: {:.2f} % \n".format(result['Perc']))
        
        file.write('-' * 50 + '\n')
        for result in prolog.query("count_lenovo(Num)"):
            file.write(f"numero prodotti lenovo: {result['Num']} \n")
            
        file.write('-' * 50 + '\n')
        for result in prolog.query("pcApple_MacOSX(ID)"):
            file.write(f"pc Apple con MacOSX: {result['ID']} \n")
        
        print("fine.")

writefile('./Dataset/output.txt','w')
