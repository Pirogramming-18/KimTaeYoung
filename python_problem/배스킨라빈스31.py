
num = 0



while 1:
  try: 
    call = int(input())
  except: 
    print("정수를 입력하세요")
    continue
  
  player1 = "PlayerA"
  
  if call == 0 or call > 3:
    print("1,2,3 중 하나를 입력하세요")
    continue
    
  for _ in range(call):
    num+= 1
    print(f'{player1} : {num}')
    
  if (num >= 31):
    break