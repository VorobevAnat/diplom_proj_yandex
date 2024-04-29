import requests
import data
import configuration


def post_order():  # Клиент создает заказ.
        return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)


def get_order_track(track):  # Проверяется, что по треку заказа можно получить данные о заказе
        return requests.get(f"{configuration.URL_SERVICE}{configuration.CREATE_ORDER}/track?t={track}")
