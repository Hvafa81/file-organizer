# File Organizer

A simple Python script that automatically organizes files in the Windows **Downloads** folder into separate categories based on their file extensions.

## Features

- Detects files inside the `Downloads` folder
- Organizes files into different categories:
  - Images
  - Documents
  - Videos
  - Music
  - Applications
  - Other Files
- Automatically creates category folders if they don't already exist
- Uses Python's `pathlib` for file and path management
- Uses `shutil` to move files

## Supported File Types

| Category | Extensions |
|---|---|
| Images | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.heic` |
| Documents | `.doc`, `.xlsx`, `.docx`, `.pptx`, `.odt`, `.txt`, `.pdf` |
| Videos | `.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`, `.flv`, `.webm` |
| Music | `.mp3`, `.wav`, `.flac` |
| Applications | `.exe`, `.apk` |
| Other Files | Any unsupported extension |

## How It Works

The program checks the user's `Downloads` folder and examines each item.

If the item is a file, its extension is checked against the supported file types. The file is then moved to the appropriate category folder.

For example:

```text
Downloads/
│
├── photo.jpg
├── report.pdf
├── song.mp3
├── video.mp4
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── report.pdf
│
├── Music/
│   └── song.mp3
│
└── Videos/
    └── video.mp4
```

## Requirements

- Python 3.x
- No external Python packages are required.

The project uses Python standard-library modules:

```python
from pathlib import Path
import shutil
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/Hvafa81/file-organizer.git
```

Go to the project directory:

```bash
cd file-organizer
```

Run the script:

```bash
python file_organizer.py
```

The program will organize files in your `Downloads` folder automatically.

## Project Structure

```text
file-organizer/
│
├── file_organizer.py
├── .gitignore
└── README.md
```

## Technologies

- Python
- pathlib
- shutil

## Purpose

This project was created as a Python practice project to work with:

- File System (سیستم فایل)
- Path Management (مدیریت مسیرها)
- File Extensions (پسوند فایل‌ها)
- Conditional Statements (دستورات شرطی)
- Loops (حلقه‌ها)
- Standard Library (کتابخانه استاندارد پایتون)

The project will be gradually refactored to improve its structure, readability, maintainability, and error handling.

## Future Improvements

Planned improvements include:

- Refactoring repeated code
- Using dictionaries for file categorization
- Creating reusable functions
- Adding error handling
- Handling duplicate filenames
- Improving the project structure
- Adding more file categories
- Adding tests
