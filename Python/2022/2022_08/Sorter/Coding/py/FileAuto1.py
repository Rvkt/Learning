import os
import shutil

source_path = ''
target_path_img = ''
target_path_archive = ''
target_path_text = ''
target_path_music = ''
target_path_video = ''

while True:
    file_names = os.listdir(source_path)
    for file_name in file_names:
        if os.path.join(source_path, file_name).endswith('.png'):
            shutil.move(os.path.join(source_path, file_name), target_path_img)
        if os.path.join(source_path, file_name).endswith('.rar'):
            shutil.move(os.path.join(source_path, file_name), target_path_archive)
        if os.path.join(source_path, file_name).endswith('.txt'):
            shutil.move(os.path.join(source_path, file_name), target_path_text)
        if os.path.join(source_path, file_name).endswith('.mp3'):
            shutil.move(os.path.join(source_path, file_name), target_path_music)
        if os.path.join(source_path, file_name).endswith('.mp4'):
            shutil.move(os.path.join(source_path, file_name), target_path_video)