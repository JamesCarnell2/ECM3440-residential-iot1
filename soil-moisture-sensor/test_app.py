from mockito import when, mock, unstub
from mockito.mockito import verify

# import app

# class MockClient:
#     on_method_request_received = {}
#     def connect():
#         return True


# when(app.CounterFitConnection).init('127.0.0.1', 5000).thenReturn(True)
# when(app.IoTHubDeviceClient).create_from_connection_string('HostName=moist-hub.azure-devices.net;DeviceId=soil-moisture-sensor;SharedAccessKey=Vg1ScoJmsBVF09aqu3jDhp4si4cUCpUlN9vNtn/ROAU=').thenReturn(MockClient)

# app.main()
# # def test_connection():
# #     assert app.device_client.connect() == True

# def test_dummy():
#     assert True

def test_myfunction():

    import app

    when(app).main().thenReturn('test')
    assert app.device_client == ''
    verify(app.device_client == '')
    unstub()