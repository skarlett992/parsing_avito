from math import sin, cos, sqrt, atan2, radians
from features_from_response import df
#функция расчета между координатами комнаты и центром (условно Кремль)
kreml_lat = 55.7522
kreml_lng = 37.6156

#функция расчета между координатами комнаты и центром (условно Кремль)
def distances(data):
# approximate radius of earth in km
    R = 6373.0
    dlat = [lat for lat in data['lat'] - kreml_lat]
    dlon = [lng for lng in data['lng'] - kreml_lng]
    dist = {'lat': [lat for lat in data['lat'] - kreml_lat], 'lng': [lng for lng in data['lng'] - kreml_lng]}
    # dist = zip(dlat, dlon)
    print(type(dist))
    print(len(dist), len(data['lat']), len(data['lng']), len(dlat), len(dlon))
    distances = []
    for dlat, dlon in dist.items():
        lat2 = radians((int(dlat)) + int(kreml_lat))
        dlat = radians(dlat)
        dlon = radians(dlon)

        a = sin(dlat / 2)**2 + cos(kreml_lat) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        distances.append(distance)
    return distances
df['distance'] = distances(df)