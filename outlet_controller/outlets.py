import requests
import settings
# Turns Off the Outlet Specified
def off(device):
    payload={'access_token' : settings.SPARK_ACCESS_TOKEN, 'params':'D'+ device +',LOW'}
    url='https://api.spark.io/v1/devices/' + settings.DEVICE_ID +'/digitalwrite'
    requests.post(url, data=payload)
    return "true"
#Turns On the Outlet Specified
def on(device):
    payload={'access_token' : settings.SPARK_ACCESS_TOKEN, 'params':'D'+ device +',HIGH'}
    url='https://api.spark.io/v1/devices/' + settings.DEVICE_ID + '/digitalwrite'
    requests.post(url, data=payload)
    return "true"
