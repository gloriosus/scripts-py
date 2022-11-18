# scripts-py
* Product version: 1.0.6
* Runtime: python 3.8.10 embedded

## Description
A collection of scripts that may be helpful in system administration. The project was designed to be portable and lightweight. Python 3.8.10 embedded is used as a runtime for executing the scripts on Windows 7 and older without installing full version of python on the system.

## What is included
### get_cryptoprosn.py
Allows to get a serial number (product key) of the installed version of CryptoPro CSP and save it for future installations. The script offers to save the serial number to a text file (1), show on console (2), or copy to the clipboard (3). Each option is selected by typing the corresponding digit. The default output (if none of the options was selected) is console.

If different versions of CryptoPro CSP are presented in the system then the script will output serial numbers of all of the versions. In case of saving to a text file the script will save all serial numbers to different files named with the corresponding version number. A computer name is also added to the end of the file name.

### copy_pkeycontainer.py
This script scans the Windows registry for any CryptoPro private key containers and allows you to choose which container to save on a drive even if the private key container was marked as for no export. 

The container is selected by typing the corresponding digits showing on the console window. If there are no private key containers, the script will output no options to choose from. 

If CryptoPro CSP is not installed on a computer, then the script will output a warning message.

### remove_msedge.py
Removes all versions of Microsoft Edge (old and new Chromium Edge) from the current Windows installation. **CAUTION! The script will just instantly remove the browsers and not output any warnings or messages.**

## How to build and run
1. Run the build.ps1 script from command line or by clicking "Run with PowerShell" in the context menu.
2. Wait until the script will complete its job by downloading all the necessary binaries and generating Windows shortcuts.
3. Run the scripts by double clicking on the shortcuts.
4. In case of showing error messages about missing dlls (e.g. 'api-ms-win-crt-runtime-l1-1-0.dll'), install the Microsoft Visual C++ Redistributables 2015 from the deps folder (x86 on the 32-bit systems, x64 and x86 on the 64-bit systems).
