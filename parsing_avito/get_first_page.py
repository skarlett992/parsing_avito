from requests import get

# first_page_url = 'https://www.avito.ru/js/v2/map/items?categoryId=23&locationId=637640&correctorMode=1&page=1&map=e30%3D&params%5B200%5D=1054&params%5B511%5D%5B0%5D=5300&params%5B511%5D%5B1%5D=5299&params%5B511%5D%5B2%5D=5298&verticalCategoryId=1&rootCategoryId=4&viewPort%5Bwidth%5D=940&viewPort%5Bheight%5D=230&limit=10'
# если адрес не валиден, найти корректную первую страницу:
# https://www.avito.ru/moskva/komnaty/prodam-ASgBAgICAUSQA7wQ?cd=1&f=ASgBAQICAUSQA7wQAUD~BzToUuZS5FI&map=e30%3D
# отсюда Request URL в XHR в категории самый первый
main_url = 'https://www.avito.ru/js/v2/map/items'
limit = 10
dict_headers = {
    # 'authority': 'www.avito.ru',
    'accept': 'application/json',
    'x-requested-with': 'XMLHttpRequest',
    'x-source': 'client-browser',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    'content-type': 'application/json',
    # 'sec-fetch-site': 'same-origin',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-dest': 'empty',
    # 'referer': 'https://www.avito.ru/moskva/komnaty/prodam-ASgBAgICAUSQA7wQ?cd=1&f=ASgBAQICAUSQA7wQAUD~BzToUuZS5FI&map=e30=',
    # 'referer': 'https://www.avito.ru/moskva/komnaty/prodam-ASgBAgICAUSQA7wQ?cd=1&f=ASgBAQICAUSQA7wQAUD~BzToUuZS5FI&map=e30%3D',
    # 'cookie': 'u=2fucm3ed.pc136m.g9y2z1sa2h; buyer_selected_search_radius4=0_general; _ym_uid=1576442867562098991; _ga=GA1.2.1885226350.1576442868; _ym_d=1604085141; __gads=ID=c2335394d1c48b87:T=1604085141:S=ALNI_MZQMhydhTl0PMPChHBO3UOvuIkZ8w; buyer_laas_location=637640; buyer_local_priority_v2=0; __cfduid=dbf595db21a13b030b4d6d24665aa4a871615202539; showedStoryIds=60-58-57-51-50-49-47-42-32; lastViewingTime=1615202542264; no-ssr=1; _gcl_au=1.1.1348920047.1615202543; _fbp=fb.1.1615202546038.178932095; isCriteoSetNew=true; SEARCH_HISTORY_IDS=1; buyer_location_id=637640; buyer_popup_location=637640; _gid=GA1.2.2011082348.1615792677; luri=moskva; _ym_isad=2; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa858f6718e375efe92c93bf74210ee38d940e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0ac71e7cb57bbcb8e0ff0c77052689da50d7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eabdc5322845a0cba1a0df103df0c26013a93e76904ac7560d30c79affd4e5f1d11162fe9fd7c8e976755ec3c3e8df1d6461d4382dab48110cf5e61d702b2ac73f7cdd7d7007065d4e04e0f80e5b86a5ca5d0f5b8ef11da64611028400fa4f68e44c772035eab81f5e146b8ae4e81acb9fa46b8ae4e81acb9faf5b8e78c6f0f62a3f054f620239787a7c88c0de1610b7f4f2da10fb74cac1eab2da10fb74cac1eabc98d1c3ab1f148dcc54811c1319f697fce02a0df804225d6; v=1615885529; sx=H4sIAAAAAAACAwXBOw6AIAwA0Lt0dgDlU7iNQexQk8aU2IFwd9+b0KTTcWs8M2toTCqO0JgD1AkfVEhDpT/yXsNY0BxqIHSiyGbkGmzQofrkY8m+7GWtH3/dfH5UAAAA; so=1615885529; dfp_group=27; abp=0; _ym_visorc=b; _dc_gtm_UA-2546784-1=1'
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
request_url_start = '?categoryId=23&locationId=637640&correctorMode=1&page='
request_url_end = '&map=e30%3D&params%5B200%5D=1054&params%5B511%5D%5B0%5D=5300&params%5B511%5D%5B1%5D=5299&params%5B511%5D%5B2%5D=5298&verticalCategoryId=1&rootCategoryId=4&viewPort%5Bwidth%5D=940&viewPort%5Bheight%5D=230&limit='
first_page = 1
first_page_url = main_url+request_url_start+str(first_page)+request_url_end+str(limit)
first_page_response = get(first_page_url, headers=dict_headers, verify=False)
response_first_page = first_page_response.json()


#TODO: дописать функцию, которая указывает, что response == 200