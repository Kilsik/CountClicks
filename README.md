# Обрезка ссылок с помощью Битли и подсчет кликов для них

Для работы необходимо зарегистрироваться на [Битли](https://bit.ly/) и получить [токен](https://bitly.com/a/oauth_apps)
вида `17c09e20ad155405123ac1977542fecf00231da7`. Его нужно сохранить в файле .env в корне проекта с именем BITLY_TOKEN:
```BITLY_TOKEN=17c09e20ad155405123ac1977542fecf00231da7```

Пример работы утилиты:

```
>> python main.py https://jenyay.net/Programming/Argparse
Битлинк:  https://bit.ly/3JOhBIL

>> python main.py https://bit.ly/3JOhBIL
Количество кликов:  0
```

#### Как установить

Python3 должен быть уже установлен.
Затем используйте pip (или pip3 если есть конфликт с Python2) для
установки зависимостей:
'''
pip imstall -r requirements.txt
'''

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

 Код написан в образовательных целях на онлайн-курсах школы [Devman](https://dvmn.org/)