## check predict vlaue in history lotto


fr = open('number.txt', 'r')    # อ่านค่าประวัติ

v_lotto = list([])  # keep lotto
all_lotto = 0
for i in fr.readlines():
    v_lotto.append(int(i[:-1]))
    all_lotto += int(i[:-1])

# for i in range(len(v_lotto)-1):
#     result = v_lotto[i] - v_lotto[i +1]
#     if result < 0:
#         result *= (-1)
#     print(result)
print(v_lotto)
print(488316 in v_lotto)

