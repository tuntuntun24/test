def gcd(a,b):
	if (a%b==0):
		return b
	return gcd(b,a%b)
def nd(a,n):
    if gcd(a,n)!=1:
        return "Error!"
    x = [0,1]
    r = [n,a]
    i = 2
    while r[i-1]!=1:
        r.append(r[i-2]%r[i-1])
        q = r[i-2]//r[i-1]
        x.append(x[i-2]-q*x[i-1])
        i += 1
    if(x[i-1]<0):
        return x[i-1]+n 
    return x[i-1]
def uni(a):
	alpha = "a â ă b c d đ e ê f j h i j k l m n o ô ơ p q r s t u ư v w x y z á à ả ã ạ ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ é è ẻ ẽ ẹ ế ề ể ễ ệ í ì ỉ ĩ ị ó ò ỏ õ ọ ố ồ ổ ỗ ộ ớ ờ ở ỡ ợ ú ù ủ ũ ụ ứ ừ ử ữ ự ý ỳ ỷ ỹ ỵ"
	alpha = alpha.split(' ')
	leng = len(alpha)
	for i in range(0,leng):
		alpha.append(alpha[i].upper())
	return alpha.index(a)
def runi(a):
	alpha = "a â ă b c d đ e ê f j h i j k l m n o ô ơ p q r s t u ư v w x y z á à ả ã ạ ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ é è ẻ ẽ ẹ ế ề ể ễ ệ í ì ỉ ĩ ị ó ò ỏ õ ọ ố ồ ổ ỗ ộ ớ ờ ở ỡ ợ ú ù ủ ũ ụ ứ ừ ử ữ ự ý ỳ ỷ ỹ ỵ"
	alpha = alpha.split(' ')
	leng = len(alpha)
	for i in range(0,leng):
		alpha.append(alpha[i].upper())
	return alpha[a]
def luni():
	alpha = "a â ă b c d đ e ê f j h i j k l m n o ô ơ p q r s t u ư v w x y z á à ả ã ạ ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ é è ẻ ẽ ẹ ế ề ể ễ ệ í ì ỉ ĩ ị ó ò ỏ õ ọ ố ồ ổ ỗ ộ ớ ờ ở ỡ ợ ú ù ủ ũ ụ ứ ừ ử ữ ự ý ỳ ỷ ỹ ỵ"
	alpha = alpha.split(' ')
	return len(alpha)

def en(s,a,b):
	if gcd(a,luni())!=1:
		return "Không thể mã hóa do gcd(a,93) không bằng 1"
	res = ""
	for i in range(0,len(s)):
		if s[i].isalpha():
			if s[i].islower():
				res += runi((uni(s[i])*a + b) % luni())
			else:
				res += runi(((uni(s[i])-uni('A'))*a + b) % luni()+uni('A'))
		else:
			res += s[i]
	return res
def de(s,a,b):
	if gcd(a,luni())!=1:
		return "Không thể giải mã do gcd(a,93) không bằng 1"
	a_nd =  nd(a,luni())
	res = ""
	for i in range(0,len(s)):
		if s[i].isalpha():
			if s[i].islower():
				res += runi(a_nd*(uni(s[i])-b) % luni())
			else:
				res += runi(a_nd*(uni(s[i])-uni('A')-b) % luni()+uni('A'))
		else:
			res += s[i]
	return res

s = input("Nhập xâu: ")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Bản mã: "+en(s,a,b))
print("Bản giải mã: "+de(en(s,a,b),a,b))