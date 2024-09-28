with open('requirements.txt', 'r') as f:
    for line in f:
        # Извлечение имени пакета до '=='
        package = line.split('==')[0].strip()
        if package and not package.startswith('#'):  # Игнорируем комментарии
            print(package)
