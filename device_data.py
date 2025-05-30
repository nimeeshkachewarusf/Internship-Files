import random
from faker import Faker
import pandas as pan
f = Faker()

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

    



