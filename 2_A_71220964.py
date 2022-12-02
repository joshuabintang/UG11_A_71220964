def cetakhuruf(str):
    strlength = len(str)
    if strlength % 2 == 0:
     return str[0]+str[1]+'dan'+str[-3]+str[-2]+str[-1]
    else:
        tengah =int(strlength/2)
    return str[tengah-1]+str[tengah]+str[tengah+1]
kata = input("masukkan kata :")
res = cetakhuruf(kata)
print("huruf yang diambil pada kata",kata,"adalah",res)
    