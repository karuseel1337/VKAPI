echo 'Начинаю установку модулей...'
pip3 install -r requirements.txt
chmod +x vkapi
mv vkapi /data/data/com.termux/files/usr/bin
clear
echo "Установка окончена, для запуска пропишите python3 vk.py, для запуска из любой директории пропишите vkapi"
