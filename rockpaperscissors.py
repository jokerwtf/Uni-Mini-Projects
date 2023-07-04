pc_moves = "rrpssprpsppssprrs"
i = 0

while True:
    player_move = input("choose (r)ock, (s)cissors, (p)aper: ")
    if player_move == '': # Breaks the program if you hit enter
        break
    if player_move not in 'rps' :
        print("please input r, s or p")
    if player_move in 'rps':
        print('computer chose ' + pc_moves[i])
        i += 1 # Moves pc_moves by 1, meaning from 0,1,2,3 (string-wise) etc everytime you play
    if i == len(pc_moves):
        i = 0
    if player_move == pc_moves[i-1]:
        print("Tie")
    elif player_move == 'r':
        if pc_moves[i-1] == 's':
            print("You won!")
        else:
            print("You lost!")
    elif player_move == 's':
        if pc_moves[i-1] == 'p':
            print("You won!")
        else:
            print("You lost!")
    elif player_move == 'p':
        if pc_moves[i-1] == 'r':
            print("You won!")
        else:
            print("You lost!")
