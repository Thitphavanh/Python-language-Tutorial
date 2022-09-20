# Tower of Hanoi

'''
n = ຈຳນວນຈານ
ເສົາ => A,B,C

ມີຈານຈຳນວນ 3 ຈານ
n=1 (n-1)
n=2 (n-1)
n=3 (ໃຫຍ່ສຸດ)

A => 3 => C => ໃຫຍ່ => ນ້ອຍ
B (ຈຸດພັກຈານ)

A => ນ້ອຍ ກາງ ໃຫຍ່
A (ນ້ອຍ ກາງ) => B (ນ້ອຍ ກາງ)
A ໃຫຍ່ => C


C => ນ້ອຍ ກາງ ໃຫຍ່

'''


def towOfHanoi(n, a, b, c):
    # a => c
    if(n == 0):
        return
    # ຍ້າຍ a (ນ້ອຍ ກາງ) -> b | c ຈຸດພັກ (ຍ້າຍ a, ພັກ c, ໄປ b)
    towOfHanoi(n-1, a, c, b)
    print('ຈານທີ່ :', n, 'ຈາກ :', a, ' ໄປ :', c)
    towOfHanoi(n-1, b, a, c)


towOfHanoi(3, 'A', 'B', 'C')
