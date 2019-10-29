#BLACKJACK

#IMPORTS
import random

#GLOBALS
o = 0
p = []
d = []
md = []
win = 2
move = 0
t = 0
add= '123'

dealer_sum= 0
player_sum= 0

dv = []
pv = []
'''deck = [# 2  3  4  5  6  7  8  9  10  J   Q   K   A
          2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A',
          2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A',
          2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A',
          2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A',]
'''
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
deck = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']*4
values = {'One':1,'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,'Eleven':11, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
random.shuffle(deck)

#-----------------------------------------------------------------------------------------------------------------
def welcome():
    global o
    global suits
    global ranks
    global values
    global deck

    print('Welcome to BLACKJACK by Rohan Sharma\n')
    while True:
        try:
            ask = str.upper(input('Would You like to play the game? '))
            if ask == 'YES':
                o = 1
                #deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A',2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A',2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A',2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A',]
                deck = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']*4
                random.shuffle(deck)
                break
#                suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
#                ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
#                values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
            elif ask == 'NO':
                o = 0
                break
            else:
                print('Please enter Yes or No')
        except ValueError:
            print('Please enter Yes or No')
            
            
#-----------------------------------------------------------------------------------------------------------------
def give():
    global deck
    global p 
    global d
    global md
    global player_sum
    global dealer_sum
    global pv
    global dv
    global values

#DEALER
    d1=random.choice(deck)
    d2=random.choice(deck)
    d.append(d1)
    d.append(d2)
    for val_d in d:
        dv.append(values[val_d])
    
    md = d[1:]
    md.insert(0,'X')
    
    for id in dv:
        dealer_sum+=id
#PLAYER 
    p1=random.choice(deck)
    p2=random.choice(deck)
    p.append(p1)
    p.append(p2)
    for val_p in p:
        pv.append(values[val_p])
    for ip in pv:
        player_sum+=ip
    
    print('\nDealer has {} cards.\nYou have {} cards.\n{}\n'.format(md,p,player_sum))
            
            
#-----------------------------------------------------------------------------------------------------------------            
def turn():
    global t
    global p
    global d
    global move
    while True:
        t = str.upper(input('What whould you like to do, Hit or Stand? '))
        if t == 'HIT':
            move = 1
            break
        elif t== 'STAND':
            move = 2
            break
        else:
            print('Enter \'HIT\' or \'STAND\' only.\n')

#-----------------------------------------------------------------------------------------------------------------
def wincheck():
    global move
    global deck
    global values
    global player_sum
    global dealer_sum
    global win
    
    if player_sum>21:
        print('YOU LOST THE GAME!')
        win=0
    elif dealer_sum>21:
        print('YOU WON THE GAME!')
        win = 1
#-----------------------------------------------------------------------------------------------------------------
def calc():
    global deck
    global p
    global d
    global md
    global player_sum
    global dealer_sum
    global pv
    global dv
    global values
    
    dv = []
    pv=[]
    
    dealer_sum = 0
    player_sum = 0
    
    for id in d:
        dv.append(values[id])
    for ip in p:
        pv.append(values[ip])
        
    for ii in dv:
        dealer_sum+=ii
    for iv in pv:
        player_sum+=iv
#-----------------------------------------------------------------------------------------------------------------        
def ace():
    global add
    global pv
    if add == 'Ace':
        acea = int(input('Do you want to use Ace as 1 or 11?'))
        if acea == 1:
            p.append('One')
        elif acea == 11:
            p.append('Eleven')


#-----------------------------------------------------------------------------------------------------------------
def go():
    global o
    global win
    global move
    global deck
    global values
    global add
    global md
    
    welcome()
    if o ==0:
        print('Thanks for coming! Hope to see you again')
        
    else:
        give()
        wincheck()
        while win != 1 or win !=0:
            turn()
            if move ==1:
                add = random.choice(deck)
                if add == 'Ace':
                    ace()
                else:
                    p.append(add)
                    calc()
                    print('\nDealer has {} cards.\nYou have {} cards.\n{}\n'.format(md,p,player_sum))
                    wincheck()
                    if win==1 or win==0:
                        print('\nThe dealer had {} as the hidden card and a sum of {}.'.format(d[0],dealer_sum))
                        break
                    else:
                        continue
                    
            elif move ==2:
                add = random.choice(deck)
                d.append(add)
                md = d[1:]
                md.insert(0,'X')
                calc()
                wincheck()
                print('\nDealer has {} cards.\nYou have {} cards.\n{}\n'.format(md,p,player_sum))
                if win==1:
                    print('YOU WON THE GAME!')
                    print('\nThe dealer had {} as the hidden card and a sum of {}.'.format(d[0],dealer_sum))
                    print('The dealer got BUSTED')
                    break
                else:
                    pr = abs(21-player_sum)
                    dr = abs(21-dealer_sum)
                    if pr > dr:
                        print('YOU LOST THE GAME!\nDeler was Closer to 21 by {}!'.format(dr))
                        print('\nThe dealer had {} as the hidden card and a sum of {}.'.format(d[0],dealer_sum))
                        win =0
                        break
                    elif pr == dr:
                        print('THATS A DRAW!')
                        print('\nThe dealer had {} as the hidden card and a sum of {}.'.format(d[0],dealer_sum))
                        win = 0
                        break
                    else:
                        print('YOU WON THE GAME!\nYou were closer to 21 by {}.'.format(pr))
                        print('\nThe dealer had {} as the hidden card and a sum of {}.'.format(d[0],dealer_sum))
                        win = 1
                        break
                    
                    
                    
                        
#-----------------------------------------------------------------------------------------------------------------

if __name__=='__main__':
    go()