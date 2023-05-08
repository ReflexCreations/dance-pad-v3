import hid
from multiprocessing import Process
from ..utils import system

PAD_USB_VID = 0x0483
PAD_USB_PID = 0x5750
PAD_PRODUCT_STRING = "RE:Flex Dance Pad"
USB_HID_PACKET_SIZE = 64

class PadInterfaceModel():
    def __init__(self):
        self.pad = None

    def open(self, serial=None):
        self.pad = hid.device()
        self.pad.open(PAD_USB_VID, PAD_USB_PID, serial_number=serial)
        if self.pad.get_product_string() == PAD_PRODUCT_STRING:
            process = Process(target=self.io_loop, args=(serial,))
            process.start()
        self.lock_access()

    def close(self):
        self.unlock_access()
        self.pad.close()

    def lock_access(self):
        system.lock_access(self.pad)

    def unlock_access(self):
        system.unlock_access(self.pad)

    @staticmethod
    def enumerate():
        pad_list = [p for p in hid.enumerate(PAD_USB_VID, PAD_USB_PID)]
        return pad_list

    @staticmethod
    def io_loop(serial):
        pad = hid.device()
        pad.open(PAD_USB_VID, PAD_USB_PID, serial_number=serial)
        rx_packet = pad.read(USB_HID_PACKET_SIZE)
        print(rx_packet)