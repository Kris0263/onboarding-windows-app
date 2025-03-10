# Terminal Knowledge

## Which terminal client did you choose? Why?
I chose **PowerShell** because it is powerful for Windows system administration, supports scripting, and integrates well with Windows Terminal.

## What customizations (if any) did you make?
- Set up aliases (`ll` for `Get-ChildItem`, `cls` for `Clear-Host`).
- Installed `posh-git` to show Git branches in the prompt.
- Changed the theme in Windows Terminal to a dark mode.

## What was the most useful command you learned today?
`Get-Process | Sort-Object -Property CPU -Descending | Select-Object -First 5`
This command lists the top 5 processes consuming the most CPU. It’s useful for monitoring system performance.
