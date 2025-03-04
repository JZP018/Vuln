# Linksys E5600 V1.1.0.26 command injection
## Product Information

    Device: Linksys E5600
    Firmware Version: V1.1.0.26
    Manufacturer's website information：https://www.linksys.com/
    Firmware download address ：https://downloads.linksys.com/support/assets/firmware/FW_E5600_1.1.0.26_prod.img

![image-20250224102758745](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_emailReg_email/image-20250304132331801.png)
## Vulnerability Description

Linksys E5600 v1.1.0.26 was discovered to contain a command injection vulnerability in the runtime.emailReg function . The vulnerability can be triggered via the `pt["email"]` parameter.

![image-20250224110329468](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_emailReg_email/image-20250304132758062.png)
## Payload

The vulnerability was verified by injecting the command `ls > www/999.txt` into the `email` parameter, as shown in the figure below. The result of the `ls` command was successfully displayed in the `999.txt` file located in the router's `www` directory.
[CI_emailReg_email.py](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_emailReg_email/CI_emailReg_email.py)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_emailReg_email/image-20250304133801783.png)


