import pyttsx3
import PyPDF3
from tkinter import *
from tkinter import filedialog

tensach=0

def mofile():
    global duonglink
    duonglink= filedialog.askopenfilename()  #mothumucdechonfilepdf
    print(duonglink)    #induonglinkra

def noi():
        nguoidoc = pyttsx3.init()                      # laynguoidoc
        tocdonoi = float(nhaptocdonoi.get())           #Nhaptocdonoi
        nguoidoc.setProperty('rate', tocdonoi)         #caidattocdonoi
        sach = open(duonglink, 'rb')                   # mofilepdf/'rb'=readbinary(định dạng filepdf la binary)
        doc = PyPDF3.PdfFileReader(sach)               # layfilepdf
        sotrang = doc.numPages                         #demsotrang
        print(sotrang)                                 #insotrangra
        trangmuondoc= int(khungnhapsotrang.get())      #nhaptrangmuonbatdaudoc
        print(trangmuondoc)
        for i in range(trangmuondoc-1, sotrang):
            sotrangtrongkhoang = doc.getPage(i)      #laytrangtrongkhoangduocchon
            vanban = sotrangtrongkhoang.extractText()  #layvanbantrongkhoangduocchon
            nguoidoc.say(vanban)                       #doc
            nguoidoc.runAndWait()

cuaso = Tk()   #tao1cuaso
cuaso.title('Sachnoi')   #taotieudecuaso
cuaso.geometry('400x300')  #kichthuoccuaso

tieude=Label(cuaso,text='CHÀO MỪNG ĐẾN VỚI SÁCH NÓI')  #taotieude
tieude.pack()

nutmofilepdf= Button(cuaso,text='Nhấn vào đây để chọn file pdf', command=mofile)
nutmofilepdf.pack(pady=('30','0'))

nhapsotrang= Label(cuaso, text='Bạn muốn đọc từ trang số mấy')
nhapsotrang.pack(pady=('30','0'))

khungnhapsotrang= Entry(cuaso)
khungnhapsotrang.pack()

nhaptocdonoi= Label(cuaso, text='Nhap toc do noi. Khuyen khich:125' )
nhaptocdonoi.pack(pady=('30','0'))
nhaptocdonoi= Entry(cuaso)
nhaptocdonoi.pack()

nutdocsach= Button(cuaso,text='Nhấn vào đây để bắt đầu đọc sách', command=noi)
nutdocsach.pack(pady=('30','0'))


cuaso.mainloop()





