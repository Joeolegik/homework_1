list_eng_rus = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate(eng_word):
    return (list_eng_rus.get(eng_word))
    # print(eng_rus_dict.get(eng_word))
print(num_translate('one'))
print(num_translate('two'))
print(num_translate('three'))
print(num_translate('four'))
print(num_translate('five'))
print(num_translate('six'))
print(num_translate('seven'))
print(num_translate('eight'))
print(num_translate('nine'))
print(num_translate('ten'))