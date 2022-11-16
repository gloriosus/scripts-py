import os, subprocess, winreg


def get_path() -> str:
    if not os.path.exists("C:\\Program Files (x86)"):
        return "C:\\Program Files\\Microsoft\\Edge\\Application"
    else:
        return "C:\\Program Files (x86)\\Microsoft\\Edge\\Application"


app_path = get_path()

apps = [app.path for app in os.scandir(app_path) if app.is_dir()]

for i in range(len(apps)):
    installer = apps[i] + "\\Installer"
    
    if os.path.isdir(installer):
        setup = subprocess.Popen([installer + "\\setup.exe", "--uninstall --system-level --verbose-logging --force-uninstall"])
        setup.wait()

reg = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\EdgeUpdate", 0, winreg.KEY_WRITE | winreg.KEY_WOW64_64KEY)
winreg.SetValueEx(reg, "DoNotUpdateToEdgeWithChromium", 0, winreg.REG_DWORD, 1)

appx = subprocess.Popen(["powershell", "Get-AppxPackage *edge* | Remove-AppxPackage"])
appx.wait()