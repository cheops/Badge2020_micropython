#!/bin/bash

BOARD=FRI3D_BADGE_2020_REV2

source esp-idf/export.sh

FIRMWARE_VERSION=`git describe --always --tags --dirty`
ROOTDIR=`pwd`

FIRMWARE_PACKAGE=$ROOTDIR/micropython-$FIRMWARE_VERSION.zip

cd micropython

make -C mpy-cross

cd ports/esp32
# link our board file into micropython
[ ! -e boards/$BOARD ] && ln -s $ROOTDIR/boards/$BOARD boards/$BOARD

# HACK: make git ignore our board dir in the micropython submodule
echo "ports/esp32/boards/$BOARD" > $ROOTDIR/.git/modules/micropython/info/exclude

echo $PWD
make BOARD=$BOARD clean
make -j4 BOARD=$BOARD USER_C_MODULES=$ROOTDIR/st7789_mpy/st7789/micropython.cmake FROZEN_MANIFEST="$ROOTDIR/manifest.py"

rm $FIRMWARE_PACKAGE
pushd build-$BOARD && cp $ROOTDIR/flash_args . && zip $FIRMWARE_PACKAGE flash_args $(cat flash_args | while read _ f; do [[ -f $f ]] && echo $f; done) && popd

echo "Firmware package ready: $FIRMWARE_PACKAGE"
