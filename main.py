# Задача №2
# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон. Нужно написать
# программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
#
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку “Получить OAuth-токен”.
# HOST: https://cloud-api.yandex.net:443


import requests


class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload" # Определяем запрос для получения ссылки
        # согласно документации Yandex.API
        filename = file_path.split('/', )[-1] # Выделяем имя загружаемого файла
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)} # Определяем
        # формат заголовков запроса
        params = {"path": f"C:/{filename}", "overwrite": "true"} # Определяем параметры запроса (назначаем путь
        # загрузки, имя файла и разрешаем перезапись)
        _response = requests.get(upload_url, headers=headers, params=params).json() # Выполняем запрос на получение
        # ссылки для загрузки
        href = _response.get("href", "") # Выделяем ссылку для загрузки в отдельную переменную
        responce = requests.put(href, data=open(file_path, 'rb')) # Выполняем запрос на загрузку файла на Яндекс.Диск
        # по полученной ссылке
        responce.raise_for_status() # Получаем статус отправки файла
        if responce.status_code == 201: # Проверяем отправку по полученному статусу
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    path_to_file = '' # Получаем путь к загружаемому файлу и токен от пользователя
    token = ''
    uploader = YaUploader(token) # Определяем экземпляр класса для токена пользователя
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск") # Загружаем файл на диск
    result = uploader.upload(path_to_file)
    print(result)

