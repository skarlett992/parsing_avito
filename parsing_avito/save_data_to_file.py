from count_of_pages import count_of_pages
# с яндекс реалти
# from count_of_page_yandex import count_of_pages
from main_response import main_response
import json
# count_of_pages = 13

def save_data_to_file():
    rooms = []
    #проходим по всем страницам и в цикле добавляем в json данные для парсинга
    for page_num in range(1, count_of_pages-1):
        current_page = main_response(page_num=page_num)
        # Если с авито :
        rooms.extend(current_page)

        # если с ЯНДЕКС РЕАЛТИ:
    #     rooms.append(current_page)
    # with open('zapas_room_yandex.txt', 'w') as outfile:
    #     json.dump(rooms, outfile)
        # break
        # создаем json с данными только страницы объявлений
    # with open('yandex_rooms.json', 'w') as file:
    #     json_string = json.dumps(rooms)
    #     json.dump(json_string, file)

# save_data_to_file()