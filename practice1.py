bilet = input("№ Билета ").strip()
a = 0
b = 0
for num_pos in range(len(bilet)):
    try:
        if num_pos % 2 == 0:
            a += int(bilet[num_pos])
        else:
            b += int(bilet[num_pos])
    except Exception as err:
        print(err)
        exit()
if a == b:
    print(f"Билет {bilet} счастливый!")
else:
    print(f"Билет {bilet} несчастливый...")