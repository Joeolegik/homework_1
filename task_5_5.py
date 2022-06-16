'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:
result = [23, 1, 3, 10, 4, 11] '''

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [el for el in src if src.count(el) == 1]
print(result) #решение не подходящее для собеседования.


unique_src = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_src.add(el)
    else:
        unique_src.discard(el)
    tmp.add(el)
#print(unique_src)

unique_src_ord = [el for el in src if el in unique_src]
print(unique_src_ord)