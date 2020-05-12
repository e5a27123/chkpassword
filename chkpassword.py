password = 'a123456'
y = 3
while y > 0 :
    x = input('輸入密碼 : ')
    if x != password :
    	y = y - 1
    	print('密碼錯誤! 還有', y,'次機會')
    else :
    	print('登入成功!')
    	break
