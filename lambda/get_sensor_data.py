import boto3
import urllib.request
import json


def build_response(message):
    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": message
            }
        }
    }


def lambda_handler(event, context):
    if 'GetSensorData' == event['currentIntent']['name']:
        sensor_id = event['currentIntent']['slots']['sensor_id']

        url = "https://dt.nathanglover.com/api/v1/data"
        res = urllib.request.urlopen(url)
        res_body = res.read()
        json_data = json.loads(res_body.decode("utf-8"))

        msg = ""
        for item in json_data['data']:
            if item['sensor_id'] == ("NODE-" + sensor_id):
                msg += "*Node ID*: " + item['sensor_id'] + "\n*Node MAC*: " + item[
                    'sensor_mac'] + "\n*Latitude*: " + str(item['location_lat']) + "\n*Longitude*: " + str(
                    item['location_lon']) + "\n*Last Updated*: " + item['timestamp'] + "\n*GPS Datestamp*: " + item[
                           'datestamp'] + "\n*Altitude*: " + str(item['altitude']) + "\n*Velocity*: " + str(item[
                                                                                                                'velocity']) + "\n*GPS Error*: " + str(
                    item['GPSerror']) + "\n*IMU Error*: " + str(item[
                                                                    'IMUerror']) + "\n*Valid Orientation*: " + str(
                    item['rightdirection']) + "\n*Course*: " + str(item[
                                                                       'course']) + "\n*Satellites*: " + str(
                    item['nsats']) + "\n*SNR1*: " + str(item['snr1']) + "\n*SNR2*: " + \
                       str(item['snr2']) + "\n*SNR3*: " + str(item['snr3']) + "\n*SNR4*: " + str(item['snr4'])

        return build_response(msg)
