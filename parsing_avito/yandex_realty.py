from requests import get

'''curl 'https://realty.yandex.ru/gate/react-page/get/?bottomLatitude=55.574907&leftLongitude=37.050028&page=2&rightLongitude=37.437302&topLatitude=55.608008&zoom=12.56&rgid=324292&type=SELL&category=APARTMENT&roomsTotal=STUDIO&_pageType=search&_providers=seo&_providers=queryId&_providers=forms&_providers=filters&_providers=filtersParams&_providers=awaps&_providers=direct&_providers=mapsPromo&_providers=newbuildingPromo&_providers=refinements&_providers=search&_providers=react-search-data&_providers=searchHistoryParams&_providers=searchParams&_providers=searchPresets&_providers=serpDirectPicType&_providers=showSurveyBanner&_providers=seo-data-offers-count&_providers=related-newbuildings&crc=u170ca8d267799379a5c401d4a855a144' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"' \
  -H 'Accept: application/json' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'X-Retpath-Y: https://realty.yandex.ru/marushkino/kupit/kvartira/studiya/?bottomLatitude=55.574907&leftLongitude=37.050028&rightLongitude=37.437302&topLatitude=55.608008&zoom=12.56&page=2' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://realty.yandex.ru/marushkino/kupit/kvartira/studiya/?bottomLatitude=55.574907&leftLongitude=37.050028&rightLongitude=37.437302&topLatitude=55.608008&zoom=12.56&page=2' \
  -H 'Accept-Language: en-US,en;q=0.9,pt;q=0.8,ru;q=0.7' \
  -H 'Cookie: yandexuid=7581725941595363903; yuidss=7581725941595363903; ymex=1910723903.yrts.1595363903#1910723903.yrtsi.1595363903; mda=0; my=YwA=; gdpr=0; _ym_uid=1597688209388684104; fuid01=5f6107fb0ae77452.0U1gNfjZgOVcZknMOYEhopu5ldbywUtqF7gfDwD3Nem57pSxQ4wxi96qaMmzvYBVN5HqIxH8X4c8rHprE11SYnjnBYabrlkGsr3RyLnpLzA_XsVfqRHVXlYPp3C_Hako; is_gdpr=0; is_gdpr_b=CNnvZBC+BCgC; _csrf_token=dce72e5221f4a8262dd65600bf32805d6123a9c19b56d444; suid=d1c43aef962b9e8fa7d312dbf9dd43a2.0d8fb21e040a45544b98e1c8a6f12d72; L=RgpaYldBdVt0WW1VWAVaeXYHcHBjRUpIH0MQLSNDWww/LwQELQ0j.1611040306.14485.326408.1dd12a4261a90931421b12b692c8a27d; yandex_login=iurii.biznigaev; font_loaded=YSv1; user=1; amcuid=3490519381612713195; rgid=324292; ys=udn.cDrQrtGA0LjQuSDQkdC40LfQvdC40LPQsNC10LI%3D#wprid.1614933886511880-173246457377632907458926-production-app-host-man-web-yp-317#c_chck.376713690; i=WX3WtGpPg4eQ5AnstD8mhctgyO2Vu1M/wsG+OuNPEVS8kOSOD7PkKrFG5lircVV92tTVbq5JLIzhNGOzpFyy9fMAldE=; yandex_gid=213; _ym_isad=2; zm=m-white_bender-redesign.webp.css-https%3As3home-static_xxy56WqUENwP-rORiseNYWlDCHs%3Al; Session_id=3:1616782997.5.0.1596379791232:bWw7sA:7e.1|466634927.4759060.2.1:82149505.2:4759060|699524176.794923.2.2:794923|232199.703930.hu937tp9zhC6pdH2Q94E96YNVdQ; sessionid2=3:1616782997.5.0.1596379791232:bWw7sA:7e.1|466634927.4759060.2.1:82149505.2:4759060|699524176.794923.2.2:794923|232199.673487.ujodJLJH514Hu97rmLDwOJoiki8; _ym_d=1616783171; yabs-frequency=/5/000200000020xq5W/bmXpS9G0000OG27DSR1mbG0001X0OHTIGMs60000340dtYf1ROO00007GFp____cTx1mbG000DS__F___s3KFMs60000640W/; yp=1648115281.ygu.1#1632550999.szm.2:1792x1120:1747x905#1926400306.udn.cDrQrtGA0LjQuSDQkdC40LfQvdC40LPQsNC10LI%3D#1912534714.multib.1#1619461580.csc.1; cycada=nr03yPdi/6uH1ZPDgCUPBzxTfDeIBR09tZh31k0Q0tk=; from=direct; X-Vertis-DC=vla; popup_shown=1; egrn_report_popup_shown=closed; _ym_visorc=w; prev_uaas_data=7581725941595363903%23329667%23323414%23316455%23309353%23300297%23293147%23287705%23292916%23270006%23254621%23241381%23227540%23220600%23333753%23318278%23284422%23273553%23279804%23245497%23233396%23241661%23213160; prev_uaas_expcrypted=N1z2tGC0zfrjDdaiwYnrLAxyJi5tz4MubUWgLy-NLhQtiZ_DFLYzBFPDT0Ef06YCBS9vHZhqlQRMYmaVeSkdiSA-IbmnRbqV4CXRLuKw7QSuhgpwHIk71znydhdU2V89kHaq2s6uHiiQuXY6z4B2WaCfcXldISfHJNCQsi1Ux5tEZ6bQx3zQLTXzPOPqmKi_wgTmbo-wIctcLXVCjuEiF6WQlt9m8PbPBIY11WzC_ld6Q5kL5XrCxf2nFhnZ1Ah12A2aHqqZQPWziqSHgfq_xwEO-Ko28w684ulTf3rHm94qDaUfkxfpnoytMtI_GWlwWz1G0i7Wmpy04Zimg9h9dhEuoThMEmEj; from_lifetime=1616786316612' \
  --compressed'''
