#Chap07_ChatGPT로생성한_다운로드받은파일자동분류.py
import os
import glob
import shutil

# Define the source and destination directories
downloads_dir = r'c:\Users\user\Downloads'
images_dir = os.path.join(downloads_dir, 'Images')
pdfs_dir = os.path.join(downloads_dir, 'PDFs')
datasets_dir = os.path.join(downloads_dir, 'DataSets')
archives_dir = os.path.join(downloads_dir, 'Archives')

# Create the destination directories if they don't exist
os.makedirs(images_dir, exist_ok=True)
os.makedirs(pdfs_dir, exist_ok=True)
os.makedirs(datasets_dir, exist_ok=True)
os.makedirs(archives_dir, exist_ok=True)

# Define the file patterns and corresponding destination directories
file_patterns = {
    '*.jpeg': images_dir,
    '*.jpg': images_dir,
    '*.JPEG': images_dir,
    '*.JPG': images_dir,
    '*.pdf': pdfs_dir,
    '*.csv': datasets_dir,
    '*.tsv': datasets_dir,
    '*.xlsx': datasets_dir,
    '*.zip': archives_dir
}

# Move files to their corresponding directories
for pattern, dest_dir in file_patterns.items():
    for file_path in glob.glob(os.path.join(downloads_dir, pattern)):
        try:
            shutil.move(file_path, dest_dir)
            print(f'Moved {file_path} to {dest_dir}')
        except Exception as e:
            print(f'Error moving file {file_path}: {e}')
