# RE:Flex Dance Pad V3 - Sensor Board

The V3 sensor board iterates upon the V2 'Panel board' and 'I/O board' electronic designs.

## Changes

- The LED grid has been removed, with LED data GPIO pins exposed for external connection. This will allow users to choose an LED architecture, or omit one altogether to significantly reduce cost.
- Power supply has been moved to an external supply, and will no longer be provided by USB, to improve reliability/control of the conditions of supply. On-board switch-mode power supply handles power for both microcontroller and LEDs.
- The UART interface has been upgraded to CAN FD. This increases the robustness of communications between boards and allows for a daisy-chain approach. It also increases the speed of transmission to allow up to 9 panels of data.
- The I/O functionality has been integrated to the sensor board, preventing the need for two separate board designs/system architectures. This board also acts as a panel 'link' board in the Pad Bus standard.
- The sensor input has been exposed to the user, allowing a choice of load cell, force sensitive resistor or traditional sensor options.
- The microcontroller choice has been migrated to STM32G4 series for part availability and long term maintenance. MCU core speed has increased from 72->144MHz to accommodate greater processing speed requirements.
- The microcontroller upgrade also exposes DFU update capabilities, allowing firmware flashing over USB. Firmware updates are now available within the updated python utility.
- The ST-Link functionality has been changed to Async Serial Wire to allow more debugging output for developers, and Nucleo compatibility.
- The status LEDs now come in 3 separate colours for easier identification.
- Board connectors are added to support the new Pad Bus standard.
- Firmware has been moved to a sub-directory to be considered a part of the Sensor Board.
- Firmware has been upgraded to utilize FreeRTOS for increased communications reliability and task scheduling.
