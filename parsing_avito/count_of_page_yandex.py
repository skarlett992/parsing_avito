import math
# только для комнат
from get_first_page import response_first_page
# ДЛЯ КОМНАТ И КВАРТИР
# from get_flat import response_first_page
# ИЗ ЯНДЕКС РЕАЛТИ!
from yandex_realty import response_first_page

# print(response_first_page)
#TODO: сделать автоматический расчет количества страниц с яндекс реалти
# count_of_pages = math.ceil(int(response_first_page['applyButton']['title'][9:12])
#                            / len(response_first_page['items']))
