import pandas as pd

# Read the CSV file
data = pd.read_csv('NSE_data.csv')

for x in range(data.shape[0]):
  
    row=str(x)
    if( data.iloc[x, data.columns.get_loc('Code')]=='KURV'):
        for y in ["12m Low","12m High","Day Low","Day High","Day Price","Previous"]:
            value= data.iloc[x, data.columns.get_loc(y)]
            data.iloc[x, data.columns.get_loc(y)]=float(value.replace(',',''))
    if( data.iloc[x, data.columns.get_loc('Code')]=='GLD'):
       for y in ["12m Low","12m High","Day Low","Day High","Day Price","Previous"]:
           value= data.iloc[x, data.columns.get_loc(y)]
           data.iloc[x, data.columns.get_loc(y)]=float(value.replace(',',''))


    if( data.iloc[x, data.columns.get_loc('Change')]=='-'):
         data.iloc[x, data.columns.get_loc('Change')]='0'

    if( data.iloc[x, data.columns.get_loc('Change%')]=='-'):
         data.iloc[x, data.columns.get_loc('Change%')]='0'
    
    if (data.iloc[x, data.columns.get_loc('Volume')]=="-"):
        data.iloc[x, data.columns.get_loc('Volume')]='0'
    
    if (data.iloc[x, data.columns.get_loc('Adjusted Price')]=="-"):
        data.iloc[x, data.columns.get_loc('Adjusted Price')]='0'
        
    else:
        value= data.iloc[x, data.columns.get_loc('Volume')]
        data.iloc[x, data.columns.get_loc('Volume')]=float(value.replace(',',''))
       
# Write the modified data to a new CSV file
data.to_csv('clean_data.csv', index=False)