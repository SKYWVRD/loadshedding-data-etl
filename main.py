import requests
import json

MY_HEADERS = {'token': '175EFE6A-B97D4AE0-B5ACDE31-BB66EA3B'}

def get_current_status():
    response = requests.get(
        'https://developer.sepush.co.za/business/2.0/status', headers=MY_HEADERS)
    json_object = json.loads(response.text)


def get_area_information():
    response = requests.get(
        'https://developer.sepush.co.za/business/2.0/area?id=eskde-10-fourwaysext10cityofjohannesburggauteng&test=current', headers=MY_HEADERS)
