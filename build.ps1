Invoke-WebRequest "https://www.python.org/ftp/python/3.8.10/python-3.8.10-embed-win32.zip" -OutFile "python-3.8.10-embed-win32.zip"
Expand-Archive "python-3.8.10-embed-win32.zip" -DestinationPath "bin"
Remove-Item -Path "python-3.8.10-embed-win32.zip"

$scripts = Get-ChildItem -Path "src/*" -Include *.py

$WshShell = New-Object -comObject WScript.Shell

foreach ($script in $scripts)
{
	$basedir = Split-Path $myInvocation.MyCommand.Path
	$Shortcut = $WshShell.CreateShortcut("$($basedir)\$($script.BaseName).lnk")
	$Shortcut.TargetPath = "$($basedir)\bin\python.exe"
	$Shortcut.Arguments = "src\$($script.Name)"
	$Shortcut.WorkingDirectory = "$($basedir)"
	$Shortcut.IconLocation = "$($basedir)\bin\python.exe"
	$Shortcut.Save()
}