import argparse
import random 

parser = argparse.ArgumentParser()
parser.add_argument("--godmode", help="you always win", action="store_true")
parser.add_argument("--lose", help="you always lose", action="store_true")
args = parser.parse_args()
    
def gui():
    print '-' * 70
    print """
Welcome to the rock paper scissors game. You have to choose one
thing of three. 
Rules: 
rock--> beats scissors, lose with paper
paper--> beats rock, lose with scissors
scissors--> beats paper, lose with rock
\n\t\t\tgf&hf
"""
    print '-' * 70
            
def normal_game():
    rps = ['rock', 'paper', 'scissors']    
    play_again = 'y'    
             
    while play_again == 'y': 
        user_choice = raw_input("Please provide your choice >> ")
        user_choice = user_choice.lower()
        python = random.choice(rps)
        
        if user_choice[0] == python[0] :
            print "Tie!"
        elif user_choice[0] == 'r' and python[0] == 'p':
            print "Program choose paper, you lose!"
        elif user_choice[0] == 'r' and python[0] == 's':
            print "Program choose scissors, you win!"
        elif user_choice[0] == 'p' and python[0] == 'r':
            print "Program choose rock, you win!"
        elif user_choice[0] == 'p' and python[0] == 's':
            print "Program choose scissors, you lose!"
        elif user_choice[0] == 's' and python[0] == 'p':
            print "Program choose paper, you win!"
        elif user_choice[0] == 's' and python[0] == 'r':
            print "Program choose rock, you lose!"
             
        play_again = raw_input("Play again? (y/n) >> ")

def god():
    play_again = 'y'
    while play_again == 'y': 
        user_choice = raw_input("Please provide your choice >> ")
        user_choice = user_choice.lower()
        
        if user_choice[0] == 'r':
            print "Program choose scissors, you win!"
        elif user_choice[0] == 'p':
            print "Program choose rock, you win!"
        elif user_choice[0] == 's':
            print "Program choose paper, you win!"
            
        play_again = raw_input("Play again? (y/n) >> ")
    
def lost():
    play_again = 'y'
    while play_again == 'y': 
        user_choice = raw_input("Please provide your choice >> ")
        user_choice = user_choice.lower()
        
        if user_choice[0] == 'r':
            print "Program choose paper, you lose!"
        elif user_choice[0] == 'p':
            print "Program choose scissors, you lose!"
        elif user_choice[0] == 's':
            print "Program choose rock, you lose!"
            
        play_again = raw_input("Play again? (y/n) >> ")
    
if args.godmode:
    gui()
    god()
elif args.lose:
    gui()
    lost()   
else:
    gui()
    normal_game()
