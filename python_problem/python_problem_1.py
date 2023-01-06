import random

num = 0
player1 = "player"
player2 = "computer"
isPlayerTurn = True


def brGame():
  global num
  global isPlayerTurn
  if isPlayerTurn:
    try:
      call = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
    except ValueError:
      print("정수를 입력하세요")
      return
    if call <= 0 or call > 3:
      print("1,2,3 중 하나를 입력하세요")
      return
  else:
    call = random.randint(1,3)
  
  for i in range(call):
    
    num += 1
    print(f'{player1}: {num}') if isPlayerTurn == True else print(f'{player2}: {num}')
    if num == 31:
      
      print(f'{player2} win!') if isPlayerTurn == True else print(f'{player1} win!')
      return
  isPlayerTurn = not isPlayerTurn

while 1:

  brGame()

  if num == 31:
    break

  
  
  