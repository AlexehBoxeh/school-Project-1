import time
import os
import subprocess
import random
import json

p1score = 0
p2score = 0
y = ''
correcty = 'Password'
repeat = True
player1 = ''
player2 = ''

def fetchData(filename='leaderboard.json'):
    if os.stat(filename).st_size == 0:
        return []
    with open(filename) as f:
        return json.load(f)

def diceroll():
  return random.randint(1, 6)

def clear():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n" * 120)

def login(password, reqpassword):
  if password == reqpassword:
    clear()
    print ("Access granted")
    return False
  else:
    print ("Try again!")
    time.sleep(1)
    clear()
    return True
  if repeat != False:
    print ("Try again!")

while  repeat:
  player1 = input("Whats Player 1's username?\n")
  player2 = input("Whats Player 2's username?\n")
  Password = input("Whats the password?\n")
  repeat = login(Password, correcty)

print ("Welcome to the dice game!!!")
time.sleep(2)
clear()
g = float(input("How long of pause do you want between rounds?\n"))
for x in range (1, 5):
  clear()
  roll11 = diceroll()
  roll12 = diceroll()
  roll21 = diceroll()
  roll22= diceroll()
  double1 = diceroll()
  double2 = diceroll()
  print ("Round ",x,". p1 rolled", roll11," and ",roll12, ". p2 rolled", roll21, " and ", roll22)
  if roll21 == roll22:
    print ("P2 rolled doubles! Their Extra die got them", double2)
    p2score += double2
  if roll11 == roll12:
    print ("P1 rolled doubles! Their Extra die got them", double1)
    p1score += double1
  p1score += roll11 + roll12
  p2score += roll21 + roll22
  if p1score % 2 == 0:
    p1score += 10
  else:
    p1score -= 5
  if p2score % 2 == 0:
    p2score += 10
  else:
    p2score -= 5
  if p1score < 0:
    p1score -= p1score
  if p2score < 0:
    p2score -= p2score
  print ("The scores are currently at\np1:",p1score, "\np2:", p2score)
  time.sleep(g)
  clear()
if p1score > p2score:
  print ("The game has concluded, P1 wins!\nScores were: p1:",p1score,"  p2:",p2score)
  newDict = {}
  newDict['Name']= player1
  newDict['score']= p1score
  newStuff = fetchData()
  newStuff.append(newDict)
  with open('leaderboard.json','w') as f:
    f.write(json.dumps(newStuff))
elif p2score > p1score:
  print ("The game has concluded, P2 wins!\nScores were: p1:",p1score,"  p2:",p2score)
  newDict = {}
  newDict['Name']= player2
  newDict['score']= p2score
  newStuff = fetchData()
  newStuff.append(newDict)
  with open('leaderboard.json','w') as f:
    f.write(json.dumps(newStuff))
else:
  clear()
  print ("The game has concluded, It was a draw! You will each roll 1 die to see who wins")
  while p1score == p2score:
    finroll1 = diceroll()
    finroll2 = diceroll()
    print ("p1 rolled",finroll1,"\np2 rolled", finroll2)
    p1score += finroll1
    p2score += finroll2
    print ("The scores are currently at\np1: ",p1score, "\np2:", p2score)
    if p1score > p2score:
      print ("The game has concluded, P1 wins!")
      newDict = {}
      newDict['Name']= player1
      newDict['score']= p1score
      newStuff = fetchData() 
      newStuff.append(newDict)
      with open('leaderboard.json','w') as f:
        f.write(json.dumps(newStuff))
    elif p2score > p1score:
      print ("The game has concluded, P2 wins!")
      newDict = {}
      newDict['Name']= player2
      newDict['score']= p2score
      newStuff = fetchData() 
      newStuff.append(newDict)
      with open('leaderboard.json','w') as f:
        f.write(json.dumps(newStuff))
    else:
      print ("Draw again. Roll again.")
      
leaderboard = fetchData()
leaderboard.sort(key = lambda dog:dog['score'],reverse = True)

count = 1

for x in leaderboard[:5]:
  name = x['Name']
  score = x['score']
  print (count, '.', name, "achieved a score of: ", score)
  count += 1
  time.sleep(0.5)