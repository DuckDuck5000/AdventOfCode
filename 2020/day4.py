output = rawInput.split("\n\n")

import re

def numberOfValidPassports(array):
    fields = ["pid", "ecl", "hcl", "hgt", "eyr", "iyr", "byr"]
    count = 0
    fieldRegex = {'byr': '(^(19)[2-9][0-9]$)|(^(200)[0-2]$)',
                     'iyr': '(^(201)[0-9]$)|(^(2020)$)',
                     'eyr': '(^(202)[0-9]$)|(^(2030)$)',
                     'hgt': '(^((1[5-8][0-9])|((19)[0-3]))cm$)|(^((59)|(6[0-9])|(7[0-6]))in$)',
                     'hcl': '^#[0-9a-f]{6}$',
                     'ecl': '(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)',
                     'pid': '^[0-9]{9}$'}
    
    for line in array:
        tempCount = 0
        newLine = re.split("[(' ''\n')]", line)
        
        for check in newLine:
            if check[:3] in fields:
                if re.match(fieldRegex[check[:3]], check[4:]):
                    tempCount += 1
        if tempCount == len(fields):
            count += 1
            
    return count


print(numberOfValidPassports(output))
