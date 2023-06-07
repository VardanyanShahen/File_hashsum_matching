import hashlib
import os

def get_file_hash(filename):
    # Проверяем, существует ли файл
    if not os.path.exists(filename):
        print(f"File {filename} does not exist")
        return None

    # Открываем файл в бинарном режиме
    with open(filename, "rb") as f:
        # Вычисляем хэш-сумму содержимого файла
        hash_value = hashlib.sha256(f.read()).hexdigest()
    return hash_value

# Пример использования
# Получаем хэш-сумму файла при первом запуске
initial_hash = get_file_hash('D:\Github\PythonApplication1\my_file.txt')

if initial_hash is None:
    # Остановить выполнение, если файла не существует
    exit()

# Проверяем текущую хэш-сумму файла
current_hash = get_file_hash('D:\Github\my_file.txt')

if current_hash is None:
    # Остановить выполнение, если файла не существует
    exit()

if initial_hash == current_hash:
    print('File has not been modified')
else:
    print('File has been modified')