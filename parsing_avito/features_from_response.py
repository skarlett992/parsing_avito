import pandas as pd
import json
import re

# regex = re.compile('\s+')

with open('rooms_file.json', 'r') as file:
    rooms = json.load(file)
    response = json.loads(rooms)


itemId = []
url = []
commission = []
address = []
area = []
rooms_count = []
floor = []
floors_count = []
house_type = []
metro_distance = []
price = []
lat = []
lng = []
ext = []
geo = []
coords = []
colors = []
colors1 = []
colors2 = []
metro_distance_1 = []
metro_distance_2 = []
metro_distance_3 = []
station_1 = []
station_2 = []
station_3 = []
metro = []
remove_features = ['images', 'hasVideo', 'bezopasnyi_prosmotr', 'paramsMap',
                               'time', 'title', 'priceFormatted', 'category',
                               'location', 'imagesCount', 'type', 'favorite']
dict = {'itemId': itemId, 'commission': commission, 'room_area, m2': area,
        'rooms_count': rooms_count, 'floor': floor, 'floors_count': floors_count,
        'house_type': house_type, 'lat':lat, 'lng': lng,
        'colors': colors, 'url': url, 'metro_distance': metro_distance,
        'station_1': station_1, 'station_2': station_2, 'station_3': station_3,
        'metro_distance_1': metro_distance_1, 'metro_distance_2': metro_distance_2,
        'metro_distance_3': metro_distance_3, 'name': metro, 'address': address, 'price, rub': price}
for i, feature in enumerate(response):
    for key, value in response[i].items():
        if key not in remove_features:
            if key == 'itemId':
                itemId.append(value)
            if key == 'price':
                price.append(value)
            if key == 'url':
                url.append(value)
            if key == 'ext':
                ext.append(value)
                # print(value, type(value))
                if 'metro_distance' not in value:
                    metro_distance.append(None)
                    station_1.append(None)
                    metro_distance_1.append(None)
                    station_2.append(None)
                    metro_distance_2.append(None)
                    station_3.append(None)
                    metro_distance_3.append(None)

                else:
                    for k, v in value.items():
                        if k == 'metro_distance':
                            key_list = list(v.keys())
                            value_list = list(v.values())
                            print(key_list, value_list)
                            # for i in key_list:
                                # print(key_list[0], key_list[1], key_list[2])
                            if len(key_list) == 3:
                                station_1.append(key_list[0])
                                metro_distance_1.append(value_list[0])
                                station_2.append(key_list[1])
                                print(value_list[1])
                                metro_distance_2.append(value_list[1])
                                station_3.append(key_list[2])
                                metro_distance_3.append(value_list[2])
                            elif len(key_list) == 2:
                                station_1.append(key_list[0])
                                metro_distance_1.append(value_list[0])
                                station_2.append(key_list[1])
                                metro_distance_2.append(value_list[1])
                                station_3.append(None)
                                metro_distance_3.append(None)
                            # print(station_3)
                            elif len(key_list) == 1:
                                station_1.append(key_list[0])
                                metro_distance_1.append(value_list[0])
                                station_2.append(None)
                                metro_distance_2.append(None)
                                station_3.append(None)
                                metro_distance_3.append(None)
                            metro_distance.append(v)
                if 'commission' not in value:
                    commission.append(None)
                else:
                    for k, v in value.items():
                        if k == 'commission':
                            commission.append(v)

                if 'address' not in value:
                    address.append(None)
                else:
                    for k, v in value.items():
                        if k == 'address':
                            address.append(v)

                if 'area' not in value:
                    area.append(None)
                else:
                    for k, v in value.items():
                        if k == 'area':
                            area.append(v[:-3])
                if 'rooms' not in value:
                    rooms_count.append(None)
                else:
                    for k, v in value.items():
                        if k == 'rooms':
                            rooms_count.append(v)
                if 'floor' not in value:
                    floor.append(None)
                else:
                    for k, v in value.items():
                        if k == 'floor':
                            floor.append(v)
                if 'floors_count' not in value:
                    floors_count.append(None)
                else:
                    for k, v in value.items():
                        if k == 'floors_count':
                            floors_count.append(v)
                if 'house_type' not in value:
                    house_type.append(None)
                else:
                    for k, v in value.items():
                        if k == 'house_type':
                            house_type.append(v)

            if key == 'coords':
                coords.append(value)
                # print(value, type(value))
                if 'lat' not in value:
                    lat.append(None)

                else:
                    for k, v in value.items():
                        if k == 'lat':
                            lat.append(v)
                if 'lng' not in value:
                    lng.append(None)
                else:
                    for k, v in value.items():
                        if k == 'lng':
                            lng.append(v)


            if key == 'geo':
                geo.append(value)
                if 'geoReferences' not in value:
                    # print(value)
                    metro.append(None)
                    colors1.append(None)
                    colors2.append(None)
                else:
                    for k, v in value.items():
                        if type(v[0]) == type(dict):
                            if 'content' not in v[0].keys():
                                # print(v[0].keys(), v[0].values())
                                metro.append(None)
                            else:
                                metro.append(v[0]['content'])
                            if 'colors' not in v[0].keys():
                                colors.append(None)

                            else:
                                colors.append(v[0]['colors'])


df = pd.DataFrame.from_dict(dict)
df.to_json('rooms_df.json', orient='records')  # , lines=True)
df.to_csv('rooms_df.csv', header=True, index=False)
# print(df.head(3))
