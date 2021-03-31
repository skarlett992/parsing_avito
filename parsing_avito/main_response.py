from requests import get
import pandas as pd
# с авито только комнаты
from get_first_page import dict_headers, limit, main_url, request_url_start, request_url_end
# с авито квартиры
# from get_flat import dict_headers, limit, main_url, request_url_start, request_url_end
# С ЯНДЕКС РЕАЛТИ
# from yandex_realty import dict_headers, limit, main_url, request_url_start, request_url_end

def main_response(page_num):
    url = main_url + request_url_start + str(page_num) + request_url_end + str(limit)
    response = get(url, headers=dict_headers, verify=False)
    # С АВИТО
    response = response.json()['items']
    # С ЯНДЕКС РЕАЛТИ
    # response = response.json()['response']
    return response

