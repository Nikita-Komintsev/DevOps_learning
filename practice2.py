def func_chunk(lst, n):
    for x in range(0, len(lst), n):
        e_c = lst[x: n + x]
        if len(e_c) < n:
            e_c = e_c + [None for y in range(n - len(e_c))]
        yield e_c


len_matrix = int(input('Введите размер матрицы: '))
my_list = []
for i in range(len_matrix ** 2):
    my_list.append(i + 1)

my_list = list(func_chunk(my_list, len_matrix))

for i in range(len(my_list)):
    if i % 2 != 0:
        my_list[i].reverse()

for i in range(len(my_list)):
    for x in my_list:
        print(x[i], end=' ')
    print()
