import random

options=['R','P','S']

def player_select():
    player=input('Choose R for rock, P for paper or S for scissors \n').upper()
    if player in ['R','P','S']:
        player=='R'
    elif player in ['R','P','S']:
        player=='P'
    elif player in ['R','P','S']:
        player=='S'
    else:
        print('invalid choice try again')
    return player

def computer_select():
    computer=random.choice(options)
    return computer

while True:
    player=player_select()
    computer=computer_select()
    if player == 'R':
        print('player(Rock)')
        if computer == 'R':
            print('computer(Rock)')
            print('Tie try again')
            continue
        elif computer == 'P':
            print('computer(Paper)')
            print('computer wins paper beats rock')
            break
        elif computer == 'S':
            print('computer(Scissors)')
            print('player wins rock beats scissors')
            break
    if player == 'P':
        print('player(Paper)')
        if computer == 'R':
            print('computer(Rock)')
            print('player wins paper beats rock')
            break
        elif computer == 'P':
            print('computer(Paper)')
            print('Tie try again')
            continue
        elif computer == 'S':
            print('computer(Scissors)')
            print('computer wins scissors beats paper')
            break
    if player == 'S':
        print('player(Scissors)')
        if computer == 'R':
            print('computer(Rock)')
            print('computer wins rock beats scissors')
            break
        elif computer == 'P':
            print('computer(Paper)')
            print('player wins scissors beats paper')
            break
        elif computer == 'S':
            print('computer(Scissors)')
            print('Tie try again')
            continue
    
        
   
            
            
     
    
        
        
