import math
# только для комнат
# from get_first_page import response_first_page
# ДЛЯ КОМНАТ И КВАРТИР
from get_flat import response_first_page

#TODO: сделать в отдельной функции эту проверку и конкатенацию
# https://www.avito.ru/moskva/komnaty/prodam-ASgBAgICAUSQA7wQ?cd=1&f=ASgBAQICAUSQA7wQAUD~BzToUuZS5FI&map=e30%3D
# отсюда Request URL в XHR в категории самый первый : выглядит примерно так:
# url = 'https://www.avito.ru/js/v2/map/items?categoryId=23&locationId=637640&correctorMode=1&page=1&map=e30%3D&params%5B200%5D=1054&params%5B511%5D%5B0%5D=5300&params%5B511%5D%5B1%5D=5299&params%5B511%5D%5B2%5D=5298&verticalCategoryId=1&rootCategoryId=4&viewPort%5Bwidth%5D=940&viewPort%5Bheight%5D=230&limit=10'

count_of_pages = math.ceil(int(response_first_page['applyButton']['title'][9:12]) / len(response_first_page['items']))
