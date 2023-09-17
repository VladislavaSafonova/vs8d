import configuration
import requests
import data

#Функция создания заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)


response = post_new_order(data.order_body);
print(response.json())

track = response.json()['track']

#Функция получения заказа по его номеру
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))