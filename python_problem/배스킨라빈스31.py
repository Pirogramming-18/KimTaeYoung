
num = 0



while 1:
  call = int(input())

  if isinstance(call, int) == False:
    print("정수를 입력하세요")

  else:
    if call == 0 or call > 3:
      print("1,2,3 중 하나를 입력하세요")

    else:
      break
  
