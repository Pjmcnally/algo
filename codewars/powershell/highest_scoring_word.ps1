function Get-HighestScoringWord([string]$words) {
    $maxWord = ''
    $maxScore = 0
    ForEach($word in $words -split ' ') {
        $score = 0
        $word.ToCharArray() | ForEach-Object { $score += [int]([char]$_ - 96) }
        if ($score -gt $maxScore) {
            $maxWord, $maxScore = $word, $score
        }
    }

    $maxWord
}

Describe "Fixed Tests" {
    It "Should pass fixed test" {
        Get-HighestScoringWord("man i need a taxi up to ubud") | Should Be "taxi"
    }

    It "Should pass fixed test" {
        Get-HighestScoringWord("what time are we climbing up to the volcano") | Should Be "volcano"
    }

    It "Should pass fixed test" {
        Get-HighestScoringWord("take me to semynak") | Should Be "semynak"
    }
}
