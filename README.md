# BeaconGrab

BeaconGrab is the beacon grabbing system which allows you to view any pre-configured iBeacons with your Sniffer device. It also includes BeaconSet, the system which lets you add iBeacons to the Sniffer.

## Usage:
Install ngrok, then download the binaries you want
Use ngrok to create an IP tunnel which points to the sniffer's IP address - **Make sure it doesn't go to the API itself**.
From there, you will be asked for the tunnel link.
After that, run the file locally and take a look at the UUID, major, and minor. 
If the RSSI is less than -75, then we can usually say that the beacon is outside of the Sniffer's location, so connection is not needed after.

## Temporary warning: Currently BeaconSet goes against the HTTP Protocol (using GET for a POST operation), so be careful while using it

Please note that, the sniffer refreshes itself every 15-30 seconds (shown by "Scanning" on the screen).

Thanks!

**btw, updates will come soon, watch this repo to be the first to find latest updates**
