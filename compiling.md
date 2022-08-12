## Build steps

_Warning: this download is big! Ask around if someone at the camp can give you a copy via USB stick._

`git submodule update --init`

`esp-idf/install.sh esp32`

`./build.sh`

Enjoy

## Windows USB drivers
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

## WiFi setup
* Connect to badge via Serial, BAUD: 115200
* send CTRL+C
* settings.set("wifi.essid","YourSSIDHere")
* settings.set("wifi.password","YourPASSWORDhere")
* settings.store()
* (reset), can be done with CTRL+D