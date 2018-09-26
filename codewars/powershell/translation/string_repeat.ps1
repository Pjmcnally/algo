<# Translation of String Repeat  https://www.codewars.com/kata/string-repeat/

How to: https://github.com/Codewars/codewars.com/wiki/Tutorial:-How-to-translate-a-kata
Style Guide: https://github.com/PoshCode/PowerShellPracticeAndStyle
Pester Docs: https://github.com/pester/Pester
#>


# Solution
function New-RepeatString {
    [OutputType([string])]
    Param (
      [int]$Repeat,
      [string]$String
    )

    $string * $repeat
  }

# Test Cases
# You can test with Pester (https://github.com/pester/Pester)
# TODO: replace with your own tests (TDD), these are just here to demonstrate usage.

Describe 'Basic Tests' {
    It 'Should return aaaa' {
      New-RepeatString 4 'a' | Should be 'aaaa'
    }
  }

<# Setup
function New-RepeatString {
  [OutputType([string])]
  Param (
    [int]$Repeat,
    [string]$String
  )

  # Your code here
}


#>
