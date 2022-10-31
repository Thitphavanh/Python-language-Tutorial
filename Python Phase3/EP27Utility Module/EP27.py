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
