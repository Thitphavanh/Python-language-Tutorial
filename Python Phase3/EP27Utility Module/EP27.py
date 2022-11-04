# Module Date / Time
import datetime

result = datetime.datetime.now()
# print(result.year)
# print(result.month)

newDate = datetime.datetime(2022, 10, 31, 8)
# print(newDate)

# ຮູບແບບສະແດງຜົນ
print('ເລີ່ມຕົ້ນ', result)
print(result.strftime('%x'))  # m/d/y ແບບສັ້ນ
print(result.strftime('%X'))  # ເວລາ time
print(result.strftime('%c'))  # ວັນ/ເດືອນ/ວັນທີ ເວລາ ປີ

# ເວລາ
print(result.strftime("%H:%M:%S %p"))

# 1 - 366
print(result.strftime('%j'))

# date
print(result.strftime('%a'))  # ແບບຫຍໍ້
print(result.strftime('%A'))  # ແບບເຕັມ
print(result.strftime('%w')) # 0 = Sunday
print(result.strftime('%d')) # ວັນທີ
print(result.strftime('%b')) # ເດືອນແບບຫຍໍ້
print(result.strftime('%B')) # ເດືອນແບບເຕັມ
print(result.strftime("%d %A %B %Y"))

# ວ/ດ/ປ
print(result.strftime('%d/%m/%Y'))
