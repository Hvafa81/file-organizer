from pathlib import Path
import shutil


downloads_path = Path.home() / "Downloads"
images_path = downloads_path / "Images"
documents_path = downloads_path / "Documents"
videos_path = downloads_path / "Videos"
music_path = downloads_path / "Music"
application_path = downloads_path / "Application"
other_files_path = downloads_path / "Other Files"

images_path.mkdir(exist_ok=True)
documents_path.mkdir(exist_ok=True)
videos_path.mkdir(exist_ok=True)
music_path.mkdir(exist_ok=True)
application_path.mkdir(exist_ok=True)
other_files_path.mkdir(exist_ok=True)


image_suffixes = [".png", ".jpg", ".jpeg", ".gif", ".webp", ".heic"]
document_suffixes = [".doc", ".xlsx", ".docx", ".pptx", ".odt", ".txt", ".pdf"]
video_suffixes = [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"]
music_suffixes = [".mp3", ".wav", ".flac"]
application_suffixes = [".exe", ".apk"]


for item in downloads_path.iterdir():

    print("Name :" + item.name)
    print("Suffix :" + item.suffix)
    print("Stem :" + item.stem)

    if item.is_file():
        print("this is file")
    elif item.is_dir():
        print("directory")

    print("_______________________________________________________________")

    if item.is_file():
        if item.suffix in image_suffixes:
            shutil.move(item, images_path)
        elif item.suffix in document_suffixes:
            shutil.move(item, documents_path)
        elif item.suffix in video_suffixes:
            shutil.move(item, videos_path)
        elif item.suffix in music_suffixes:
            shutil.move(item, music_path)
        elif item.suffix in application_suffixes:
            shutil.move(item, application_path)
        else:
            shutil.move(item, other_files_path)
