from cx_Freeze import setup, Executable
import sys

build_options = {
    'packages': [
        "PySide6",
        "cv2",
    ],
    'excludes': ['tkinter'],
    'include_files': [
        ('ffmpeg/', 'lib/ffmpeg/'), # ffmpeg may need to be moved to the lib folder for the build to work
        ('Resources/', 'Resources/')
    ]
}

# GUI applications require a different base on Windows (the default is for a console application).
if sys.platform == 'win32':
    base = 'Win32GUI'
elif sys.platform == 'darwin':
    base = 'Console'
else:
    base = None

executables = [
    Executable(
        'main.py',
        base=base,
        target_name='VidSplit.exe',
        icon="Resources/bread.ico",
        shortcut_name="VidSplit"
    )
]

setup(
    name='VidSplit',
    version='1.00',
    description='A program designed for splitting videos into smaller clips',
    author='Alex Kussauer',
    author_email='akussauer@gmail.com',
    options={'build_exe': build_options},
    executables=executables
)

# Run with "uv run python setup.py build"
# py2app needs to be removed for the build to work