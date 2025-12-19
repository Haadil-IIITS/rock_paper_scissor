import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer=random.randint(0,2)
user=int(input("enter 0=rock,1=paper,2=scissor"))
print("user")
if(user==0):
    print(rock)
elif(user==1):
    print(paper)
else:
    print(scissors)
print("computer")
if(computer==0):
    print(rock)
elif(computer==1):
    print(paper)
else:
    print(scissors)
if(user>computer):
    if(user==2 and computer==0):
        print("u lose")
    else:
        print("u win")
elif(user==computer):
    print("draw")
else:
    if(user==0 and computer ==2):
        print("u win")
    else:
        print("u lose")
