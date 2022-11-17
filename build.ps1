Invoke-WebRequest "https://www.python.org/ftp/python/3.8.10/python-3.8.10-embed-win32.zip" -OutFile "python-3.8.10-embed-win32.zip"
Expand-Archive "python-3.8.10-embed-win32.zip" -DestinationPath "bin"
Remove-Item -Path "python-3.8.10-embed-win32.zip"

Invoke-WebRequest "http://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x64.exe" -OutFile (New-Item -Path "deps\vc_redist.x64.exe" -Force)
Invoke-WebRequest "http://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x86.exe" -OutFile (New-Item -Path "deps\vc_redist.x86.exe" -Force)

$WshShell = New-Object -comObject WScript.Shell
$scripts = Get-ChildItem -Path "src/*" -Include *.py

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