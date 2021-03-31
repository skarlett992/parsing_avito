import pandas as pd
from metro_code_avito import codes
import json

data = pd.read_csv("./rooms_df.csv")

#фрейм с широтой и долготой станций метро
df_metro_lat_lng = pd.read_csv("./GPS_code_metro.csv",  delimiter = '\t', names=['name','lat_metro','lng_metro'])
#некоторые станции обозначены нестандартно, исправим
df_metro_lat_lng['name'] = df_metro_lat_lng['name'].apply(lambda x: x[:-7] if x[-6:] == '(стр.)' else x)

# словарь с кодами метро - приводим к фрему и делаем мердж с широтой и долготой
metro_codes = pd.DataFrame.from_dict(codes)
metro_data = pd.merge(df_metro_lat_lng, metro_codes, how='inner', on="name")
df = pd.merge(data, metro_data, how='inner', on="name")
