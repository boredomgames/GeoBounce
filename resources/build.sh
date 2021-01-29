pyinstaller --add-data ./GeoBounce/images/:./images/ \
    --icon ./resources/icon.icns --name GeoBounce --windowed \
    ./GeoBounce/__main__.py
