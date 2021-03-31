from requests import get

url_rooms_yandex = 'https://realty.yandex.ru/gate/map/offers-gen2/?mapPolygon=55.82643%2C37.82826%3B55.89285%2C37.70192%3B55.90828%2C37.53712%3B55.86583%2C37.39704%3B55.7413%2C37.36821%3B55.59227%2C37.52064%3B55.56971%2C37.69093%3B55.65211%2C37.84336&zoom=12.81&rgid=324292&type=SELL&category=ROOMS&lat=55.683113&lon=37.521805&id=8652432882015990272&pageSize=100&crc=u683441e0cdbe3a65b7c778745e794238'


rooms_yandex = []

dict_headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://realty.yandex.ru/marushkino/kupit/kvartira/studiya/?bottomLatitude=55.574907&leftLongitude=37.050028&rightLongitude=37.437302&topLatitude=55.608008&zoom=12.56&page=2',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://realty.yandex.ru/marushkino/kupit/komnata/karta/?activePoint=55.683113%2C37.521805&bottomLatitude=55.661888&leftLongitude=37.42121&mapPolygon=55.82643%2C37.82826%3B55.89285%2C37.70192%3B55.90828%2C37.53712%3B55.86583%2C37.39704%3B55.7413%2C37.36821%3B55.59227%2C37.52064%3B55.56971%2C37.69093%3B55.65211%2C37.84336&rightLongitude=37.686749&topLatitude=55.683579&zoom=12.81',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'yandexuid=2824582811574066622; mda=0; my=YwA=; fuid01=5df0c82975df6958.1CAlSH4RObSZeQdUPO0whfZPpvYeGcK5tO4tboJ0ExwQ76R9xhnPxrlqAXgK3MiEPyUcZFsmqlzyGnkZ5Q-L4U3P1KCk0SX_MIdEx0YuCaxTgCLYyCAWAelKT9PezAvT; yuidss=2824582811574066622; ymex=1631122210.yrts.1599586210#1889426622.yrtsi.1574066622; _ym_uid=1599763889769649623; is_gdpr=0; gdpr=0; is_gdpr_b=CKGPeRDGDCgC; L=YwtZY0BRVE1nWEh5RVtGdQFQZ3BQZmNRQisTQABBIkcQHAh2.1605532619.14421.375640.d094cc30d8b06ec48fc4045854b91575; yandex_login=uid-57lpgpf7; i=UmD+umefZL19p86IRCsXDfXm4Rm8daUbAmC2z+ve9P6UPZ74ID+DZ1fMyxZ9pnGztBHeopakVUs9JqDBjYUJdNhzEME=; yp=1608034694.ygu.1#1610665014.yrts.1579129014#1889426622.yrtsi.1574066622#1920892619.udn.czoyMjAxMzU2MDI6ZmI60J3QsNGC0LDQu9GM0Y8g0K7RgNC40L3QsA%3D%3D#1608203211.szm.1:1440x900:1440x688; _ym_d=1607598411; skid=2688731891612200272; _ga=GA1.2.1425880147.1614273826; _csrf_token=7bc570225a317e686dab12e526f9773085a79814f8672f7b; suid=99bee0e3b6f02917eff36a5a44ee6840.adcbc35562f1bec5222b0ab166ff0ebf; font_loaded=YSv1; amcuid=6824747311615610858; _fbp=fb.1.1616479802286.1857147165; user=1; from=direct; Session_id=3:1617032282.5.0.1605532619030:QgXgfwGv2-zfsSeBcBMAKg:15.1|1004419804.-1.0.1:220135602|232337.777049.bOhn7t6PuW1EuCEcCFNABYn0EyI; sessionid2=3:1617032282.5.0.1605532619030:QgXgfwGv2-zfsSeBcBMAKg:15.1|1004419804.-1.0.1:220135602|232337.538482.FmXrMzXBRrNxjRBxxsB_JkFpJF4; rgid=324292; _ym_isad=2; prev_uaas_data=2824582811574066622%23329667%23323414%23316455%23309353%23300297%23293147%23287705%23292916%23270006%23254621%23241381%23227540%23220600%23337344%23333752%23318278%23284422%23273553%23279804%23245498%23233395%23241661%23214300%23224506%23213159; prev_uaas_expcrypted=N1z2tGC0zfrjDdaiwYnrLAxyJi5tz4MubUWgLy-NLhQtiZ_DFLYzBFPDT0Ef06YCBS9vHZhqlQRMYmaVeSkdiSA-IbmnRbqV4CXRLuKw7QSuhgpwHIk71znydhdU2V89kHaq2s6uHiiQuXY6z4B2WaCfcXldISfHJNCQsi1Ux5tEZ6bQx3zQLTXzPOPqmKi_wgTmbo-wIcveWmfQd_1bx93auz39Sud_API6UPBoWi0QheN-0t5vzpbYtD99mIKX_6treEm4cWvIRXBb4zPSCqZeYGKXm6orultMepp9CDTVQqgP1aC4FG6wOlWqTf8D5yUMsg5A3oicGiI2qpJQbr9YTOBrsOq_9tsmMXLWgmavBFodSXItsfNQ8GbpP-SJzZcDwr1YW9WGlSOzJF8CxQ%2C%2C; X-Vertis-DC=sas; from_lifetime=1617119414124'
    }

response = get(url_rooms_yandex, headers=dict_headers, verify=False)
rooms_yandex = rooms_yandex.json()



for url in url_rooms_yandex:
    response = get(url, headers=dict_headers, verify=False)
    rooms_yandex.append(response)
rooms_yandex = rooms_yandex.json()
