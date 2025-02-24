# Linksys E5600 V1.1.0.26 command injection
## Product Information
Device: Linksys E5600

Firmware Version: V1.1.0.26

Manufacturer's website information：https://www.linksys.com/

Firmware download address ：https://downloads.linksys.com/support/assets/firmware/FW_E5600_1.1.0.26_prod.img

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_count/image-20250224230227518.png)
## Vulnerability Description

In the \usr\share\lua\runtime.lua file, there is a command injection vulnerability in the runtime.pingTest function via the pt["pkgsize"] parameter.

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_pkgsize/image-20250224231450455.png)

## Payload
![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_pkgsize/image-20250224231510273.png)

We can trigger this vulnerability by injecting the ls command using the following payload. [CI_pingTest_pkgsize.py](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_pkgsize/CI_pingTest_pkgsize.py)
![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_pingTest_pkgsize/image-20250224231527299.png)


