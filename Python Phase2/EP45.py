# dictionary => key (ການເຂົ້າເຖິງຂໍ້ມູນ), value (ຄ່າຂອງຂໍ້ມູນ)

dicts1 = {"red": "ສີແເດງ", "yellow": "ສີເຫຼືຶອງ",
          "blue": "ສີຟ້າ", 3.14: "ຄ່າ Pi"}
country = {"England": "ອັງກິດ"}
# footballers = {"David Beckham": "ນັກເຕະບານ ສັນຊາດ ອັງກິດ"}
# livescore = {2: "Liverpool"}

# print(dicts1[3.14])
# print(country["England"])
# print(footballers["David Beckham"])
# print(livescore[2])


dicts2 = dict({"red": "ສີແເດງ", "yellow": "ສີເຫຼືຶອງ", "blue": "ສີຟ້າ",
              3.14: "ຄ່າ Pi", True: "ໂສດ", False: "ແຕ່ງງານແລ້ວ"})
# print(dicts2["red"])
# print(dicts2[False])

colors = dict({"red": "ສີແເດງ", "yellow": "ສີເຫຼືຶອງ", "blue": "ສີຟ້າ"})
# colors.update({"pink": "ສີບົວ"})
# colors.update({"pink": "ສີບົວ", "orange": "ສີສົ້ມ"})

# for k,v in colors.items():
#     print(k,v)

# print(colors)
# colors.pop("red")
# colors.popitem()
# print(colors)

# print(colors)
# del colors
# print(colors)

# x = colors.copy()
# print(x)

Footballers = {"Ronaldo": {"club": "Manchester United", "country": "Portuguese", "information": [37, "forword"]},
               "Salar": {"club": "Liverpool", "country": "Egypt", "information": [28, "forword"]}, "Mount": {"club": "Chelsea", "country": "England", "information": [24, "midfield"]}}

print(Footballers["Ronaldo"]["country"])
