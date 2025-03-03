# Linksys E5600 V1.1.0.26 command injection
## Product Information
Device: Linksys E5600

Firmware Version: V1.1.0.26

Manufacturer's website information：https://www.linksys.com/

Firmware download address ：https://downloads.linksys.com/support/assets/firmware/FW_E5600_1.1.0.26_prod.img

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_count/image-20250224230227518.png)
## Vulnerability Description

In the \usr\share\lua\runtime.lua file, there is a command injection vulnerability in the runtime.pingTest function via the pt["count"] parameter.

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_count/image-20250224230347733.png)

## Payload
![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_count/image-20250224230418983.png)

The telnet connection feature of this router is disabled by default and cannot be configured through the web interface. We can enable this feature by injecting the command `/usr/sbin/telnetd -l /bin/sh` to achieve shell access. [CI_pingTest_count.py](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_count/CI_pingTest_count.py)
![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_count/image-20250224230450821.png)


