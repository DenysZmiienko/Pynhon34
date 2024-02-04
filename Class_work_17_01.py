

# fale = open('data.txt', 'r', encoding='utf-8')
# log_entry = fale.read()
# fale.close()
# log_entry = log_entry.split("\n")
# student = []
# averege = 0
# for s in log_entry:
#     s = s.split(" ")
#     student.append([s[0], s[1], int(s[2])])
# print("Below 3 points:")
# for p in student:
#     averege += int(p[2])
#     if p[2] < 3:
#         print(f"{p[0]} {p[1]}: {p[2]}")
#     averege /= len(student)
# print(f"Averege: {averege:.2f}")

fname = input('Название файла: ')
f = open(fname,'w+')
while True:
    s = input()
    if s == '': break
f.write(s+'\n')
f.close()