function main() {
    Set-Location $PSScriptRoot
    $modName = "prime_factors"
    $funcNames = ConvertFrom-Json (
        python -c "import $modName; print($modName.get_functions())"
    )

    $testValues = @(
        100000,  # Large round number
        111111,  # Large odd number
        5039,  # Prime number
        (4831*5039),  # Product of two primes
        (2*3*4*5*6*7*8*9),  # 10!
        [math]::pow(2,15),  # Large power of 2
        [math]::pow(3,15)   # Large power of 3
    )
    Write-Host "Testing different methods of calculate prime factors of n."
    ForEach($val in $testValues) {
        Write-Host "`r`nTest for n where n = $val`r`n=========================="
        ForEach($func in $funcNames) {
            Write-Host "`r`n$($func): "
            python -m timeit -s "from $modName import $func" "$func($val)"
        }
    }
}

main
