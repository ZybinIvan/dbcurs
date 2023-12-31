import os
import subprocess
import datetime

# Настройки для подключения к базе данных.
db_name = 'course'
db_user = 'postgres'
db_password = 'Vanya13574'  # Замените на реальный пароль
db_host = 'localhost'  # или ваш хост базы данных
db_port = '5432'  # или ваш порт

# Путь для сохранения резервной копии.
backup_folder = 'datas'

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
    print('Backup successful!')
except Exception as e:
    print(f'Error creating backup: {e}')

# Удаление переменной окружения для безопасности.
del os.environ['PGPASSWORD']
