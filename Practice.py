import math


testContainer = ["test", "hello", "myWorld"]

# While 반복문.
index = 5
while index >= 1:
    print("index : " + str(index))
    index -= 1

# 컨테이너 사용법.
for testValue in testContainer:
    print(testValue)

def TestFuntion(userName):
     print("UserName : " + userName)
     radian = 0.0
     while(radian <= 1.0):
          print("cos value : " + str(math.cos(radian)))
          radian += 0.1
    
    

TestFuntion("opk4406")

