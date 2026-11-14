# #1
# name = input("ENTER NAME >> ")
# length = len(name.split())
# print("name >> ", name, "number of words >> ", length)

# #2
# atext = ""
# import random
# for i in range(6):
#     randomtext = str(chr(random.randint(33,127)))
#     atext = atext + randomtext
# print(atext)
# print("HAVE ANY NUMBERS INNIT? >> ",any(char.isdigit() for char in atext))

#3
# du_lieu = input("Nhập các số: ")
# ds = du_lieu.split(",")
# tong = 0
# for so in ds:
# tong = tong + so
# print("Tổng: " + tong)
# print("Lớn nhất:", ds.max())
# ds.sort
# print("Danh sách tăng dần:", ds)

du_lieu = input("Nhap cac so: ")
ds = list(map(int,du_lieu.split()))
tong = 0
for so in ds:
    tong = tong + so
print("Tong: ", tong)
print("Lon nhat: ", max(ds))
print("Danh sach tang dan: ",sorted(ds))