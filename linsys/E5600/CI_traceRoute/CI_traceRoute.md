# Linksys E5600 V1.1.0.26 command injection
## Product Information

    Device: Linksys E5600
    Firmware Version: V1.1.0.26
    Manufacturer's website information：https://www.linksys.com/
    Firmware download address ：https://downloads.linksys.com/support/assets/firmware/FW_E5600_1.1.0.26_prod.img

![image-20250224102758745](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_traceRoute/image-20250224102758745.png)
## Vulnerability Description

In the \usr\share\lua\runtime.lua file, there is a command injection vulnerability in the runtime.traceRoute function via the pt parameter.

![image-20250224110329468](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_traceRoute/image-20250224110329468.png)
## Payload

The telnet connection feature of this router is disabled by default and cannot be configured through the web interface. We can enable this feature by injecting the command `/usr/sbin/telnetd -l /bin/sh` to achieve shell access.[CI_traceRoute.py](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_traceRoute/CI_traceRoute.py)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_traceRoute/image-20250224183329944.png)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_traceRoute/image-20250224183654817.png)

