
num = 0

num = int(input())

while 1:
  

  if isinstance(num, int) == False:
    print("정수를 입력하세요")

  else:
    if num == 0 or num > 3:
      print("1,2,3 중 하나를 입력하세요")

    else:
      break
  
