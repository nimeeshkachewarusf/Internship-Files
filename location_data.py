from faker import Faker
import pandas as pan
import random
f = Faker()

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