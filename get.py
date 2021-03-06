from tkinter import *
import urllib.request
import json

linkinput = input('What is the IP Tunnel your sniffer runs on? Make sure to include a forward slash at the end. ')

req = urllib.request.Request(
    url=f"{linkinput}api/get?action=tagstatus"
)



with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))
    version = data['version']
    device = data['device']
    result = data['result']
    print(f'This is data from device {device} on version {version}')
    if result[0]:
      text = ""
      for ibeacon in result:
        if abs(ibeacon['rssi']) < 80:
          uuid = ibeacon['uuid']
          text += f"iBeacon detected!\nUUID: {uuid}"
          major = ibeacon['major']
          text += f"\nMajor: {major}"
          minor = result[0]['minor']
          text += f"\nMinor: {minor}\n\n"
          print(text)
        else:
          text += "Configured iBeacon is not in range of Sniffer\n\n"
    else:
      print('No beacons available. Try again later, or move your device.')

def refresh():
  with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))
    version = data['version']
    device = data['device']
    result = data['result']
    print(f'This is data from device {device} on version {version}\n\n')
    if result[0]:
      text = ""
      for ibeacon in result:
        if abs(ibeacon['rssi']) < 80:
          uuid = ibeacon['uuid']
          text += f"iBeacon detected!\nUUID: {uuid}"
          major = ibeacon['major']
          text += f"\nMajor: {major}"
          minor = result[0]['minor']
          text += f"\nMinor: {minor}\n\n"
          print(text)
        else:
          text += "Configured iBeacon is not in range of Sniffer\n\n"
    else:
      print('No beacons available. Try again later, or move your device.')
    status.config(text=text)

tk = Tk()
tk.title("BeaconGrab")

firstText = Label(tk, text=f"Running BeaconGrab on device {device} which uses version {version}\n")
firstText.pack()

if abs(result[0]['rssi']) > 80:
  status = Label(tk, text=text)
else:
  status = Label(tk, text=text)
status.pack()

button = Button(tk, text="Refresh", command=refresh)
button.pack()

tk.mainloop()