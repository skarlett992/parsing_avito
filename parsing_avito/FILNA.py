from features_from_response import df
from metro_code_avito import codes
import pandas as pd

df['metro']
codes[0]
list_metro = df['metro'].to_dict()
# def metro_id(list_metro):
metro_id = []
for key, value in list_metro.items():
        for i in codes:
            if value == i['name']:
                key = i['id']
                metro_id.append(key)

# metro_id = metro_id(list_metro)
df['metro_id'] =  pd.DataFrame(metro_id)
#заполнение нолей в станциях
df.loc[df['station_3'].isnull(), 'station_3'] = df['metro_id']
df.loc[df['station_2'].isnull(), 'station_2'] = df['metro_id']
df.loc[df['station_1'].isnull(), 'station_1'] = df['metro_id']

