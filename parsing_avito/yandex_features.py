import pandas as pd
import json
import re
from read_data_from_file import rooms

# regex = re.compile('\s+')

#ТОЛЬКО для авито!
with open('yandex_rooms.json', 'r') as file:
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
heatmaps = []
heatmapInfos = []
regions = []
geo_area = []
price_m2 = []
ceilingHeight = []
livingSpace = []
floorCovering = []
author = []
author_id = []
floor = []
place_id = []
ridWithMetro = []
hasConcierge = []
hasYandexRent = []
hasMetro = []
hasPik = []
isInMO = []
rgidMO = []
isMsk = []
rgidMsk = []
metro_id = []
call_url = []
order_type_id = []
market_rating = []
market_ugc_rating = []
from_MKAD = []

for i, feature in enumerate(rooms):
    for key, value in rooms[i].items():
        if key == 'seo':
            lat.append(value['region']['latitude'])
            lng.append(value['region']['longitude'])
            # print(value['region']['heatmaps'])
            heatmaps.append(value['region']['heatmaps'])
            heatmapInfos.append((value['region']['heatmapInfos'][0]['palette']))
            hasConcierge.append(value['region']['hasConcierge'])
            hasYandexRent.append(value['region']['hasYandexRent'])
            ridWithMetro.append(value['region']['ridWithMetro'])
            hasConcierge.append(value['region']['hasConcierge'])
            hasYandexRent.append(value['region']['hasYandexRent'])
            hasMetro.append(value['region']['hasMetro'])
            hasPik.append(value['region']['hasPik'])
            isInMO.append(value['region']['isInMO'])
            rgidMO.append(value['region']['rgidMO'])
            isMsk.append(value['region']['isMsk'])
            rgidMsk.append(value['region']['rgidMsk'])

            # print(value['region']['heatmapInfos'][0])
            # print(value['footerLinksDecl'])
            list_regions = value['footerLinksDecl'][0]['data']
            for i in list_regions:
                regions.append([int(i['id']), i['name']])
        elif key == 'forms':
            geo_area.append(value['offers']['geo-area'])
            address.append(value['offers']['geo-region']['label'])
        # elif key == 'search':
        #     price.append(value['offers']['entities'][0]['price']['priceForWhole']['value'])
        #     price_m2.append(value['offers']['entities'][0]['price']['pricePerPart']['value'])
        #     area.append(value['offers']['entities'][0]['area']['value'])
        #     metro.append(value['offers']['entities'][0]['location']['metro']['name'])
        #     metro_id.append(value['offers']['entities'][0]['location']['metro']['metroGeoId'])
        elif key == 'direct':
            place_id.append(int(value['place']))

            # if  'ceilingHeight' not in value['offers']['entities'][0]:
            #         ceilingHeight.append(None)
            # else:
            #     ceilingHeight.append(value['offers']['entities'][0]['ceilingHeight'])
            # if 'floorsTotal' not in value['offers']['entities'][0]:
            #     floors_count.append(None)
            # else:
            #     floors_count.append(value['offers']['entities'][0]['livingSpace'])
            # # print(value['offers']['entities'][0]['livingSpace'])
            # if 'value' not in value['offers']['entities'][0]['livingSpace']:
            #     livingSpace.append(None)
            # else:
            #     # print(value['offers']['entities'][0]['livingSpace'])
            #     livingSpace.append(value['offers']['entities'][0]['livingSpace']['value'])
            # if 'floorCovering' not in value['offers']['entities'][0]:
            #     floorCovering.append(None)
            # else:
            #     floorCovering.append(value['offers']['entities'][0]['floorCovering'])
            # if 'id' not in value['offers']['entities'][0]['author']:
            #     author_id.append(None)
            # else:
            #     author_id.append(value['offers']['entities'][0]['author']['id'])
            # if 'category' not in value['offers']['entities'][0]['author']:
            #     author.append(None)
            # else:
            #     author.append(value['offers']['entities'][0]['author']['category'])
            # if 'floorsOffered' not in value['offers']['entities'][0]:
            #     floor.append(None)
            # else:
            #     floor.append(value['offers']['entities'][0]['floorsOffered'][0])
            # if 'place' not in value['offers']['direct']:
            #     place_id.append(None)
            # else:
            #     place_id.append(value['offers']['direct']['place'])


            # for i in value['offers']['direct']['premium']:
            #     address.append(i['address'])
            #     call_url.append(i['call_url'])
            #     metro.append(i['metro'])
            #     metro_id.append(i['order_id'])
            #     order_type_id.append(i['order_type'])
            #     print(i['order_type'])
            #     market_rating.append(i['order_type']['ratings']['market_rating'])
            #     market_ugc_rating.append(i['order_type']['ratings']['market_ugc_rating_float'])
            #     print(i['order_type']['ratings']['sitelinks'])
            #     from_MKAD.append(i['order_type']['ratings']['sitelinks'])



            # if  'order_id' not in value['offers']['direct']['premium']['order_id']:
            #         ceilingHeight.append(None)
            # else:
            #     ceilingHeight.append(value['offers']['entities'][0]['ceilingHeight'])


