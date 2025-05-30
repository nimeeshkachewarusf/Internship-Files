from faker import Faker
import pandas as pan
f = Faker()

client_data = []
for i in range(1,101):
    company = f.company().replace('-',' ').replace('Inc','').replace('Ltd','').replace('PLC','').replace('LLC','')
    
    collection = {'CustomerId' : 'C' + str(i),
           'Name' : company + ' Inc',
           'Email' : 'contact@' + company.replace(' ', '').replace(',','').lower() + '.com',
           'Phone' : '+1 ' + f.bothify('### ### ####')}
    
    client_data.append(collection)



data_frame1 = pan.DataFrame(client_data)
data_frame1.to_excel('client_data5.ods', engine = 'odf', index=False)
