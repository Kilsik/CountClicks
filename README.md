# CountClicks
Обрезка ссылок с помощью сервиса [Bitly.com](https://bitly.com/) и подсчет кликов для них через консоль.
### Окружение
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
Для работы нужна переменная окружения с именем BITLY_TOKEN, содержащая токен API-сервиса. Его можно получить на [Bitly.com](https://bitly.com/a/oauth_apps)
```BITLY_TOKEN=17c09e20ad155405123ac1977542fecf00231da7```
#### Как установить
Python3 должен быть уже установлен.
Затем используйте pip (или pip3 если есть конфликт с Python2) для
установки зависимостей:
```
pip install -r requirements.txt
```
### Пример работы утилиты:

```
>> python main.py https://jenyay.net/Programming/Argparse
Битлинк:  https://bit.ly/3JOhBIL

>> python main.py https://bit.ly/3JOhBIL
Количество кликов:  0
```
### Примечание
 Код написан в образовательных целях на онлайн-курсах школы [Devman](https://dvmn.org/).
