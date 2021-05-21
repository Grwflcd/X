import pandas as pd

#常量
Morning_start=1479168000
Morning_end=1479168600
Noon_start=1479182400
Noon_end=1479183000
Afternoon_start=1479200400
Afternoon_end=1479201000

Longitude_min=108.92909
Longitude_max=108.96209
Latitude_min=34.214946
Latitude_max=34.241936



df=pd.read_csv("gps_20161115",names=['vehicle_id','order_number','time','longitude','latitude'])
data=df[(df['longitude'] > Longitude_min) & (df['longitude'] < Longitude_max) & (df['latitude']>Latitude_min) &(df['latitude'] < Latitude_max)]#lacaltion
data2=data[( (data['time']>Morning_start) & (data['time']<Morning_end)) | ((data['time']>Noon_start)&(data['time']<Noon_end)) | ((data['time']>Afternoon_start)&(data['time']<Afternoon_end))]
data.to_csv('step1.csv')
data2.to_csv('step2.csv')
print(data.tail().to_string())