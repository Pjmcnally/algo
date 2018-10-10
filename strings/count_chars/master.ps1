Write-Host "`r`nRunning PowerShell file:"
Write-Host (Measure-Command {./count_chars.ps1 -DisplayFull $false})

Write-Host "`r`nRunning Python file:"
Write-Host "Total letters: $(python count_chars.py)"
python -m timeit -u sec -s "import count_chars" -p "count_chars.main(False)"
