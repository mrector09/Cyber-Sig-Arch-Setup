
@echo off
title UltraCompress - Maximum Compression (Auto 25 MB Limit)
echo UltraCompress - Maximum Compression Script
echo.

:: Specify the file or folder to compress
set /p target="Enter the full path of the file or folder to compress: "

:: Define output compressed file name
set output=UltraCompressed.7z

:: Start 7-Zip compression with maximum settings
echo Compressing with 7-Zip (Ultra Compression)...
7z a -t7z -mx=9 -m0=lzma2 -mfb=273 -md=1536m -ms=on "%output%" "%target%"

:: Check the size of the compressed file
set /a maxsize=26214400
set filesize=%~z0
for %%A in ("%output%") do set filesize=%%~zA

echo Compressed File Size: %filesize% bytes

:: If the file is larger than 25 MB, attempt further compression
if %filesize% gtr %maxsize% (
    echo File is still larger than 25 MB. Optimizing further...
    7z a -t7z -mx=9 -m0=lzma2 -mfb=273 -md=1024m -ms=on -ms=solid "%output%" "%target%"
    for %%A in ("%output%") do set filesize=%%~zA

    echo Re-Compressed File Size: %filesize% bytes
)

:: If still larger, offer to split the file
if %filesize% gtr %maxsize% (
    echo File is still larger than 25 MB. Would you like to split it? (y/n)
    set /p splitchoice="Choice: "
    if /i "%splitchoice%"=="y" (
        echo Splitting the file into 24 MB parts...
        7z a -t7z -v24m -mx=9 "%output%" "%target%"
    ) else (
        echo Compression complete without splitting.
    )
) else (
    echo Compression complete. File size is under 25 MB.
)

pause
