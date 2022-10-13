#1сеп
a=int(input("a="))
b=int(input("b="))
for i in range(a,b+1):
  print(i)

#2есеп
a=int(input("a="))
b=int(input("b="))
if a<=b:
  for i in range(a,b+1):
    print(i)
else:
  for i in range(a,b-1,-1):
    print(i)


#3есеп
# Берілген диапазонда тақ сандарды басып шығаруға арналған Python бағдарламасы
start, end = 1, 15
# тізімдегі әрбір санды қайталау
for num in range(start, end + 1):
  # тексеру шарты
  if num % 2 != 0:
    print(num, end=" ")

#4есеп
n = int(input()) #N-ге дейінгі сандары бар карталар 15
sum = 0
for i in range(1, n + 1): #1-ден 16-ға дейінгі
    sum += i  #sum = sum + i
for i in range(n - 1):  #15
    sum -= int(input()) #sum = sum - int(input())
print(sum) #Сумманы шығару
