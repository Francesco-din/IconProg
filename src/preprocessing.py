import pandas as pd
from utils import *


mappa_op_sys = {}
def assegna_valore_numerico(stringa):
        if stringa not in mappa_op_sys:
            mappa_op_sys[stringa] = max(mappa_op_sys.values(), default=0) + 1
        return mappa_op_sys[stringa]

def preprocessing():
    df=pd.read_csv('./filecsv/laptop_price.csv')
    #print(df)
    print('preprocessing dataset...')
    
    #pulizia collone
    carattere= '('
    df['Product'] = df['Product'].str.replace(f'\\s* \\{carattere}.*', '', regex=True)
    df['Product'] = df['Product'].str.replace('"', '')
    
    df['Weight'] = df['Weight'].str.replace('kg', '')
    df['Ram'] = df['Ram'].str.replace('GB', '')
    
    df['Price_euros'] = df['Price_euros'].str.replace(r'\.(\d{2})\.\d{2}', r'.\1', regex=True)
    
    #crea la colonna TouchScreen e pone il valore a 1 se è touchscreen, a 0 se non lo è
    df['TouchScreen'] = df['ScreenResolution'].str.contains('Touchscreen', case=False, regex=True).astype(int)
    
    df['ScreenResolution'] = df['ScreenResolution'].str.replace(r'[^0-9x.]|\.(?![0-9])', '', regex=True)
    df['ScreenResolution'] = df['ScreenResolution'].str.replace(r'^4', '', regex=True)

    # Applica la funzione di assegnazione di valori numerici alla colonna 'OpSys'
    df['OpSys'] = df['OpSys'].apply(assegna_valore_numerico)
    
    return df
a = preprocessing()
print("Saving preprocessed data...")

percorso_nuovo_file = './filecsv/newLaptopPrice.csv'
a.to_csv(percorso_nuovo_file, index=False)
print("Preprocessed data saved!")