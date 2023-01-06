import random




num = 0
isPlayer1Turn = True





def brGame():
  global num
  global isPlayer1Turn
  player1 = "player"
  player2 = "computer"
  

  if isPlayer1Turn:
    
    call = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
    
    if (not str.isdigit(call)):
      print("정수를 입력하세요")
      return
    call = int(call)
    if (call == 0 or call > 3):
      print("1,2,3 중 하나를 입력하세요")
      return
  else:
    call = random.randint(1, 3)
  for _ in range(call):
    num+= 1
  
    print(f'{player1}: {num}') if isPlayer1Turn == True else print(f'{player2}: {num}')
    if num == 31:
      
      print(f'{player2} win!') if isPlayer1Turn == True else print(f'{player1} win!')
      return
    
  isPlayer1Turn = not isPlayer1Turn


    
  
    
    
  




while 1:

  brGame()

  if num == 31:
    break

  
  
