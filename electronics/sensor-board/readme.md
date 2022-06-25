# RE:Flex Dance Pad V3 - Sensor Board

The V3 sensor board iterates upon the V2 'Panel board' and 'I/O board' electronic designs.

## Changes

- The LED power and LED grid board functionality has been removed, with LED data GPIO pins exposed for external connection. This will allow users to choose an LED architecture, or omit one altogether to significantly reduce cost.
- DIP Switches have been added to specify the panel position. This allows for up to 9 panels in a user-specified layout.
- The UART interface has been upgraded to CAN Bus. This increases the robustness of communications between boards and allows for a daisy-chain approach.
- The I/O functionality has been integrated to the sensor board, preventing the need for two separate board designs/system architectures. 
- The sensor input has been exposed to the user, allowing a choice of load cell, force sensitive resistor or traditional sensor options.
- The microcontroller choice has been migrated to STM32F302 for part availability and long term maintenance.
- The microcontroller upgrade also exposes DFU update capabilities, allowing firmware flashing over USB. Firmware updates are now available within the updated python utility.
- The ST-Link functionality has been changed to JTAG to allow more standardized debugging for developers.
- There is now greater ESD protection for USB and communications.
- The status LEDs now come in 3 separate colours for easier identification.
- A new set of board connectors is available for 'backplanes'.
- Firmware has been moved to a sub-directory to be considered a part of the Sensor Board.
- Firmware has been upgraded to utilize FreeRTOS for increased communications reliability and task scheduling.