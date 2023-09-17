# Владислава Сафонова, 8-я когорта — Финальный проект. Инженер по тестированию плюс

import order
import data

def test_get_order_info_by_track():
    track = order.post_new_order(data.order_body).json()['track']
    response = order.get_order(track)
    assert response.status_code == 200


