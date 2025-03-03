# Linksys E5600 V1.1.0.26 command injection
## Product Information
Device: Linksys E5600

Firmware Version: V1.1.0.26

Manufacturer's website information：https://www.linksys.com/

Firmware download address ：https://downloads.linksys.com/support/assets/firmware/FW_E5600_1.1.0.26_prod.img

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_macClone_mc.ip/image-20250303213615891.png)
## Vulnerability Description

In the \usr\share\lua\runtime.lua file, there is a command injection vulnerability in the runtime.macClone function via the mc.ip parameter.

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_macClone_mc.ip/image-20250303213703741.png)

## Payload
![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_macClone_mc.ip/image-20250303213947503.png)

We can trigger this vulnerability by injecting the ls command using the following payload. [CI_pingTest_count.py](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_macClone_mc.ip/CI_macClone_mc.ip.py)

![images](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_macClone_mc.ip/image-20250303214035796.png)



