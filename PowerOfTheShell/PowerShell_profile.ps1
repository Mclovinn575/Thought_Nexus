
# Setting Env Variables===================================================================================================
#
$vim_path = 'C:\Program Files\vim\_vimrc'
$local_kb_path = "C:\users\a_e67048.FCSERV\vimwiki_html"
$kb_path = '\\PSW-SCCM-1\sources$\user_data\Michael\Knowledge_Base\index.html'

# Setting Aliases===================================================================================================

sal in enter-pssession

sal sesh New-PsSession

sal disconnect Remove-PsSession

sal np Notepad

sal p Test-NetConnection

sal ss Enable-ScreenSaver

sal dss disable-screensaver

sal t test-connection


# Setting profile functions ===================================================================================================

function footprints {start-process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -ArgumentList "https://swan-fp-02/footprints/servicedesk/application.html#search/saved/13404/search-list-default/769557df-57b7-40fc-a234-0325fe4fca22/11dce5ec-8241-44ba-8383-738ec1585ebb"}

function l {tree /F /A}

function wiki-update {& "$local_kb_path\datasync.ps1"}

function kb {invoke-item $kb_path}

function info {
	param(
	[Parameter(Mandatory)]
	[string]
	$User)
	$user_info = aduser -Filter * | ? {$_ -match $user}
	$e_number = $user_info.SamAccountName
		if($e_number.count -gt 1){
			$eNum_list = $e_number
			write-host "=== Multiple Users Detected ===`n"
			$eNum_list
			while($true){
				$e_number = read-host -prompt "`nChoose an Employee Number"
				if($eNum_list -contains $e_number){
					$additional_info = net user /domain $e_number
					break
				}else{
					write-host "=== Not a valid choice ===" -BackgroundColor Red -ForegroundColor White
					write-host "Try again..."
				}
			}
		
		}else{
			$additional_info = net user /domain $e_number
		}

	if($user_info){
		write-host "`n=== USER INFORMATION ===`n"
		$user_info | ? {$_.SamAccountName -eq $e_number}
		$additional_info

	}else{
		write-host "=== Cannot find specified User ===" -BackgroundColor Red -ForegroundColor White
	}

}

function dup {docker compose up -d}

function down {docker compose down}

function SCCM {mstsc /v:PSW-SCCM-1}

function shell {start-process "C:\Users\e67048\AppData\Local\Programs\Git\git-bash.exe"}

function log {
	param(
	[Parameter(Mandatory)]
	[string]
	$file_path)
	$cmtrace_source = "C:\Windows\CCM\cmtrace.exe"
	if(test-path $file_path){
		& $cmtrace_source $file_path
	}

	}

function Remote-Desktop {
	param(
	[Parameter(Mandatory)]
	[string]
	$Device)
	$location = get-location
	set-location -path "C:\"
	
	write-host "`n=== Pinging $Device ===`n"
	$ping = Test-NetConnection -ComputerName $Device
	$target_ip = $ping.RemoteAddress

	if($ping.PingSucceeded){
		write-host "Ping Successful.`n`nAttempting to connect [ $target_ip  ]...`n"
		if(!(test-path "\\$device\c$\users\a_e67048.fcserv\documents\WindowsPowershell\Microsoft.PowerShell_profile.ps1")){
			ni -type file -Path "\\$device\c$\users\a_e67048.fcserv\documents\WindowsPowershell\Microsoft.PowerShell_profile.ps1" -Force
		}elseif(!(test-path "\\$device\c$\users\a_e67048\documents\WindowsPowershell\Microsoft.PowerShell_profile.ps1")){
			ni -type file -Path "\\$device\c$\users\a_e67048\documents\WindowsPowershell\Microsoft.PowerShell_profile.ps1" -Force
		}

		# Attempt to copy $profile to target computer
		cp C:\Users\a_e67048.FCSERV\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1 "\\$device\c$\Users\a_e67048.FCSERV\Documents\WindowsPowershell\Microsoft.PowerShell_profile.ps1" -Force -erroraction silentlycontinue
		cp C:\Users\a_e67048.FCSERV\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1 "\\$device\c$\Users\a_e67048\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1" -force -erroraction silentlycontinue

		# Set location to server temporarily to run remote control {SCCM}
		set-location -path "P01:\"
		Invoke-CMRemoteControl -DeviceName $device

		# Revert location back
		set-location $location
		& "C:\Users\e67048\OneDrive - First Community Services\Documents\Work\Scripts\Tools\Failsafe.ps1" $device 5

	}else{
		Write-Host "=== Computer appears offline. ===`n" -BackgroundColor Red -ForegroundColor White
		set-location $location

	}

	}

