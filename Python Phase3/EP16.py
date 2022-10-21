try:
    read_flie = open('score.txt', 'r', encoding='utf-8')
    write_flie = open('grade.txt', 'w', encoding='utf-8')
    grade = None
    for line in read_flie.readlines():
        score = line[4:].strip()  # ຄະແນນນັກຮຽນ
        # score = line[-4:].strip()  # s01 80
        studenId = line[:3].strip()  # ລະຫັດນັກຮຽນ
        # print('ລະຫັດ =', studenId, 'ຄະແນນ =', score)
        score = int(score)
        if score >= 80:
            grade = 'A'
        elif score >= 70 and score < 80:
            grade = 'B'
        elif score >= 50 and score <= 69:
            grade = 'C'
        else:
            grade = 'F'
        print('ລະຫັດ =', studenId, 'ຄະແນນ =', score, 'ເກຣດ =', grade)
        write_flie.writelines(studenId+'\t'+str(score)+'\t'+grade+'\n')
    write_flie.close()
    read_flie.close()


except Exception as e:
    print(e)
