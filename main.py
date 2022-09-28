import pygame
import sys as sus
import random as r
import RUN
import time as t
#import unfair
#import noncence

pygame.init()
money = 20
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

while loop:
  if money == 0:
    sus.stop('NO MONEY')
  input('\nGIVE ME YOUR MONEY \n' + 'you have ' + str(money) + ' left\n')
  money -= 1
  if r.randint(0,3) == 2:
    loop = False

print('here\'s no money')
money -= 2
if money <=0:
    sus.stop('NO MONEY')
t.sleep(5)
print('and taxes')

money -= 2
if money <=0:
    sus.stop('NO MONEY')

w = pygame.display.set_mode([40, 40])

rick = pygame.image.load('unnamed.gif')

for i in range(100):
  w.blit(rick,(0,0))
  pygame.display.flip()
  pygame.time.wait(10)

