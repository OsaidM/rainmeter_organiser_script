'''Downloads Organizer
this script searches your downloads folder
and then organises your files into categorised subfolders
'''
import os
from pathlib import Path
import shutil
os.chdir('C:\\Users\\'+os.getlogin()+'\\Downloads')

def init_category_folders():
    # if these folders not there then create them otherwise ignore
    set_of_categories = {
        'Compressed', 'Documents', 'Music',
        'Pictures', 'Programs', 'Video'
        }
    for category in set_of_categories:
        Path(category).mkdir(exist_ok=True)

def pick_a_category(ext):
    # different types of extensions for each category, might update them in future
    all_ext_categories = {
        'Documents': {'.pptx', '.doc', '.docx', '.pdf', '.xlsx', '.xls', '.ppt', '.odt'},
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
        if ext in val:
            return key

if __name__ == '__main__':
    init_category_folders()
    for file in os.listdir():
        # for each file in the downloads folder split extension and decide where to put
        name, ext = os.path.splitext(file)
        category = pick_a_category(ext)
        if category != None:
            print(file, '-',category)
            shutil.move(file, category)
