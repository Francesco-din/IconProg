import pandas as pd

def create_kb(path: str, name: str):
    print("Reading data...")
    df = pd.read_csv('./filecsv/newLaptopPrice.csv', low_memory = False)
    prolog_file = open(path + name, "w")
    print(f"Creating knowledge base at {path + name}...")
    prolog_file.write(":-style_check(-discontiguous).\n")
    print("Writing facts...")

    for index, row in df.iterrows():
        prolog_file.write(f"prop({row['laptop_ID']},'larghezza Risoluzione',{row['ScreenResolution'].split('x')[0]}).\n")
        prolog_file.write(f"prop({row['laptop_ID']},'altezza Risoluzione',{row['ScreenResolution'].split('x')[1]}).\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Modello', '{row['Product']}').\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Marca', '{row['Company']}').\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Dimensioni schermo', {row['Inches']}).\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Cpu', '{row['Cpu']}').\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Ram', '{row['Ram']}').\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Memoria', '{row['Memory']}').\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Sistema Operativo', {row['OpSys']}).\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Peso', {row['Weight']}).\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Prezzo (euro)', {row['Price_euros']}).\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'Touchscreen', {row['TouchScreen']}).\n")
        prolog_file.write(f"prop({row['laptop_ID']}, 'tipo', '{row['TypeName']}').\n")        

    prolog_file.close()
    print("Knowledge base created!")

create_kb("./Dataset/", "kb.pl")