tenmon = ['TCC', 'KTVM', 'LLNNPL', 'TTHCM', 'TDLT', 'GTN']
tv = int(input('Nhap so luong thanh vien trong lop '))
sotinchi  = [3, 3, 1, 2, 3, 1]
ds = []
bangdiem = []
for i in range (tv):
    print('Nhap ten thanh vien thu', i + 1)
    s = input()
    ds.append(s)
def nhapdiem():
    for i in range(len(ds)):
        diem = []
        for j in range(len(tenmon)):
            x = float(input('Nhap diem mon ' + str(tenmon[j]) + ' cua ban ' + str(ds[i] + ': ')))
            diem.append(x)
        bangdiem.append(diem)
    return bangdiem
def nhapdrl():
    for i in range (tv):
        print('Nhap diem ren luyen cua ban ', ds[i], ": ")
        diemrenluyen = int(input())
        drl.append(diemrenluyen)
drl=[]
def diemtrungbinh(a):
    tongdiem = 0
    for i in range(len(tenmon)):
        tongdiem += bangdiem[a][i]*sotinchi[i]
    return   float(tongdiem/sum(sotinchi))
def tinhdiem():
    tongdiem = []
    for i in range (tv):
        diemcuoiki = diemtrungbinh(i) + 0.2 * drl[i]
        tongdiem.append(diemcuoiki)
    for i in range(5):
        m = max(tongdiem)
        for j in range (tv):
          if tongdiem[j] == m:
            dstop.append(j)
            tongdiem[j] = 0
            break
        thutudiem.append(m)
thutudiem=[]
dstop=[]
nhapdiem()
nhapdrl()
tinhdiem()
print(thutudiem)
for i in range(5):
    print('TOP ',str(i+1), ' la ban ', ds[dstop[i]], ' voi ', thutudiem[i], ' diem ')


