set-alias remote remote-desktop

function branches {
	param(
	[Parameter(Mandatory)]
	[string]
	$RC)

	Import-Excel \\psw-sccm-1\sources$\Branches.xlsx | ? {$_.RC -eq $RC}

	}

function failsafe {& "C:\Users\e67048\OneDrive - First Community Services\Documents\Work\scripts\failsafe.ps1"}

function backup {& "C:\Users\e67048\OneDrive - First Community Services\Documents\Work\scripts\server_sync\SCCM_Script_update.ps1"}

function web {
	param(
	[Parameter()]
	[string]
	$Site = "home/")
	& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" $Site}

function console {set-location P01:}

function test {
	param(
	[Parameter()]
	[string]
	$Path)
	Test-Path $Path}

function g {
	param(
	[parameter(Mandatory)]
	[string]
	$search)
	$search = $search.replace(' ','+')
	start-process 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' "https://www.google.com/search?q=$search"
}
set-alias google g

function tenable {web "https://cloud.tenable.com/tio/app.html#/myapps"}

function ISE {web "https://172.24.12.16/admin/#context_dir/context_dir_devices"}

function Intune {web "https://intune.microsoft.com/#home"}

function FedEx {web "https://www.fedex.com/secure-login/en-us/#/login-credentials?redirectUrl=https:%2F%2Fwww.fedex.com%2Fshippingplus%2Fen-us%2F"}

# Setting AutoComplete ===================================================================================================


Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

Set-PSReadLineKeyHandler -Key "Alt+l" -Function ForwardChar

Set-PSReadLineKeyHandler -Key "Alt+h" -Function BackwardChar

Set-PSReadLineKeyHandler -Key "Ctrl+h" -Function BackwardWord

Set-PSReadLineKeyHandler -Key "Ctrl+l" -Function ForwardWord

Set-PSReadLineKeyHandler -Key "Ctrl+Alt+l" -Function ClearScreen


# Setting PSDrives ===================================================================================================

New-PSDrive -Name desk -PSProvider FileSystem -Root "C:\Users\e67048\OneDrive - First Community Services\Desktop"

New-PSDrive -Name docs -PSProvider FileSystem -Root "C:\Users\e67048\OneDrive - First Community Services\Documents"

New-PSDrive -Name scripts -PSProvider FileSystem -Root "C:\Users\e67048\OneDrive - First Community Services\Documents\Work\Scripts"

new-psdrive -name Downloads -PSProvider FileSystem -Root C:\Users\e67048\Downloads\

new-psdrive -name java -PSProvider FileSystem -Root "C:\Users\e67048\OneDrive - First Community Services\Documents\Work\Java"

new-psdrive -name python -PSProvider FileSystem -Root "C:\Users\e67048\OneDrive - First Community Services\Documents\Work\Python"

new-psdrive -name docker -PSProvider FileSystem -Root "C:\Users\e67048\OneDrive - First Community Services\Documents\Work\Docker"

new-psdrive -name sccm -PSProvider FileSystem -Root "\\PSW-SCCM-1\sources$\"

new-psdrive -name cylon -PSProvider FileSystem -Root "C:\users\a_e67048.FCSERV\git\CyLON"

# Importing Modules  ===================================================================================================

Import-Module 'C:\Program Files (x86)\Microsoft Configuration Manager\AdminConsole\bin\ConfigurationManager.psd1' -ErrorAction SilentlyContinue

Import-Module "C:\Users\e67048\OneDrive - First Community Services\Documents\cmatrix"
Set-screenSaverTimeout -seconds 30
# Enable-ScreenSaver


# Display Info ===================================================================================================

Write-Host """
============================================================================================================================================================================================================

-- Custom Functions --
> Console | P01:\
> Shell | Bash
> Branches | Basic Branch Information
> Remote-Desktop | Microsoft Remote Desktop
> SCCM | Launches Configuration Manager

============================================================================================================================================================================================================
"""

cd scripts:
