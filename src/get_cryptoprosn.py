import winreg, subprocess


def clip(value: str):
    cmd = "echo " + value.strip() + "|clip"
    return subprocess.check_call(cmd, shell=True)


def output(method: str, value: str, *args):
    if method == "1":
        filename = "cryptoprosn-" + args[0] + ".txt"
        with open(filename, "w") as file:
            file.write(value)
            print("Файл с именем " + filename + " создан в текущей директории")
    elif method == "2":
        print(value)
    elif method == "3":
        clip(value)
        print("Серийный номер скопирован в буфер обмена")
    else:
        print("Способ вывода не был выбран. По-умолчанию будет использоваться консоль")
        print(value)
    return None


output_method = input("Как вывести серийный номер? Файл (1), консоль (2), буфер (3): ")
print("\n")

products = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products", 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)

for i in range(1024):
    try:
        product_name = winreg.EnumKey(products, i)
        properties = winreg.OpenKey(products, product_name + "\\InstallProperties")
        display_name = winreg.QueryValueEx(properties, "DisplayName")[0]
        
        if display_name == "КриптоПро CSP":
            serial_number = winreg.QueryValueEx(properties, "ProductId")[0]
            display_version = winreg.QueryValueEx(properties, "DisplayVersion")[0]
            output(output_method, serial_number, display_version)
    except:
        None

print("\n")
input()