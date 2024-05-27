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

def en(s,k):
	res = ""
	for i in range(0,len(s)):
		if s[i].isalpha():
			if s[i].islower():
				res += runi((uni(s[i])+k) % luni())
			else: 
				res += runi((uni(s[i])-uni('A')+k) % luni() + uni('A'))
		else:
			res += s[i]
	return res
def de(s,k):
	res = ""
	for i in range(0,len(s)):
		if s[i].isalpha():
			if s[i].islower():
				res += runi((uni(s[i])-k) % luni())
			else: 
				res += runi((uni(s[i])-uni('A')-k) % luni() + uni('A'))
		else:
			res += s[i]
	return res

s = input("Nhập xâu: ")
k = int(input("Nhập khóa: "))
print("Bản mã: "+en(s,k))
print("Bản giải mã: "+de(en(s,k),k))
