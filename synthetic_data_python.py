# ------- Client Data ---------------------------------------------
from faker import Faker
import pandas as pan
import random
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

# --------------------------- Client Data script ends------------------------------------------


# ---------------------------Device Data ------------------------------------------------------


device_data = []

for i in range(1,25001):
    unformatted_start_date = f.date_between(start_date = '-5y', end_date = '-1y')
    formatted_start_date = unformatted_start_date.strftime('%#d-%b-%y')

    unformatted_end_date = f.date_between(start_date = unformatted_start_date, end_date = 'today')
    formatted_end_date = unformatted_end_date.strftime('%#d-%b-%y')

    collection2 = {'DeviceId': 'Device' + str(i),
                  'Device Owner Name' : f.name(),
                  'Start Date' : formatted_start_date,
                  'End Date' : formatted_end_date,
                  'Client Id' : 'C' + str(random.randint(1,100))
                  }
    
    device_data.append(collection2)


data_frame2 = pan.DataFrame(device_data)
data_frame2.to_excel('device_data3.ods', engine = 'odf', index=False)

# --------------------- Device Data Script Ends ------------------------------------------



#--------------------- Location Data -----------------------------------------------------

location_data = []
con = 1

for i in range(1,25000):

    raw_time = f.date_time()
    year_range = f.date_between(start_date='-4y',end_date='today')
    new_time = raw_time.strftime(f'{raw_time.month}/{raw_time.day}/{year_range.year} {raw_time.hour}:{raw_time.minute}')
    
    latitude_initial = float(f.latitude())
    longitude_initial = float(f.longitude())

    for j in range(7):

        random1 = float(random.uniform(-0.0008,0.0065))
        random2 = float(random.uniform(-0.0008,0.0065))
        latitude_initial += random1
        longitude_initial += random2


        collection3 = {'Id' : con,
                    'DateTime' : new_time,
                    'DeviceId': f'Device{i}',
                    'Latitute' : f'{latitude_initial:.6f}',
                    'Longitude' : f'{longitude_initial:.6f}'}
        
        con += 1
        location_data.append(collection3)

data_frame3 = pan.DataFrame(location_data)
data_frame3.to_excel('location_data_final.ods', engine = 'odf', index=False)

# --------- Location Data Script Ends -----------------------------------------


