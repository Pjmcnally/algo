Write-Host "Testing different versions of Sieve of Eratosthenes."
$testValue = 1000000
$modName = "sieve"
$funcNames = @("sieve_list", "sieve_dict", "sieve_dict_odd", "sieve_set",
    "sieve_set_odd")

ForEach($func in $funcNames) {
    Write-Host "`r`n$($func): "
    python -m timeit -s "from $modName import $func" "$func($testValue)"
}
