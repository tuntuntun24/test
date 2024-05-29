import random
from math import pow

def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def gen_key(q):
    key = random.randint(10**5,q)
    while gcd(q,key) != 1:
        key = random.randint(10**5, q)

    return key

def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2 !=0:
            x = (x*y)%c
        y=(y*y)%c
        b=int(b/2)
    return x%c

def encrypt (msg, p, y, a):
    en_msg = []
    k = gen_key(p)
    K=  power(y,k,p)
    c1= power(a,k,p)

    print("k được sử dụng:", k)
    print("K được sử dụng trong mã hóa:", K)
    print("C1 được tính ra:", c1)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    for i in range(0, len(en_msg)):
        en_msg[i] = K*ord(en_msg[i])

    print("C2 (còn gọi là tin nhắn đã mã hóa): ", en_msg)
    print("==================================")
    return en_msg, c1

def decrypt(msg, c1 , x, p):
    dr_msg = []
    K = power(c1,x,p)
    print("Khoá K được sử dụng trong giải mã: ",K)
    for i in range(0, len(msg)):
        dr_msg.append(chr(int(msg[i]/K)))

    return dr_msg

def main():
    msg = "Hà Nội"
    print("Thông tin ban đầu: ",msg)
    p = random.randint(10**10, 10**20)
    a = random.randint(2,p-1)

    x = gen_key(p)
    y = power(a,x,p)

    print("Khoá bí mật p được sử dụng:", p)
    print("Khoá công khai a được sử dụng:", a)
    print("Khoá bí mật x:", x)
    print("Khoá công khai y:", y)
    en_msg , c1 = encrypt(msg,p,y,a)
    dr_msg = decrypt(en_msg,c1,x,p)

    dmsg = ''.join(dr_msg)

    print("Tin nhắn giải mã: ",dmsg)

if __name__ == '__main__':
    main()
