Invoke-WebRequest "https://www.python.org/ftp/python/3.8.10/python-3.8.10-embed-amd64.zip" -OutFile "python-3.8.10-embed-amd64.zip"
Invoke-WebRequest "https://www.python.org/ftp/python/3.8.10/python-3.8.10-embed-win32.zip" -OutFile "python-3.8.10-embed-win32.zip"

Expand-Archive "python-3.8.10-embed-amd64.zip" -DestinationPath "python-3.8.10-embed-amd64"
Expand-Archive "python-3.8.10-embed-win32.zip" -DestinationPath "python-3.8.10-embed-win32"

Remove-Item -Path "python-3.8.10-embed-amd64.zip"
Remove-Item -Path "python-3.8.10-embed-win32.zip"

$scripts = Get-ChildItem -Path "src/*" -Include *.py

foreach ($script in $scripts)
{
	New-Item "$($script.BaseName).bat" -ItemType File -Value "if exist `"C:\Program Files (x86)\`" ( %COMSPEC% /C `"start python-3.8.10-embed-amd64\python.exe src\$($script.Name)`" ) else ( %COMSPEC% /C `"start python-3.8.10-embed-win32\python.exe src\$($script.Name)`" )"
}