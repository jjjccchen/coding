correct_password = 'a123456'

i = 1
while i <= 3:
	user_password = input('請輸入密碼: ')
	if user_password == correct_password:
		print('登入成功')
		break
	else:
		if i == 3:
			print('還是打錯了')
			break
		remain_try = (3 - i)
		remain_try = str(remain_try)
		print('密碼錯誤! 還有'+ remain_try +'次機會')
	i += 1