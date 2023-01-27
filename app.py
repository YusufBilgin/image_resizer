import os
import time
from PIL import Image
from colorama import Fore
from colorama import init
from pick import pick

init(autoreset=True)

path = input("Dosya dizini: ")
path = path.replace('\\', '/')
files = os.listdir(path)

title = 'Yüzde kaç küçültmek istediğinizi seçin: '
options = ['10', '20', '33', '40', '50', '60', '70', '80', '90', '100']
option, index = pick(options, title)

try:
    os.mkdir(path + '/output/')
except FileExistsError:
    pass

for file in files:
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        im = Image.open(path + '/' + file)

        width, height = im.size
        width = (width / 100) * int(option)
        height = (height / 100) * int(option)
        size = width, height
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(path + r'/output/%s.png' % (os.path.splitext(file)[0]), "PNG")
        print(str(file) + '  ...........' + Fore.GREEN + ' ok')
    else:
        continue

print(Fore.CYAN + "Dosyalar output adlı klasöre kaydedildi")
time.sleep(5)
