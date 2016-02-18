cd ..
pyinstaller --onefile --windowed myLauncher.py
mkdir dist\IMAGES
mkdir dist\USER_data
copy IMAGES\*.* dist\IMAGES\*.*
copy USER_data\*.* dist\USER_data\*.*
rmdir build /S
rem move dist\IMAGES\*.* myCompile2exe\dist\IMAGES\*.*
copy dist\*.* myCompile2exe\dist\*.*
cd myCompile2exe