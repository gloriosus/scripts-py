import os, subprocess, winreg

app_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application"

apps = [app.path for app in os.scandir(app_path) if app.is_dir()]

for i in range(len(apps)):
    installer = apps[i] + "\\Installer"
    
    if os.path.isdir(installer):
        setup = subprocess.Popen([installer + "\\setup.exe", "--uninstall --system-level --verbose-logging --force-uninstall"])
        setup.wait()

reg_path = "SOFTWARE\\Microsoft\\EdgeUpdate"
reg = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
winreg.SetValueEx(reg, "DoNotUpdateToEdgeWithChromium", 0, winreg.REG_DWORD, 1)

appx = subprocess.Popen(["powershell", "Get-AppxPackage *edge* | Remove-AppxPackage"])
appx.wait()