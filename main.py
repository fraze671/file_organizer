import os
import shutil
from pathlib import Path
import sys
def organize_files(folder_path: str):
    folder = Path(folder_path)
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
        'Other': []
    }
    for folder_name in folders:
        (folder / folder_name).mkdir(exist_ok=True)
    moved = {'Images': 0, 'Documents': 0, 'Videos': 0, 'Other': 0}
    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            moved_to = 'Other'
            for category, extensions in folders.items():
                if ext in extensions:
                    moved_to = category
                    break
            destination = folder / moved_to / file.name
            shutil.move(str(file), str(destination))
            moved[moved_to] += 1
    print('Готово')
    for category, count in moved.items():
        print(f'{category}: {count} файлов перемещено.')
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Ошибка! Укажите путь к папке')
        print('Пример: python main.py C:/Users/Алиса/Desktop/test_folder')
        sys.exit(1)
    folder_path = sys.argv[1]
    organize_files(folder_path)