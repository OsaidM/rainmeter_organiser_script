''' @ Downloads Organizer
    # This script searches your downloads folder
    # and then organizes your files into categorized subfolders
'''

import os
from pathlib import Path
import shutil

DOWNLOADS_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')

def init_category_folders():
    # if these folders not there then create them otherwise ignore
    set_of_categories = {
        'Compressed', 'Documents', 'Music',
        'Pictures', 'Programs', 'Video'
    }
    for category in set_of_categories:
        category_path = os.path.join(DOWNLOADS_PATH, category)
        Path(category_path).mkdir(exist_ok=True)

def pick_a_category(ext):
    # different types of extensions for each category, might update them in future
    all_ext_categories = {
        'Documents': {'.pptx', '.doc', '.docx', '.pdf', '.xlsx', '.xls', '.ppt', '.odt', '.odg'},
        'Programs': {'.exe', '.msi', '.jar'},
        'Compressed': {'.zip', '.rar', '.7z', '.tar'},
        'Pictures': {'.gif', '.png', '.jpg', '.jpeg'},
        'Video': {
            '.mp4', '.mkv', '.mov', '.avi', '.flv',
            '.webm', '.f4v', '.avchd', '.mpeg-2'
            },
        'Music': {'.mp3', '.aac', '.ogg', '.flac', '.alac', '.wav', '.m4a', '.wma'}
    }
    for key, val in all_ext_categories.items():
        if ext.lower() in val:
            return key
    return None

if __name__ == '__main__':
    init_category_folders()
    moved_files = set()
    for file in os.listdir(DOWNLOADS_PATH):
        # ignore hidden and system files
        if file.startswith('.'):
            continue
        # for each file in the downloads folder split extension and decide where to put
        name, ext = os.path.splitext(file)
        if ext == '':
            # ignore files with no extension
            continue
        category = pick_a_category(ext)
        if category is not None:
            src_path = os.path.join(DOWNLOADS_PATH, file)
            dst_path = os.path.join(DOWNLOADS_PATH, category, file)
            if os.path.exists(dst_path):
                # if file already exists in the destination folder, append an integer to the filename
                i = 1
                while True:
                    new_name = f"{name}_{i}{ext}"
                    new_path = os.path.join(DOWNLOADS_PATH, category, new_name)
                    if new_path not in moved_files and not os.path.exists(new_path):
                        dst_path = new_path
                        break
                    i += 1
            try:
                shutil.move(src_path, dst_path)
                moved_files.add(dst_path)
                print(f"Moved {file.encode('utf-8')} to {category} folder.")
            except Exception as e:
                print(f"Error moving {file.encode('utf-8')} to {category} folder: {str(e)}")
