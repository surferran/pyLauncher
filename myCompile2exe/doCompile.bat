cd ..
pyinstaller --onefile --windowed myLauncher.py
copy IMAGES\*.* dist\IMAGES\*.*
copy USER_data\*.* dist\USER_data\*.*
rmdir build /S
move dist myCompile2exe\dist
cd myCompile2exe