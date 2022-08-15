This is a fork of https://github.com/Fri3dCamp/Badge2020_micropython
stripped to only include micropython with libraries and drivers for display and accelerometer

Then the electrifri3d code is added


## Build steps ##

`git submodule update --init --recursive`

`esp-idf/install.sh esp32`

`./build.sh`

Enjoy

## Windows USB drivers
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

## pre-build golden firmwares (with bugs)
(enables you to reproduce the bugs we had)  
see firmware//electrifri3d_code_13-8-2022_20_37  
install python  
install esptool `pip install esptool`  
run `python flash.py`  
plug in your badge and flashing will start automatically  


## only micropython code with labraries and drivers
see firmware/electrifri3d_no_frozen_code  
install python  
install esptool `pip install esptool`  
run `flash.bat`  
follow instructions on https://github.com/cheops/fri3d-lasertag  
