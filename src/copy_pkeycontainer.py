import winreg, random, string, os

def generate_container_name(length: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length)) + ".000"

def get_users_path() -> str:
    if not os.path.exists("C:\\Program Files (x86)"):
        return "SOFTWARE\\Crypto Pro\\Settings\\Users"
    else:
        return "SOFTWARE\\WOW6432Node\\Crypto Pro\\Settings\\Users"

containers = dict()
users_path = get_users_path()
users = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, users_path)

for i in range(1024):
    try:
        user_name = winreg.EnumKey(users, i)
        user_keys = winreg.OpenKey(users, user_name + "\\Keys")
        
        for j in range(32):
            try:
                container_name = winreg.EnumKey(user_keys, j)
                containers[j] = users_path + "\\" + user_name + "\\Keys\\" + container_name
            except:
                None
    except:
        None

print("\n")
print("Контейнер закрытого ключа какого пользователя необходимо скопировать?\n")

for i in range(len(containers)):
    print(str(i+1) + ". " + containers[i].split("\\")[-1])

print("\n")

sel_num = int(input())
sel_container = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, containers[sel_num-1])

header = winreg.QueryValueEx(sel_container, "header.key")[0]
masks = winreg.QueryValueEx(sel_container, "masks.key")[0]
masks2 = winreg.QueryValueEx(sel_container, "masks2.key")[0]
name = winreg.QueryValueEx(sel_container, "name.key")[0]
primary = winreg.QueryValueEx(sel_container, "primary.key")[0]
primary2 = winreg.QueryValueEx(sel_container, "primary2.key")[0]

folder_name = generate_container_name(8)
curr_dir = os.getcwd()
dest_dir = os.path.join(curr_dir, folder_name)

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

with open(dest_dir + "\\header.key", "wb") as file:
    file.write(header)
with open(dest_dir + "\\masks.key", "wb") as file:
    file.write(masks)
with open(dest_dir + "\\masks2.key", "wb") as file:
    file.write(masks2)
with open(dest_dir + "\\name.key", "wb") as file:
    file.write(name)
with open(dest_dir + "\\primary.key", "wb") as file:
    file.write(primary)
with open(dest_dir + "\\primary2.key", "wb") as file:
    file.write(primary2)

print("Контейнер закрытого ключа был скопирован в папку '" + folder_name + "' в текущей директории")
input()