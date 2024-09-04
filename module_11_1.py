# подключаем библиотеку для работы с запросами
import requests
# подключаем библиотеку для работы с числами
import numpy as np
# подключаем библиотеку для работы с изображениями
from PIL import Image
from PIL import ImageFilter

# указываем город
city = 'Пермь'
# формируем запрос
url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
# отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url)
if weather_data.status_code == 200:
    print('Успех!')
json_weather_data = weather_data.json()
# получаем данные о температуре и о том, как она ощущается
temperature = round(json_weather_data['main']['temp'])
temperature_feels = round(json_weather_data['main']['feels_like'])
# выводим значения на экран
print('Сейчас в городе', city, str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'a:\n {a}')
# получаем количество вложенности массива
print(f'a.ndim:\n {a.ndim}')
# размер матрицы массива
print(f'a.shape:\n {a.shape}')
# получаем числа с равным интервалом в определенном промежутке
print(np.linspace(0, 21, num=8, dtype=np.int64))

# открытие нашей картинки
image = Image.open('buildings.jpg')
# изменение размера
cropped_image = image.crop((177, 882, 1179, 1707))
# снимаем фокус с изображения
blurred_image = cropped_image.filter(ImageFilter.BLUR)
blurred_image.show()
