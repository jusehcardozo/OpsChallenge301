# Script: Ops 301 Challenge 13
# Author: Jose Cardozo
# Date of latest version:  12/29/2022
# Purpose: Powershell AD Automation

New-ADUser -Name "Franz Ferdinand" -City "Springfield" -State "Oregon" -OtherAttributes @{'title'="TPS Reporting Lead";'mail'="ferdi@GlobeXpower.com"}
