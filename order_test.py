import data
import sender


# Функция для негативной запрашиваем несуществующий заказ
def test_get_order_by_track_number_404():
    order = sender.get_order_by_track(0)
    # Проверяется, что в теле ответа атрибут "code" равен 404
    assert order.status_code == 404


# Функция для негативной проверки запрашиваем заказ без номера
def test_get_order_by_track_number_400():
    order = sender.get_order_by_track(None)
    # Проверяется, что в теле ответа атрибут "code" равен 400
    assert order.status_code == 400


# Функция для позитивной проверки
def test_get_order_by_track_number():
    new_order_data = data.new_order.copy()
    new_order = sender.post_order(new_order_data)

    # Проверяется, что код ответа равен 201
    assert new_order.status_code == 201

    # Проверяется что по треку можно получить данные о заказе
    track = new_order.json()["track"]

    order = sender.get_order_by_track(track)
    # Проверяется, что код ответа равен 200
    assert order.status_code == 200