main_url = 'https://realty.yandex.ru/gate/react-page/get/'
limit = 10
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
    'Referer': 'https://realty.yandex.ru/marushkino/kupit/kvartira/studiya/?bottomLatitude=55.574907&leftLongitude=37.050028&rightLongitude=37.437302&topLatitude=55.608008&zoom=12.56&page=2',
    'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,ru;q=0.7',
    'Cookie': 'yandexuid=7581725941595363903; yuidss=7581725941595363903; ymex=1910723903.yrts.1595363903#1910723903.yrtsi.1595363903; mda=0; my=YwA=; gdpr=0; _ym_uid=1597688209388684104; fuid01=5f6107fb0ae77452.0U1gNfjZgOVcZknMOYEhopu5ldbywUtqF7gfDwD3Nem57pSxQ4wxi96qaMmzvYBVN5HqIxH8X4c8rHprE11SYnjnBYabrlkGsr3RyLnpLzA_XsVfqRHVXlYPp3C_Hako; is_gdpr=0; is_gdpr_b=CNnvZBC+BCgC; _csrf_token=dce72e5221f4a8262dd65600bf32805d6123a9c19b56d444; suid=d1c43aef962b9e8fa7d312dbf9dd43a2.0d8fb21e040a45544b98e1c8a6f12d72; L=RgpaYldBdVt0WW1VWAVaeXYHcHBjRUpIH0MQLSNDWww/LwQELQ0j.1611040306.14485.326408.1dd12a4261a90931421b12b692c8a27d; yandex_login=iurii.biznigaev; font_loaded=YSv1; user=1; amcuid=3490519381612713195; rgid=324292; ys=udn.cDrQrtGA0LjQuSDQkdC40LfQvdC40LPQsNC10LI%3D#wprid.1614933886511880-173246457377632907458926-production-app-host-man-web-yp-317#c_chck.376713690; i=WX3WtGpPg4eQ5AnstD8mhctgyO2Vu1M/wsG+OuNPEVS8kOSOD7PkKrFG5lircVV92tTVbq5JLIzhNGOzpFyy9fMAldE=; yandex_gid=213; _ym_isad=2; zm=m-white_bender-redesign.webp.css-https%3As3home-static_xxy56WqUENwP-rORiseNYWlDCHs%3Al; Session_id=3:1616782997.5.0.1596379791232:bWw7sA:7e.1|466634927.4759060.2.1:82149505.2:4759060|699524176.794923.2.2:794923|232199.703930.hu937tp9zhC6pdH2Q94E96YNVdQ; sessionid2=3:1616782997.5.0.1596379791232:bWw7sA:7e.1|466634927.4759060.2.1:82149505.2:4759060|699524176.794923.2.2:794923|232199.673487.ujodJLJH514Hu97rmLDwOJoiki8; _ym_d=1616783171; yabs-frequency=/5/000200000020xq5W/bmXpS9G0000OG27DSR1mbG0001X0OHTIGMs60000340dtYf1ROO00007GFp____cTx1mbG000DS__F___s3KFMs60000640W/; yp=1648115281.ygu.1#1632550999.szm.2:1792x1120:1747x905#1926400306.udn.cDrQrtGA0LjQuSDQkdC40LfQvdC40LPQsNC10LI%3D#1912534714.multib.1#1619461580.csc.1; cycada=nr03yPdi/6uH1ZPDgCUPBzxTfDeIBR09tZh31k0Q0tk=; from=direct; X-Vertis-DC=vla; popup_shown=1; egrn_report_popup_shown=closed; _ym_visorc=w; prev_uaas_data=7581725941595363903%23329667%23323414%23316455%23309353%23300297%23293147%23287705%23292916%23270006%23254621%23241381%23227540%23220600%23333753%23318278%23284422%23273553%23279804%23245497%23233396%23241661%23213160; prev_uaas_expcrypted=N1z2tGC0zfrjDdaiwYnrLAxyJi5tz4MubUWgLy-NLhQtiZ_DFLYzBFPDT0Ef06YCBS9vHZhqlQRMYmaVeSkdiSA-IbmnRbqV4CXRLuKw7QSuhgpwHIk71znydhdU2V89kHaq2s6uHiiQuXY6z4B2WaCfcXldISfHJNCQsi1Ux5tEZ6bQx3zQLTXzPOPqmKi_wgTmbo-wIctcLXVCjuEiF6WQlt9m8PbPBIY11WzC_ld6Q5kL5XrCxf2nFhnZ1Ah12A2aHqqZQPWziqSHgfq_xwEO-Ko28w684ulTf3rHm94qDaUfkxfpnoytMtI_GWlwWz1G0i7Wmpy04Zimg9h9dhEuoThMEmEj; from_lifetime=1616786316612'
    }
