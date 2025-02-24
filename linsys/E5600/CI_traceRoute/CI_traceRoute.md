Linksys E5600 V1.1.0.26 command injection
Product Information

    Device: Linksys E5600
    Firmware Version: V1.1.0.26
    Manufacturer's website information：https://www.linksys.com/
    Firmware download address ：https://downloads.linksys.com/support/assets/firmware/FW_E5600_1.1.0.26_prod.img

image-20250224102758745
Vulnerability Description

In the \usr\share\lua\runtime.lua file, there is a command injection vulnerability in the runtime.traceRoute function via the pt parameter.

image-20250224110329468
Payload

We can trigger this vulnerability by injecting the ls command using the following payload.

image-20250224183329944

image-20250224183654817

