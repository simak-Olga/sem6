from random import choice
import os
 
 
def clear(): return os.system('cls')
 
 
 
def GetInt(msg):
    try:
        turn_ind = int(input(msg))
        if turn_ind in range(1, max_num + 1):
            return turn_ind
        else:
            return GetInt(msg)
    except:
        return GetInt(msg)
 
 
def PrintArr(arr):
    m = len(arr[0])
    n = len(arr)
    print("╔═══" + ("══╤═══" * (m - 1)) + "══╗")
    for i in range(n):
        print("║  " + "  │  ".join(arr[i]) + "  ║")
        if i != n - 1:
            print("╟───" + ("──┼───" * (m - 1)) + "──╢")
    print("╚═══" + ("══╧═══" * (m - 1)) + "══╝")
 
 
def CalcPos(table, num):
    x = num // len(table[0])
    y = num % len(table[0])
    return x, y
 
 
def Turn(table):
    pos = GetInt(f"На какую позицию ходить? ")
    x, y = CalcPos(table, pos - 1)
    if not table[x][y].isdigit():
        print("Сюда сходить нельзя!")
        Turn(table)
    else:
        table[x][y] = "X"
    return table
 
 
def BotTurn(table):
 
    while 1:
        pos = choice(GetAvailTurns(table))
        x, y = CalcPos(table, pos - 1)
        table[x][y] = 'O'
        return table
 
 
def GetAvailTurns(table):
    avail_turns = []
    for i in table:
        for j in filter(lambda z: z.isdigit(), i):
            if j:
                avail_turns.append(int(j))
    return avail_turns
 
 
def CheckLines(table):
    count1 = count2 = count3 = count4 = 0
    for i in range(m):
        if table[i][-i - 1] == "X":
            count1 += 1
        if table[i][i] == "X":
            count2 += 1
        if table[i].count("X") == m or count1 == m or count2 == m:
            return 1
 
        if table[i][-i - 1] == "O":
            count3 += 1
        if table[i][i] == "O":
            count4 += 1
        if table[i].count("O") == m or count3 == m or count4 == m:
            return 2
 
    return 0
 
 
def CheckState(table):
    clear()
    PrintArr(table)
    rot_table = list(zip(*table[::-1]))
    cl1 = CheckLines(table)
    cl2 = CheckLines(rot_table)
    if cl1 == 1 or cl2 == 1:
        print("Побеждает игрок!")
        return 0
    elif cl1 == 2 or cl2 == 2:
        print("Побеждает бот!")
        return 0
 
    if not GetAvailTurns(table):
        print("Конец игры!")
        return 0
 
    return 1
 
 
m = n = 3
max_num = m * n
 
table = []
i = 1
for _ in range(n):
    t = []
    for _ in range(m):
        t.append(str(i))
        i += 1
    table.append(t)
 
PrintArr(table)
 
while 1:
    BotTurn(table)
    if not CheckState(table):
        break
 
    Turn(table)
    if not CheckState(table):
        break