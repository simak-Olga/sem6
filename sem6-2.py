#2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
stroka=input('Введите числа: ')
chisla = ['0','1','2','3','4','5','6','7','8','9']
operator = ['+','-','*','/']
# # for i in range(len(stroka))
# if i in chisla
# chislo_1 = int(i)
def calc(stroka):
  if stroka.find('+') >=0: 
    return calc(stroka[:stroka.find('+')]) + calc(stroka[stroka.find('+')+1:])
  if stroka.find('-') >=0: 
    return calc(stroka[:stroka.find('-')]) + calc(stroka[stroka.find('-')+1:])
  if stroka.find('*') >=0: 
    return calc(stroka[:stroka.find('*')]) + calc(stroka[stroka.find('*')+1:])
  if stroka.find('/') >=0: 
    return calc(stroka[:stroka.find('/')]) + calc(stroka[stroka.find('/')+1:])
  return int(stroka)
print(calc(stroka))
 