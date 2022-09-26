import pygame
import sys as sus
import random as r
import RUN
#import unfair
#import noncence

money = 10
enters = 0
loop = True
c = pygame.time.Clock()
while loop:
  if money == 0:
    sus.quit('NO MONEY')
  input('\nGIVE ME YOUR MONEY \n' + 'you have ' + str(money) + ' left\n')
  money -= 1
  if r.randint(0,3) == 2:
    loop = False

print('accepted')
loop = True

while True:
  input('press enter')
  enters += 1 
  if r.randint(1,100) == 15:
    break

RUN.funsies()
