<#  Find palindromes from given file source.#>

function main() {
    $filePath = Join-Path $PSScriptRoot "..\english_words\alphabetical.txt"
    $words = Get-Content $filePath

    $p = 0
    ForEach($w in $words) {
        $p += ($w -eq ($w[-1..-($w.length)] -join ""))
    }

    return $p
}

main
