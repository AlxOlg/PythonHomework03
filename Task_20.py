# Scrabble.
price = {
    1: 'AEIOULNSTRАВЕИНОРСТ', 
    2: 'DGДКЛМПУ', 
    3: 'BCMPБГЁЬЯ', 
    4: 'FHVWYЙЫ', 
    5: 'KЖЗХЦЧ', 
    8: 'JXШЭЮ', 
    10: 'QZФЩЪ'
}
word = input('Введите слово: ').upper()
if word.isalpha():
    sum = 0
    for i in price:
        for j in range(len(word)):
            if word[j] in price[i]:
                sum += i
    print(f'Стоимость слова: {sum}')
else:
    print('Недопустимые символы!')
    