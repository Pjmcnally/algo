function count_triple_threes($start, $stop) {
    $count = 0
    foreach ($num in $start..$stop) {
        if (test_for_three_threes_mod $num) {
            $count += 1
        }
    }

    return $count
}

function test_for_three_threes_mod($num) {
    $three_count = 0
    while ($num -gt 0) {
        if (($num % 10) -eq 3) {
            $three_count += 1
        }
        $num = [int][System.Math]::Floor($num / 10)
    }

    return $three_count -ge 3
}

function main() {
    $start = Get-Date
    Write-Host "starting: $($start.ToString('yyyy-MM-dd hh:mm:ss'))"

    $count = count_triple_threes 100000 1000000

    $end = Get-Date
    Write-Host "Complete: $($end.ToString('yyyy-MM-dd hh:mm:ss'))"

    $duration = $end - $start
    Write-Host "$($duration.ToString('hh\:mm\:ss'))"

    Write-Host "Count: $count"
}

main
