function main() {
    Set-Location $PSScriptRoot
    $modName = "sieve"
    $funcNames = ConvertFrom-Json (
        python -c "import $modName; print($modName.get_functions())"
    )

    $testValue = 10000000
    Write-Host "Testing different versions of Sieve of Eratosthenes."
    Write-Host "Test for all numbers from 1 to $testValue"
    ForEach($func in $funcNames) {
        Write-Host "`r`n$($func): "
        python -m timeit -s "from $modName import $func" "$func($testValue)"
    }
}

main
