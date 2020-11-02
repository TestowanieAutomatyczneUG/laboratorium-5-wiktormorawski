import math
def roman(arabic):
    result = ''
    if arabic / 1000 > 0:
        result = result + 'M'*(int(arabic/1000))
        arabic = arabic % 1000
    if arabic / 900 > 0:
        result = result + 'CM'*(int(arabic/900))
        arabic = arabic % 900
    if arabic / 500 > 0:
        result = result + 'D'*(int(arabic/500))
        arabic = arabic % 500
    if arabic / 400 > 0:
        result = result + 'CD'*(int(arabic/400))
        arabic = arabic % 400
    if arabic / 100 > 0:
        result = result + 'C'*(int(arabic/100))
        arabic = arabic % 100
    if arabic / 90 > 0:
        result = result + 'XC'*(int(arabic/90))
        arabic = arabic % 90
    if arabic / 50 > 0:
        result = result + 'L'*(int(arabic/50))
        arabic = arabic % 50
    if arabic / 40 > 0:
        result = result + 'XL'*(int(arabic/40))
        arabic = arabic % 40
    if arabic / 10 > 0:
        result = result + 'X'*(int(arabic/10))
        arabic = arabic % 10
    if arabic / 9 > 0:
        result = result + 'IX'*(int(arabic/9))
        arabic = arabic % 9
    if arabic / 5 > 0:
        result = result + 'V'*(int(arabic/5))
        arabic = arabic % 5
    if arabic / 4 > 0:
        result = result + 'IV'*(int(arabic/4))
        arabic = arabic % 4
    if arabic / 1 > 0:
        result = result + 'I'*(int(arabic/1))
        arabic = arabic % 1
    return result
print(roman(27))