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
                msg += "*Node ID*: " + item['sensor_id'] + "\n*Node MAC*: " + item['sensor_mac'] + "\n*Latitude*: " + str(item['location_lat']) + "\n*Longitude*: " + str(item['location_lon']) + "\n*Last Updated*: " + item['timestamp']

        return build_response(msg)
