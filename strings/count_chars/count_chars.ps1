function Measure-LetterCount($filePath) {
    $letters = (Get-Content $filePath -Raw).ToCharArray()

    $res = @{}
    ForEach($let in $letters) {
        $res[$let] += 1
    }

    ForEach($elem in @($res.Keys)) {
        if (-not ($elem -match '[a-z]')) {
            $res.Remove($elem)
        }
    }

    return $res
}

function Format-Output($hash) {
    $res.GetEnumerator() | Sort-Object -Property "name" | Format-Table
    Write-Host "Total letters: $(($res.values | Measure-Object -Sum).Sum)"
}


function main($displayFull=$true) {
    $filePath = Join-Path $PSScriptRoot "..\english_words\alphabetical.txt"

    $res = Measure-LetterCount $filePath
    if ($displayFull) {
        Format-Output $res
    } else {
        Write-Host "Total letters: $(($res.values | Measure-Object -Sum).Sum)"
    }
}

main @args
