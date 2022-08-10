# /esptool.py -p (PORT) -b 460800 --before default_reset --after hard_reset --chip esp32  write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x1000 build-FRI3D_BADGE_2020_REV2/bootloader/bootloader.bin 0x8000 build-FRI3D_BADGE_2020_REV2/partition_table/partition-table.bin 0x10000 build-FRI3D_BADGE_2020_REV2/micropython.bin
# /Users/calmera/.espressif/python_env/idf4.4_py3.8_env/bin/python ../../../esp-idf/components/esptool_py/esptool/esptool.py -p (PORT) -b 460800 --before default_reset --after hard_reset --chip esp32  write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x1000 build-FRI3D_BADGE_2020_REV2/bootloader/bootloader.bin 0x8000 build-FRI3D_BADGE_2020_REV2/partition_table/partition-table.bin 0x10000 build-FRI3D_BADGE_2020_REV2/micropython.bin

source esp-idf/export.sh

cd micropython/ports/esp32

idf.py -D MICROPY_BOARD=FRI3D_BADGE_2020_REV2 -B build-FRI3D_BADGE_2020_REV2  -p /dev/tty.usbserial-01C81B73 -b 460800 flash