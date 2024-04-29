import sender_stand_request
# Анатолий Воробьев, 15-я когорта, Финальный проект, Инженер по тестированию плюс

def test_create_order_and_retrieve_order():
    # Запрос на создание заказа
    create_order_responce = sender_stand_request.post_order()
    # Проверка успешности его создания код 201
    assert create_order_responce.status_code == 201, "Не удалось создать заказ"
    # Получение трека заказа
    order_track = create_order_responce.json().get("track")
    # Выполнение запроса на получение закахаза по его треку
    retrieve_order_responce = sender_stand_request.get_order_track(order_track)
    # Проверка кода ответа 200
    assert retrieve_order_responce.status_code == 200, "Не удалось получить заказ"
