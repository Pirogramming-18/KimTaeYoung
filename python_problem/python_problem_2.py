#함수 이름은 변경 가능합니다.

from collections import defaultdict

student_check = defaultdict(lambda : 0) # 학생의 존재 여부 체크
student_list = [] # 학생 리스트
student_score = defaultdict(list) # 중간고사 기말고사 점수
grade = defaultdict(lambda : "") # 학점 등급
graded_num = 0 # 현재 학점 등급을 받은 사람의 수



##############  menu 1
def Menu1(name, mid, final):

    student_check[name] = 1

    student_score[name].append(int(mid))
    student_score[name].append(int(final))

    student_list.append(name)

##############  menu 2
def Menu2(name, graded_num):
    graded_num += 1
    
    cur = student_score[name][0] + student_score[name][1] // 2

    if cur >= 90:
        grade[name] = 'A'
    elif cur >= 80:
        grade[name] = 'B'
    elif cur >= 70:
        grade[name] = 'C'
    else:
        grade[name] = 'D'

    
    return graded_num
    
##############  menu 3
def Menu3():
    print("name  mid  final  grade")
    print("--------------------------")

    for i in student_list:
        print(f'{i}   {student_score[i][0]}   {student_score[i][1]}   {grade[i]}')
    
    print("--------------------------")


##############  menu 4
def Menu4(name, graded_num):
    student_list.remove(name)
    graded_num -= 1
    student_check[name] = 0
    student_score[name].clear()
    grade[name] = ""
    print(f'{name} student information is delted.')

    return graded_num


print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":

        try: 
            name, mid_score, final_score = input("Enter name mid-score final-score :").split()
        except:
            print("Num of data is not 3!")
            continue
            
        name = name.strip() # 공백 문제

        if (student_check[name] == 1):
            print("Already Exist name!")
            continue

        if  not str.isdigit(mid_score) or not str.isdigit(final_score) or int(mid_score) <= 0 or int(final_score) <= 0:
            print("Score is not positive integer!")
            continue 
        
        Menu1(name, mid_score, final_score)

    elif choice == "2" :

        if len(student_list) == 0:
            print("No student data!")
            

        else:
            for i in student_list:
                if not grade[i]:
                
                    graded_num = Menu2(i, graded_num) # call by value
        
            print("Grading to all students.")


    elif choice == "3" :
        if len(student_list) == 0:
            print("No student data!")
            
        elif len(student_list) != graded_num:
            print("There is a student who didn't get grade")
        
        else:
            Menu3()

    elif choice == "4" :

        
        

        if len(student_list) == 0:
            print("No student data!")
            continue
        
        student_input = input("Enter the name to delete :").strip() 
        if (student_check[student_input] == 1):
            graded_num = Menu4(student_input, graded_num)
        
        else:
            print("Not exist name!")
            

    elif choice == "5" :
        print("Exit Program!")
        break

    else :
        print("Wrong number. Choose again.")