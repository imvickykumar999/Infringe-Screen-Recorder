
# pip install pyusb

import usb.core, sys
import usb.backend.libusb1

VENDOR_ID = 0x0a07 # OnTrak Control Systems Inc. vendor ID
PRODUCT_ID = 200 # ADU200 Device product name - change this to match your product

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if device is None:
    raise ValueError('ADU Device not found. Please ensure it is connected to the tablet.')
    # sys.exit(1)

# Claim interface 0 - this interface provides IN and OUT endpoints to write to and read from
usb.util.claim_interface(device, 0)
