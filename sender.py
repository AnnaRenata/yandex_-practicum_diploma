import requests

import configuration
import data


def post_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         headers=data.headers,
                         json=body)


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        headers=data.headers,
                        params={
                            "t": track
                        })
