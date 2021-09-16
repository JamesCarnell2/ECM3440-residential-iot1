from counterfit_connection import CounterFitConnection

import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

import sys

adc = ADC()
relay = GroveRelay(5)
connection_string = 'HostName=JamesCarnellUniversity.azure-devices.net;DeviceId=soil-moisture-sensor;SharedAccessKey=aTntV9b1kW8eCvQmQzYDPLLH85hVNwkGsQTyfv7ySpA='
device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

def main():
    CounterFitConnection.init('127.0.0.1', 5000)
    
    print('Connecting')
    device_client.connect()
    print('Connected')
    device_client.on_method_request_received = handle_method_request

    # if "pytest" not in sys.modules:
    #     main()
    
    while True:
        soil_moisture = adc.read(0)
        print("Soil moisture:", soil_moisture)

        message = Message(json.dumps({ 'soil_moisture': soil_moisture }))
        device_client.send_message(message)

        time.sleep(10)

def handle_method_request(request):
    print("Direct method received - ", request.name)
    
    if request.name == "relay_on":
        relay.on()
    elif request.name == "relay_off":
        relay.off()

    method_response = MethodResponse.create_from_method_request(request, 200)
    device_client.send_method_response(method_response)

#if "pytest" not in sys.modules:
if __name__ == '__main__':
    main()
