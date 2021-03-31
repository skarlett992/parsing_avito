from save_data_to_file import save_data_to_file
from read_data_from_file import read_data_from_file
# с авито
from features_from_response import df

# с ЯНДЕКС РЕАЛТИ
# from yandex_features import df
# from get_data import get_data

#сохранить все данные в единый json
save_data_to_file()

#распарсить все сохраненные данные
rooms = read_data_from_file()

# достать из данных только необходимое
df = df
# сохранить фрейм в удобоваримый вид
# df = get_data()


# TODO: потом: определять перед записью в файл, какие данные уже есть
#  Кейсы: 1) квартира была добавлена ранее и текущие параметры в ней совпадают - не добавляем
#         2) квартира была доьавлена ранее и текущие параметры не совпадают - обновляем квартиру
#          3) квартира не была добавлена ранее - добавляем квартиру