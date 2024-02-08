def display(slot):
    tic=f"|{slot[1]}|{slot[2]}|{slot[3]}|\n|{slot[4]}|{slot[5]}|{slot[6]}|\n|{slot[7]}|{slot[8]}|{slot[9]}|\n"
    print(tic)

def check_turn(turn):
    if(turn % 2 == 0):
        return 'X'
    else: return 'O'

def result(slot):
    if(slot[1]==slot[2]==slot[3]
       or slot[4]==slot[5]==slot[6]
       or slot[7]==slot[8]==slot[9]):
        return True
    elif(slot[1]==slot[4]==slot[7]
       or slot[2]==slot[5]==slot[8]
       or slot[3]==slot[6]==slot[9]):
        return True
    elif(slot[1]==slot[5]==slot[9]
       or slot[3]==slot[5]==slot[7]):
        return True
    else:
        return False
        
