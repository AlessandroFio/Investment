import pandas as pd 
import datetime
import yfinance as yf


# info utili

a=input(f'scegli una data, scrivila come aaaa-mm-dd \n')
invest_date=[]
invest_date.append(a)

capital= float(input('how much money you want invest? \n'))


# scariare i dati

sigla=['0P0000I3X4.F']
dfi=yf.download(sigla, period='max')['Close']

df=pd.DataFrame(dfi)
df=df.reset_index()
# df.to_csv('bank_test.csv',index=True)

n_time=int(input('how many month? \n'))
print(f'you choose to start the {a} a capital of {capital} with a PAC with a duration of {n_time} months')
start_df=pd.DataFrame({'date of start':invest_date, 'capital':capital, 'PIC/PAC':n_time, 'price':None , 'n_stocks': None, 'n_tot_stocks':None}, index=['date of start'])
start_df['date of start']=pd.to_datetime(start_df['date of start'], format='%Y-%m-%d')
data=start_df['date of start'].iloc[0]
y=int(1)
n_tot_stocks=float(0)
z=int(0)

for i in range(n_time):
    
    data+= datetime.timedelta(days=15)
        
        
    while not (df.index[(df['Date']== data)] > 0):
        data+= datetime.timedelta(days=1)

    x=len(start_df)+1
    loc_value=df.index[(df['Date']== data)]
    value= capital/n_time 
    price_data=df['Close'].loc[loc_value].item()
    float(price_data)
    n_stock=value/price_data 
    z=loc_value
    opb='buy'
    
    if n_stock >= 0:
        n_tot_stocks =n_tot_stocks + n_stock

    elif n_stock == 'nan':
        n_tot_stocks= n_tot_stocks
    else:
        n_tot_stocks= n_tot_stocks
    start_df.loc[x]=[data, value, opb,price_data, n_stock, n_tot_stocks]
    y+=1            
        
# print(start_df)
stop_p= (capital/n_tot_stocks)*1.05

stop_d=df['Date'].loc[z].item()


today=datetime.date.today()

while stop_d != today:
    
    if df['Close'].loc[z].item() >= stop_p:
    

        a=df['Close'].loc[z].item()
        revenue=a*n_tot_stocks
        profit=revenue-capital
        j=profit/a
        n_tot_stocks -= j

        stop_p= (capital/n_tot_stocks)*1.05
        stop_d=df['Date'].loc[z].item()
    
        ops='sell'

        start_df.loc[(len(start_df)+1)]=[stop_d, profit, ops, a, j, n_tot_stocks]

        z +=1
    else:
        None
        z +=1
    
    if z >= len(df):
        break

start_df.to_csv('0P0000I3X4.F.c.csv', index=False)

print(start_df)
print('finish') 

# 2000-03-22
# 2020-08-04 5000 0P0000I3X4.F