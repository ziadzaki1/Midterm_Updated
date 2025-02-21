def palindrome(word):
    return word == word[::-1]

options = [
    "1414884937242655719669145562427394884141",  # A
    "6800923757255865070000705685527573290086",  # B
    "9847255590886266818998186626880955527489",  # C
    "6892149109325320763773670235239019412986"   # D
]

for i, num in enumerate(options, start=1):
    print(f"Option {chr(64+i)}: {palindrome(num)}")
