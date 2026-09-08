from pathlib import Path
import shutil

PathDownloads = Path.home() / "Downloads"
PathImages = PathDownloads / "Images" 
PathDocuments = PathDownloads / "Documents" 
PathVideos = PathDownloads / "Videos" 
PathMusic = PathDownloads / "Music" 
PathApplication = PathDownloads / "Application"
PathFile = PathDownloads / "Other Files"

PathImages.mkdir(exist_ok=True)
PathDocuments.mkdir(exist_ok=True)
PathVideos.mkdir(exist_ok=True)
PathMusic.mkdir(exist_ok=True)
PathApplication.mkdir(exist_ok=True)
PathFile.mkdir(exist_ok=True)


imagesSuffix = [".png" , ".jpg" , ".jpeg" , ".gif" ,".webp" , ".heic" ]
documentsSuffix = [".doc" , ".xlsx",".docx" ,".pptx", ".odt" , ".txt" , ".pdf"]
videosSuffix = [".mp4", ".mov",".avi",".mkv",".wmv" , ".flv" , ".webm"]
musicSuffix = [".mp3", ".wav" , ".flac"]
applicationSuffix = [".exe" ,".apk"]


for item in PathDownloads.iterdir():

    print("Name :" +item.name)
    print("Suffix :" +item.suffix)
    print("Stem :"+item.stem)
    if item.is_file():
          print("this is file")
    elif item.is_dir(): 
        print("directory")
    print("_______________________________________________________________")
    
    if item.is_file():
        if item.suffix in imagesSuffix:
            shutil.move(item , PathImages)
        elif item.suffix in documentsSuffix:
            shutil.move(item , PathDocuments)
        elif item.suffix in videosSuffix:
            shutil.move(item ,PathVideos)
        elif item.suffix in musicSuffix:
            shutil.move(item , PathMusic)
        elif item.suffix in applicationSuffix:
            shutil.move(item , PathApplication)
        else :
            shutil.move(item , PathFile)

   


