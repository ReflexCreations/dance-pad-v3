import hid
import multiprocessing

from utils import system

class PadInterfaceModel():
    def __init__(self):
        self.pad = None
        self.USB_VID = 0x0483
        self.USB_PID = 0x5750
    
    def enumerate(self):
        pad_list = [p for p in hid.enumerate(self.USB_VID, self.USB_PID)]
        return pad_list
    
    def open(self, serial):
        self.pad = hid.device()
        try: 
            self.pad.open(self.USB_VID, self.USB_PID, serial_number=serial)
        except Exception as e:
            raise
        self.lock_access()
        if self.pad.get_product_string() == 'RE:Flex Dance Pad':
            self.pad.PACKET_SIZE = 64
            process = multiprocessing.Process(target=self.io_loop, args=(self.pad,))
            process.start()
    
    def close(self):
        self.unlock_access()
        self.pad.close()

    def lock_access(self):
        system.lock_access(self.pad)
        
    def unlock_access(self):
        system.unlock_access(self.pad)

    @staticmethod
    def io_loop(pad):
        rx_packet = pad.read(pad.PACKET_SIZE)