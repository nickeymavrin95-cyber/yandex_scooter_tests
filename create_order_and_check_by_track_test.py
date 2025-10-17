import sender_stand_request
import data
import configuration


def test_create_order_and_check_by_track():

    # Шаг 1: Выполнить запрос на создание заказа
    response_create = sender_stand_request.create_order(data.order_body)

    # Проверяем, что заказ создан успешно
    assert response_create.status_code == 201

    # Шаг 2: Сохранить номер трека заказа
    track_number = response_create.json()["track"]
    print(f"Создан заказ с трек-номером: {track_number}")

    # Шаг 3: Выполнить запрос на получение заказа по треку заказа
    response_get = sender_stand_request.get_order_by_track(track_number)

    # Шаг 4: Проверить, что код ответа равен 200
    assert response_get.status_code == 200

    print("Тест пройден успешно!")
