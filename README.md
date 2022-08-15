## Build steps ##

`git submodule update --init --recursive`

`esp-idf/install.sh esp32`

`./build.sh`

Enjoy

## Windows USB drivers
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

## pre-build golden firmwares (with bugs)
see firmware//electrifri3d_code_13-8-2022_20_37
install python
install esptool `pip install esptool`
run `python flash.py`
plug in your badge and flashing will start automatically