# dict_params = {
#         'categoryId': 23,
#         'locationId': 637640,
#         'correctorMode': 1,
#         #это номер страницы
#         'page': page_num,
#         'map': 'e30%3D',
#         'params%5B200%5D': 1054,
#         'params%5B511%5D%5B0%5D': 5300,
#         'params%5B511%5D%5B1%5D': 5299,
#         'params%5B511%5D%5B2%5D': 5298,
#         'verticalCategoryId': 1,
#         'rootCategoryId': 4,
#         'viewPort%5Bwidth%5D': 940,
#         'viewPort%5Bheight%5D': 230,
#         'limit': 10
# }
request_url_start = '?bottomLatitude=55.574907&leftLongitude=37.050028&page='
request_url_end = '&rightLongitude=37.437302&topLatitude=55.608008&zoom=12.56&rgid=324292&type=SELL&category=APARTMENT&roomsTotal=STUDIO&_pageType=search&_providers=seo&_providers=queryId&_providers=forms&_providers=filters&_providers=filtersParams&_providers=awaps&_providers=direct&_providers=mapsPromo&_providers=newbuildingPromo&_providers=refinements&_providers=search&_providers=react-search-data&_providers=searchHistoryParams&_providers=searchParams&_providers=searchPresets&_providers=serpDirectPicType&_providers=showSurveyBanner&_providers=seo-data-offers-count&_providers=related-newbuildings&crc=u170ca8d267799379a5c401d4a855a144'
first_page = 1
first_page_url = main_url+request_url_start+str(first_page)+request_url_end+str(limit)
# print(first_page_url)
first_page_response = get(first_page_url, headers=dict_headers, verify=False)
# print(first_page_response)
response_first_page = first_page_response.json()
# print(response_first_page)
