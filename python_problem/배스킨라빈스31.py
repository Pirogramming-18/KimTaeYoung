

num = 0
player1 = "PlayerA"
player2 = "PlayerB"
isPlayer1Turn = True

while 1:
  try:
    call = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
  except:
    print("정수를 입력하세요")
    continue
  
  if (call == 0 or call > 3):
    print("1,2,3 중 하나를 입력하세요")
    continue
  
  for _ in range(call):
    num+= 1
  
    print(f'{player1}: {num}') if isPlayer1Turn == True else print(f'{player2}: {num}')


  isPlayer1Turn = ~isPlayer1Turn
