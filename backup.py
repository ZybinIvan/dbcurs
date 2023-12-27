import os
import subprocess
import datetime

import yadisk

oauth_token = 'y0_AgAAAABXbZ4ZAAsN7wAAAAD2ENv1hLTAKGtETA--FDzYQIQAlQQ0sOg'


def upload_on_Yandex(src_path, filename):
    dst_path = '/data/' + filename
    y = yadisk.YaDisk(token=oauth_token)
    y.upload(src_path, dst_path, overwrite=True)


# Настройки для подключения к базе данных.
db_name = 'course'
db_user = 'postgres'
db_password = 'Vanya13574'  # Замените на реальный пароль
db_host = 'localhost'  # или ваш хост базы данных
db_port = '5432'  # или ваш порт

# Путь для сохранения резервной копии.
backup_folder = 'C:/Users/Ivan/YandexDisk/university/common/5th_semester/databases/Zybin/Projects/curs/datas'

# Создание метки времени для файла.
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
file_name = f'backup_{db_name}_{timestamp}.sql'

# Полный путь к файлу резервной копии.
backup_path = os.path.join(backup_folder, file_name)

# Установка переменной окружения для пароля.
os.environ['PGPASSWORD'] = db_password

# Команда для создания резервной копии.
dump_cmd = f'pg_dump -h {db_host} -p {db_port} -U {db_user} -d {db_name} -F c > {backup_path}'

# Выполнение команды.
try:
    print(f'Creating backup of {db_name} at {backup_path}')
    subprocess.run(dump_cmd, shell=True, check=True)
    upload_on_Yandex(backup_folder + '/' + file_name, file_name)
    print('Backup successful!')
except Exception as e:
    print(f'Error creating backup: {e}')

# Удаление переменной окружения для безопасности.
del os.environ['PGPASSWORD']


