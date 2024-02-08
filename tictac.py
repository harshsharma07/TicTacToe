from helper import display,check_turn,result

slot={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
#display(slot)
turn = 0
playing = True
complete=False
prev_turn=-1
while playing:
    if prev_turn==turn:
        print("Invalid spot, please select again!")
    prev_turn=turn    
    player=(turn%2)+1
    print(f"Player {player}'s turn, please select your choice, or q to quit ")
    choice = input("Enter your choice: ")
    if(choice == 'q'): 
        playing=False
        print(f"Player {player} has quit the game, Bye! ")
    elif int(choice) in slot and str.isdigit(choice):
        if not slot[int(choice)] in ('X','O'):
            ch=check_turn(turn)
            slot[int(choice)]= ch
            display(slot)
            turn+=1
    if result(slot): 
        playing=False
        complete=True
    if(turn>8):playing=False
    
if complete:
    if check_turn(turn)=='X':
        print("Player 2 wins the game! wuhuuu")
    else:
        print("Player 1 wins the game! wuhuuu")
else:
    print("Game tied!")
           

print("Thanks for playing! Feel free to play again")
                         
            