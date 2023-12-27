import os
import subprocess

def restore_database():
    # Настройки для подключения к базе данных.
    db_name = 'course'  # Название базы данных для восстановления
    db_user = 'postgres'  # Имя пользователя
    db_host = 'localhost'  # Адрес сервера базы данных
    db_port = '5432'  # Порт сервера базы данных
    db_password = 'Vanya13574'  # Пароль от пользователя базы данных

    # Путь к файлу резервной копии.
    backup_path = input("Введите полный путь к файлу резервной копии: ")

    # Установка переменной окружения для пароля.
    os.environ['PGPASSWORD'] = db_password

    # Команда для восстановления базы данных.
    restore_cmd = f'pg_restore -h {db_host} -p {db_port} -U {db_user} -d {db_name} -c "{backup_path}"'

    # Выполнение команды.
    try:
        print(f'Восстановление базы данных {db_name} из {backup_path}')
        subprocess.run(restore_cmd, shell=True, check=True)
        print('База данных успешно восстановлена!')
    except Exception as e:
        print(f'Произошла ошибка при восстановлении базы данных: {e}')
    finally:
        # Удаление переменной окружения для безопасности.
        del os.environ['PGPASSWORD']

if __name__ == "__main__":
    restore_database()
