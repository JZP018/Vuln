# Linksys E5600 V1.1.0.26 command injection
## Product Information

    Device: Linksys E5600
    Firmware Version: V1.1.0.26
    Manufacturer's website information：https://www.linksys.com/
    Firmware download address ：https://downloads.linksys.com/support/assets/firmware/FW_E5600_1.1.0.26_prod.img

![image-20250224102758745](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/XSS_wan_name/image-20250305164521552.png)
## Vulnerability Description
In the \www\pages\setting\connectivity\setting-connectivity-wan.html file, there is a cross-site scripting (XSS) vulnerability in the page_save function via the hostname and  domainName parameter.

![image-20250224110329468](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/XSS_wan_name/image-20250305174246817.png)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/XSS_wan_name/image-20250305174923443.png)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/XSS_wan_name/image-20250305175513938.png)



## Payload
When the user submits the form, due to the lack of validation for `opt_hostname` and `opt_domain` in the `page_save` function, the payload is stored on the server. This triggers a stored cross-site scripting (XSS) vulnerability when the page is rendered.


![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/XSS_wan_name/image-20250305181510064.png)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/XSS_wan_name/image-20250305181551743.png)




