# import modules and global variables
from pathlib import Path
import shutil
base_dir = Path("D:/podcast music")
target_dir = base_dir / 'sorted files'

# categories & entensions

file_categories ={
    'images': ['.jpg', '.png', '.heic', ],
    'audio': ['.mp3', '.aac'],
    'videos': ['.mp4', '.mkv', '.avi'],
    'documents': ['.pdf', '.txt', '.xlsx', '.docx', '.pptx'],
    'archives': ['.rar', '.zip']
}

# create categories based on directories

def create_category_directoris():
    for category,_ in file_categories.items():
        (target_dir / category).mkdir(parents=True,exist_ok=True)



# searching and categorizing files

def search_and_categorizing_files():
    for file in base_dir.rglob('*'):
        for category,extensions in file_categories.items():
            if file.suffix in extensions:
                try:
                    shutil.copy(file,target_dir / category)
                except shutil.SameFileError:
                    pass

# run

create_category_directoris()
search_and_categorizing_files()

                    
               
                   
    