import configuration
import requests


def create_order(order_body):

    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body
    )


def get_order_by_track(track_number):

    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track_number}
    )
