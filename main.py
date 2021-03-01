import urllib.request
import json
req = urllib.request.Request(
    url=
    'http://0862503ea343.ngrok.io/api/get?action=tagstatus'
)

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))
    version = data['version']
    device = data['device']
    result = data['result']
    print(f'This is data from device {device} on version {version}\n')
    if result[0]:
      if abs(result[0]['rssi']) < 75:
        uuid = result[0]['uuid']
        major = result[0]['major']
        minor = result[0]['minor']
        print(f'UUID: {uuid}\nMajor: {major}\nMinor: {minor}')
      else:
        print('Beacon detected, yet signal is too low to continue.')
    else:
      print('No beacons available. Try again later, or move your device.')

    
    