dict = {'place_id': place_id, 'author': author, 'author_id': author_id, 'room_area, m2': area,
        'ceilingHeight': ceilingHeight, 'floor': floor, 'floors_count': floors_count,
        'price_m2': price_m2, 'lat':lat, 'lng': lng,
        'name': metro, 'address': address, 'price, rub': price}
for i, feature in enumerate(rooms):
    for key, value in rooms[i].items():
        lat.append(['seo']['region']['latitude'])
        # if key not in remove_features:
        #     if key == 'itemId':
        #         itemId.append(value)
        #     if key == 'price':
        #         price.append(value)
        #     if key == 'url':
        #         url.append(value)
        #     if key == 'ext':
        #         ext.append(value)
        #         # print(value, type(value))
        #         if 'metro_distance' not in value:
        #             metro_distance.append(None)
        #             station_1.append(None)
        #             metro_distance_1.append(None)
        #             station_2.append(None)
        #             metro_distance_2.append(None)
        #             station_3.append(None)
        #             metro_distance_3.append(None)
        #
        #         else:
        #             for k, v in value.items():
        #                 if k == 'metro_distance':
        #                     key_list = list(v.keys())
        #                     value_list = list(v.values())
        #                     print(key_list, value_list)
        #                     # for i in key_list:
        #                         # print(key_list[0], key_list[1], key_list[2])
        #                     if len(key_list) == 3:
        #                         station_1.append(key_list[0])
        #                         metro_distance_1.append(value_list[0])
        #                         station_2.append(key_list[1])
        #                         print(value_list[1])
        #                         metro_distance_2.append(value_list[1])
        #                         station_3.append(key_list[2])
        #                         metro_distance_3.append(value_list[2])
        #                     elif len(key_list) == 2:
        #                         station_1.append(key_list[0])
        #                         metro_distance_1.append(value_list[0])
        #                         station_2.append(key_list[1])
        #                         metro_distance_2.append(value_list[1])
        #                         station_3.append(None)
        #                         metro_distance_3.append(None)
        #                     # print(station_3)
        #                     elif len(key_list) == 1:
        #                         station_1.append(key_list[0])
        #                         metro_distance_1.append(value_list[0])
        #                         station_2.append(None)
        #                         metro_distance_2.append(None)
        #                         station_3.append(None)
        #                         metro_distance_3.append(None)
        #                     metro_distance.append(v)
        #         if 'commission' not in value:
        #             commission.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if k == 'commission':
        #                     commission.append(v)
        #
        #         if 'address' not in value:
        #             address.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if k == 'address':
        #                     address.append(v)
        #
        #         if 'area' not in value:
        #             area.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if k == 'area':
        #                     area.append(v[:-3])
        #         if 'rooms' not in value:
        #             rooms_count.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if k == 'rooms':
        #                     rooms_count.append(v)
        #         if 'floor' not in value:
        #             floor.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if k == 'floor':
        #                     floor.append(v)
        #         if 'floors_count' not in value:
        #             floors_count.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if k == 'floors_count':
        #                     floors_count.append(v)
        #         if 'house_type' not in value:
        #             house_type.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if k == 'house_type':
        #                     house_type.append(v)
        #
        #     if key == 'coords':
        #         coords.append(value)
        #         # print(value, type(value))
        #         if 'lat' not in value:
        #             lat.append(None)
        #
        #         else:
        #             for k, v in value.items():
        #                 if k == 'lat':
        #                     lat.append(v)
        #         if 'lng' not in value:
        #             lng.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if k == 'lng':
        #                     lng.append(v)
        #
        #
        #     if key == 'geo':
        #         geo.append(value)
        #         if 'geoReferences' not in value:
        #             # print(value)
        #             metro.append(None)
        #             colors1.append(None)
        #             colors2.append(None)
        #         else:
        #             for k, v in value.items():
        #                 if type(v[0]) == type(dict):
        #                     if 'content' not in v[0].keys():
        #                         # print(v[0].keys(), v[0].values())
        #                         metro.append(None)
        #                     else:
        #                         metro.append(v[0]['content'])
        #                     if 'colors' not in v[0].keys():
        #                         colors.append(None)
        #
        #                     else:
        #                         colors.append(v[0]['colors'])


df = pd.DataFrame.from_dict(dict)
df.to_json('rooms_df.json', orient='records')  # , lines=True)
df.to_csv('rooms_df.csv', header=True, index=False)
# print(df.head(3))