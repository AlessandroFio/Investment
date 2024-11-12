import pandas as pd 
import numpy as np
import datetime
import yfinance as yf

# DATI
# Data di inizio
a=input(f'scegli una data, scrivila come aaaa-mm-dd \n')
invest_date=[]
invest_date.append(a)

# Capitale
capital= float(input('how much money you want invest? \n'))

# Numero di rate
n_time=int(input('how many rate? \n'))
k=input('inserisci il codice \n')
# Variabile di ogni rata
value= capital/n_time 

# scariare i dati
sigla=[k]
dfi=yf.download(sigla, period='max')['Close']

# Creare un data frame con i dati scaricati
df=pd.DataFrame(dfi)
df=df.reset_index()
#df.to_csv('0P0000TJBE.F.s.csv',index=True)

# Creare un secondo data frame dove contenere i risultati
dati={'date of start':invest_date, 'capital':capital, 'PIC':n_time, 'price':None , 'n_stocks': None, 'n_tot_stocks':None}
start_df=pd.DataFrame(dati, columns=['date of start','capital','PIC', 'price', 'n_stocks', 'n_tot_stocks'])
start_df['date of start']=pd.to_datetime(start_df['date of start'], format='%Y-%m-%d')

# VARIABILI 
# Indice riga df
z=int(0)

# Data di inizio
data=start_df['date of start'].iloc[0]

# Numero totale delle azioni
n_tot_stocks=float(0)

# CREARE IL CICLO
# for z in range(len(df)):

while z <= len(df):

    # Ciclo per gli ACQUISTI
    for i in range(n_time):
        
        #Identifico le date di acquisto
        data+= datetime.timedelta(days=15)
        
        #chiusura ciclo
        today=datetime.datetime.today()
        if data >= today:
            break
        else:
            
        # Ciclo nel caso in cui la data di acquisto non fosse valida (sabato, domenica o festivi) 
        # ?? si può migliorare (come??) ??
            while not (df.index[(df['Date']== data)] > 0):
                data+= datetime.timedelta(days=1)

        # Ricerco il valore dell'indice nel df
            loc_value=df.index[(df['Date']== data)]
        
        # Prezzo riferito al giorno 
            price_data=df['Close'].loc[loc_value].item()

        # Numero di azioni acquistate
            n_stock=value/price_data 

        # Il nuovo indice di riga df
            z=loc_value
    
        # Tipologia di operazione
            opb='buy'

        # Conteggio delle azioni totali
            if n_stock >= 0:
                n_tot_stocks =n_tot_stocks + n_stock

            elif n_stock == 'nan':
                n_tot_stocks= n_tot_stocks
            else:
                n_tot_stocks= n_tot_stocks

        # Variabile per la posizione, e scrittura nel start_df
        x=len(start_df)+1
        start_df.loc[x]=[data, value, opb, price_data, n_stock, n_tot_stocks]
        
               
    # Verifica correzione, si può eliminare    
    print(start_df)
    
    if data >= today:
            break
    elif z > len(df):
        break
    else:
        None

    

    # Ciclo per le VENDITE
    #Variabile stop price
    stop_p= (capital/n_tot_stocks)*1.05
    
       
    while not df['Close'].loc[z].item() >= stop_p:
        if z == (len(df)-1):
            break
        else:
            z+=1

    if z == (len(df)-1):
            break
    else:
        a=df['Close'].loc[z].item()
        stop_d=df['Date'].loc[z].item()
        revenue=a*n_tot_stocks
        profit=revenue-capital
        n_stock=n_tot_stocks
        n_tot_stocks = 0

        ops='sell'

        x=len(start_df)+1       
        start_df.loc[x]=[stop_d, revenue, ops, a, n_stock, n_tot_stocks]
        data =stop_d
    
        
    print(start_df)

start_df.to_csv('0P0000VOE8.F.csv', index=False)

# print(start_df)
print('finish') 

# 2000-03-22
# 2021-09-07 5005.5 0P00000G0K.F
# 2020-08-04 4994.88 0P0000TJBE.F
# 2022-10-07 20000 0P0000TJBE.F
# 2020-08-04 5000 0P00011WON.F
# 2020-08-04 5000 0P0000VQH1.F
# 2020-08-04 5000 0P0000VOE8.F
# 2020-08-04 5000
# 2020-08-04 5000
# 2020-08-04 5000