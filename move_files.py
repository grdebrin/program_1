import os
import shutil

def move_files_from_subfolders(folder_path):
    # Проверяем каждый элемент в папке
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # Перемещаем файл в корневую папку
            try:
                shutil.move(file_path, os.path.join(folder_path, file_name))
                print(f"Файл '{file_name}' перемещен в корневую папку.")
            except shutil.Error as e:
                print(f"Не удалось переместить файл '{file_name}': {e}")

# Укажите путь к папке, из которой нужно переместить файлы
folder_to_search = 'your_path'

move_files_from_subfolders(folder_to_search)