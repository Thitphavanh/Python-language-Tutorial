
try:
    write_flie = open('score.txt', 'a', encoding='utf-8')
    # print('ສ້ງ flie ໄດ້ແລ້ວ')
    while True:
        studentId = input('ປ້ອນລະຫັດນັກຮຽນ : ')
        if studentId == 'exit':
            break
        score = input('ປ້ອນຄະແນນນັກຮຽນ : ')
        write_flie.writelines(studentId+'\t'+score+'\n')
    write_flie.close()
except Exception as e:
    print(e)
