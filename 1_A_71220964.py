def penghitung_kata(kalimat,kata):
    x = kalimat.count(kata)
    return x
def ubahkata(kalimat,terubah,perubah):
    x = kalimat.replace(terubah,perubah)
    return x
print("===== Program Manipulasi String =====")
print("pilihan Menu :")
print("1. Hitung Kata")
print("2. Ubah Kata")
pilihan = int(input("pilihan anda :"))
kalimat = str(input("masukkan sebuah kalimt/kata :"))
if pilihan==1:
        kata = str(input("masukkan kata yang ingin kita hitung:"))
        J = penghitung_kata(kalimat,kata)
        print("Terdapat Sebanyak",J,"kata",kata,"didalam kalimat")
elif pilihan ==2:
    ubah = str(input("masukkan kata yang ingin diubah :"))
    kataperubah =str(input("masukkan kata pengganti :"))
    J = ubahkata(kalimat,ubah,kataperubah)
    print("string berhasil diubah menjadi:",J)
else:
    print("pilihan yang anda input tidak terdaftar di daftar pilihan")
        