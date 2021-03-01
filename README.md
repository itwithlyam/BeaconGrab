# BeaconGrab

BeaconGrab is the beacon grabbing system which allows you to view any pre-configured Pointr beacons with your Sniffer device.

Usage:
Install Python >= 3.4.0, then download main.py
From there, make sure to edit the request link to your Sniffer's IP address or web tunnel.

## IMPORTANT: If you use the IP address method, make sure you are on the WiFi network configued beforehand in AP mode. Make sure to be on STA mode when using the system!

After that, run the file locally and take a look at the UUID, major, and minor. 
If the RSSI is less than -75, then we can usually say that the beacon is outside of the Sniffer's location, so connection is not needed after.

Please note that, the sniffer refreshes itself every 15-30 seconds (shown by "Scanning" on the screen).

Thanks!

**btw, updates will come soon, watch this repo to be the first to find latest updates**
