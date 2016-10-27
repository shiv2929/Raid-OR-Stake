def main(in_file,N):
    from collections import OrderedDict

    col_max = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    row_max = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    cutoff = 0


    import copy


    frontier=[]

    #*******************************for iterative minimax approach*****************************************************
    def minimax(board,player,depth,N,curr_stake_keys,curr_raid_keys,cutoff,frontier,game_state,player_1,player_2):
        c_u_t = OrderedDict()
        count = 0

        #cutoff = cutoff +1
        current_player = player

        while len(frontier)!=0:




            if cutoff<=depth:

                board_to_expand=frontier.pop(0)

                #cutoff = cutoff + 1
                frontier_queue = []
                # frontier.append(board)

                num = 1
                #******* To obtain what cells can be used for raiding and staking**********************
                action(board_to_expand, current_player, N, curr_stake_keys, curr_raid_keys)  # taking up stake and raid node lists

                while (len(curr_stake_keys) != 0):
                    #print(num)


                    curr_board = copy.deepcopy(board_to_expand)
                    play = curr_stake_keys.pop(0)

                    # *******Stake Moves******stake is possible at all positions

                    for keys in curr_board:
                        if list(keys) == play:
                            curr_board[keys] = [curr_board[keys][0], current_player, "Stake"]  # played first stake
                            #print("Board Num-", num, curr_board)
                            frontier_queue.append(curr_board)

                            # *******raid only from raid positions*****
                            # if play in curr_raid_keys:
                            # raid(curr_board)
                            # pass
                            num = num + 1

                    #***************Raid Moves****************
                while len(curr_raid_keys)!= 0:



                    curr_board_raid = copy.deepcopy(board_to_expand)

                    play_raid = curr_raid_keys.pop(0)

                    """******** If other player's pawn is touching current player's pawn then the other player's pawn
                    can be captured********************"""
                    for keys in curr_board_raid:
                        if list(keys) == play_raid:

                            #****Checking Corners*****

                            if ((play_raid[0]=="A" or play_raid[0] == col_max[N-1])and (play_raid[1]==N or play_raid[1]==1)):
                                if play_raid[0]=="A" and play_raid[1]==1:


                                    if curr_board_raid["B",1][1]!= current_player and curr_board_raid["B",1][1]!=".":
                                        curr_board_raid["B",1][1] = current_player
                                    if curr_board_raid["A",2][1]!=current_player and curr_board_raid["A",2][1]!=".":
                                        curr_board_raid["A",2][1] = current_player
                                    # ("left top corner")

                                elif play_raid[0]=="A" and play_raid[1]==N:
                                    if curr_board_raid["B", N][1] != current_player and curr_board_raid["B", N][1] != ".":
                                        curr_board_raid["B", N][1] = current_player
                                    if curr_board_raid["A", N-1][1] != current_player and curr_board_raid["A", N-1][1] != ".":
                                        curr_board_raid["A", N-1][1] = current_player
                                    #("left bottom corner")

                                elif play_raid[0]==col_max[N-1] and play_raid[1]==1:
                                    if curr_board_raid[col_max[N-2], 1][1] != current_player and curr_board_raid[col_max[N-2], 1][1] != ".":
                                        curr_board_raid[col_max[N-2], 1][1] = current_player
                                    if curr_board_raid[col_max[N-1], 1][1] != current_player and curr_board_raid[col_max[N-1], 1][1] != ".":
                                        curr_board_raid[col_max[N-1], 1][1] = current_player
                                    #("right up corner")

                                elif play_raid[0]==col_max[N-1] and play_raid[1]==N:
                                    if curr_board_raid[col_max[N-2], N][1] != current_player and curr_board_raid[col_max[N-2], N][1] != ".":
                                        curr_board_raid[col_max[N-2], N][1] = current_player
                                    if curr_board_raid[col_max[N-1], N-1][1] != current_player and curr_board_raid[col_max[N-1], N-1][1] != ".":
                                        curr_board_raid[col_max[N-1], N-1][1] = current_player
                                    #("right bottom corner")

                            #********checking edges, would exclude corners, since they would already be checked***********
                            elif (play_raid[0] == "A" or play_raid[0]==col_max[N-1]) and (play_raid[1]!=N or play_raid[1]!=1):
                                if play_raid[0]== "A":
                                    if curr_board_raid["A",play_raid[1]-1][1]!= "." and curr_board_raid["A",play_raid[1]-1][1]!=current_player:
                                        curr_board_raid["A",play_raid[1]-1][1] = current_player
                                    if curr_board_raid["A",play_raid[1]+1][1]!= "." and curr_board_raid["A",play_raid[1]+1][1]!=current_player:
                                        curr_board_raid["A", play_raid[1]+1][1] = current_player
                                    if curr_board_raid["B", play_raid[1]][1]!="." and curr_board_raid["B", play_raid[1]][1]!=current_player:
                                        curr_board_raid["B",play_raid[1]][1]= current_player
                                    #("raid pos on left edge")

                                elif play_raid[0]== col_max[N-1]:
                                    if curr_board_raid[col_max[N-1],play_raid[1]-1][1]!= "." and curr_board_raid[col_max[N-1],play_raid[1]-1][1]!= current_player:
                                        curr_board_raid[col_max[N-1],play_raid[1]-1][1] = current_player
                                    if curr_board_raid[col_max[N-1],play_raid[1]+1][1]!= "." and curr_board_raid[col_max[N-1],play_raid[1]+1][1]!= current_player:
                                        curr_board_raid[col_max[N-1], play_raid[1]+1][1] = current_player
                                    if curr_board_raid[col_max[N-2], play_raid[1]][1]!="." and curr_board_raid[col_max[N-2], play_raid[1]][1]!=current_player:
                                        curr_board_raid[col_max[N-2],play_raid[1]][1]= current_player
                                    #("raid right edge")

                            elif ((play_raid[0]!="A" and play_raid[0]!=col_max[N-1])and (play_raid[1]==N or play_raid[1]==1)):
                                if play_raid[1]==1:
                                    a=col_max.index(play_raid[0])


                                    if curr_board_raid[col_max[a-1],play_raid[1]][1]!= "." and curr_board_raid[col_max[a-1],play_raid[1]][1]!=current_player:
                                        curr_board_raid[col_max[a-1],play_raid[1]][1] = current_player
                                    if curr_board_raid[col_max[a+1],play_raid[1]][1]!= "." and curr_board_raid[col_max[a+1],play_raid[1]][1]!= current_player:
                                        curr_board_raid[col_max[a+1], play_raid[1]][1] = current_player
                                    if curr_board_raid[play_raid[0], play_raid[1]+1][1]!="." and curr_board_raid[play_raid[0], play_raid[1]+1][1]!=current_player:
                                        curr_board_raid[play_raid[0],play_raid[1]+1][1]= current_player
                                    #("top edge raid")

                                elif play_raid[1]== N:
                                    b= col_max.index(play_raid[0])
                                    if curr_board_raid[col_max[b - 1], play_raid[1]][1] != "." and curr_board_raid[col_max[b - 1], play_raid[1]][1] != current_player:
                                        curr_board_raid[col_max[b - 1], play_raid[1]][1] = current_player
                                    if curr_board_raid[col_max[b + 1], play_raid[1]][1]!= "." and curr_board_raid[col_max[b + 1], play_raid[1]][1]!= current_player:
                                        curr_board_raid[col_max[b + 1], play_raid[1]][1] = current_player
                                    if curr_board_raid[play_raid[0], play_raid[1] - 1][1] != "." and curr_board_raid[play_raid[0], play_raid[1] - 1][1] != current_player:
                                        curr_board_raid[play_raid[0], play_raid[1] - 1][1] = current_player
                                    #("bottom edge raid")

                            else:
                                c=col_max.index(play_raid[0])
                                if curr_board_raid[col_max[c - 1], play_raid[1]][1] != "." and curr_board_raid[col_max[c - 1], play_raid[1]][1] != current_player:
                                    curr_board_raid[col_max[c - 1], play_raid[1]][1] = current_player
                                if curr_board_raid[col_max[c + 1], play_raid[1]][1]!= "." and curr_board_raid[col_max[c + 1], play_raid[1]][1]!=current_player:
                                    curr_board_raid[col_max[c + 1], play_raid[1]][1] = current_player
                                if curr_board_raid[play_raid[0], play_raid[1] - 1][1] != "." and curr_board_raid[play_raid[0], play_raid[1] - 1][1] != current_player:
                                    curr_board_raid[play_raid[0], play_raid[1] - 1][1] = current_player
                                if curr_board_raid[play_raid[0], play_raid[1] + 1][1]!= "." and curr_board_raid[play_raid[0], play_raid[1] + 1][1]!=current_player:
                                    curr_board_raid[play_raid[0], play_raid[1] + 1][1] = current_player

                            #****** Updating Board after raiding capturing other player's pawn********
                            curr_board_raid[keys] = [curr_board_raid[keys][0], current_player, "Raid"]
                            frontier_queue.append(curr_board_raid)








                            num = num + 1
                cutoff=cutoff+1

                #z=OrderedDict()

                #(frozenset(board_to_expand))

                #******** Making a dictionary which has cutoff as key and boards as values at that level******
                if cutoff not in game_state.keys():
                    game_state[cutoff] = [frontier_queue]

                elif cutoff in game_state.keys():
                    game_state[cutoff].append(frontier_queue)

                if cutoff < depth:
                    for elements in range(len(frontier_queue)):
                        frontier.insert(elements,frontier_queue[elements])  # add new boards to frontier

                    if current_player == "X":
                        current_player = "O"
                    elif current_player == "O":
                        current_player = "X"



                elif cutoff == depth:
                    last_updated_cutoff = cutoff

                    #************MIN OR MAX********************
                    if cutoff%2 == 0:
                        v_old = 10000000000000000000000000000
                        for element_1 in frontier_queue:
                            board = element_1
                            v = utility(board,player_1,player_2)

                            v = min(v,v_old)
                            v_old = v
                    elif cutoff % 2 != 0:
                        v_old = -100000000000000000000000
                        for element_2 in frontier_queue:
                            board = element_2
                            v = utility(board, player_1,player_2)
                            v = max(v,v_old)
                            v_old = v

                    #********cutoff updation to new nodes*********
                    if len(frontier)== 0:
                        cutoff = 1
                    elif len(frontier)!=0:
                        for keys in game_state:
                            if keys == 0:
                                element = base_board
                            elif keys == 1:
                                for element in game_state[keys]:
                                    for p in element:

                                        if p == frontier[0]:
                                            cutoff = 1
                            else:

                                for element in game_state[keys]:
                                    for p in element:

                                        if p == frontier[0]:
                                            cutoff=keys

                    if cutoff % 2 != 0:
                        current_player = player_2
                    elif cutoff % 2 == 0:
                        current_player = player_1

                    if cutoff == (last_updated_cutoff - 1):
                        if cutoff not in c_u_t.keys():
                            c_u_t[cutoff] = [v]
                        elif cutoff in c_u_t.keys():
                            c_u_t[cutoff].append(v)     #appends values to the initial list

                    elif (cutoff != (last_updated_cutoff- 1)):
                        if (last_updated_cutoff - 1) in c_u_t.keys():
                            c_u_t[last_updated_cutoff-1].append(v)
                        elif last_updated_cutoff - 1 not in c_u_t.keys():
                            c_u_t[last_updated_cutoff - 1] = [v]

                        for keyz in range(last_updated_cutoff-1, cutoff, -1):
                            if keyz %2 != 0:
                                value = max(c_u_t[keyz])
                            elif keyz %2 == 0:
                                value = min(c_u_t[keyz])

                            if (keyz-1) not in c_u_t.keys():
                                c_u_t[keyz-1] = [value]
                            elif (keyz-1) in c_u_t.keys():
                                c_u_t[keyz-1].append(value)
                            del c_u_t[keyz]

                                #update player

                count = count + 1


        #print(c_u_t)
        #print(c_u_t[1].index(max(c_u_t[1])),"index")
        final_val = c_u_t[1].index(max(c_u_t[1]))
        Game = sum(game_state[1],[])

        #print(len(c_u_t[1]),"len cut")
        out_file.write("game state")

        #out_file.write(str(len(game_state[2]))+'\n')
        #out_file.write((str(len(game_state[1]))))

        #out_file.write(str(game_state)+'\n')
        #out_file.write(str(len(game_state[2])))
        #for keys in game_tree:
            #out_file.write(str(keys)+'\n')

        #actual_minmax(game_state,depth,player_1,player_2)
        #print("check program")


#*********************** MAKING NEW BOARDS- For MiniMax and Alpha Beta recursive approach**************
    def make_new_boards(board,player):

        board_to_expand = copy.deepcopy(board)
        current_player = player
        action(board_to_expand, current_player, N, curr_stake_keys, curr_raid_keys)

        frontier_queue=[]
        num = 0

        # while len(curr_stake_keys)!=0:
        while (len(curr_stake_keys) != 0):


            curr_board = copy.deepcopy(board_to_expand)
            play = curr_stake_keys.pop(0)

            # *******Stake Moves******stake possible at all positions

            for keys in curr_board:
                if list(keys) == play:
                    curr_board[keys] = [curr_board[keys][0], current_player, "Stake"]  # played first stake
                    #print("Board Num-",num, curr_board)
                    frontier_queue.append(curr_board)
                    num = num + 1

# ************Raid Moves - only possible from raid cells, checking if any adjacent other player's pawn exist********
# ***********If enemy pawn exists then, changing it to current player**********
        while len(curr_raid_keys) != 0:



            curr_board_raid = copy.deepcopy(board_to_expand)
            play_raid = curr_raid_keys.pop(0)

            for keys in curr_board_raid:
                if list(keys) == play_raid:


                    if ((play_raid[0] == "A" or play_raid[0] == col_max[N - 1]) and (
                            play_raid[1] == N or play_raid[1] == 1)):
                        if play_raid[0] == "A" and play_raid[1] == 1:
                            #("left top corner")
                            if curr_board_raid["B", 1][1] != current_player and curr_board_raid["B", 1][1] != ".":
                                curr_board_raid["B", 1][1] = current_player
                            if curr_board_raid["A", 2][1] != current_player and curr_board_raid["A", 2][1] != ".":
                                curr_board_raid["A", 2][1] = current_player


                        elif play_raid[0] == "A" and play_raid[1] == N:
                            if curr_board_raid["B", N][1] != current_player and curr_board_raid["B", N][1] != ".":
                                curr_board_raid["B", N][1] = current_player
                            if curr_board_raid["A", N - 1][1] != current_player and curr_board_raid["A", N - 1][1] != ".":
                                curr_board_raid["A", N - 1][1] = current_player

                                #("left bottom corner")
                        elif play_raid[0] == col_max[N - 1] and play_raid[1] == 1:
                            if curr_board_raid[col_max[N - 2], 1][1] != current_player and \
                                            curr_board_raid[col_max[N - 2], 1][1] != ".":
                                curr_board_raid[col_max[N - 2], 1][1] = current_player
                            if curr_board_raid[col_max[N - 1], 2][1] != current_player and \
                                            curr_board_raid[col_max[N - 1], 2][1] != ".":
                                curr_board_raid[col_max[N - 1], 2][1] = current_player
                                #("right up corner")
                        elif play_raid[0] == col_max[N - 1] and play_raid[1] == N:
                            if curr_board_raid[col_max[N - 2], N][1] != current_player and \
                                            curr_board_raid[col_max[N - 2], N][1] != ".":
                                curr_board_raid[col_max[N - 2], N][1] = current_player
                            if curr_board_raid[col_max[N - 1], N - 1][1] != current_player and \
                                            curr_board_raid[col_max[N - 1], N - 1][1] != ".":
                                curr_board_raid[col_max[N - 1], N - 1][1] = current_player
                                #("right bottom corner")

                    # ******checking edges********
                    elif (play_raid[0] == "A" or play_raid[0] == col_max[N - 1]) and (
                            play_raid[1] != N or play_raid[1] != 1):
                        if play_raid[0] == "A":
                            if curr_board_raid["A", play_raid[1] - 1][1] != "." and curr_board_raid["A", play_raid[1] - 1][
                                1] != current_player:
                                curr_board_raid["A", play_raid[1] - 1][1] = current_player
                            if curr_board_raid["A", play_raid[1] + 1][1] != "." and curr_board_raid["A", play_raid[1] + 1][
                                1] != current_player:
                                curr_board_raid["A", play_raid[1] + 1][1] = current_player
                            if curr_board_raid["B", play_raid[1]][1] != "." and curr_board_raid["B", play_raid[1]][
                                1] != current_player:
                                curr_board_raid["B", play_raid[1]][1] = current_player

                                #("raid pos on left edge")

                        elif play_raid[0] == col_max[N - 1]:
                            if curr_board_raid[col_max[N - 1], play_raid[1] - 1][1] != "." and \
                                            curr_board_raid[col_max[N - 1], play_raid[1] - 1][1] != current_player:
                                curr_board_raid[col_max[N - 1], play_raid[1] - 1][1] = current_player
                            if curr_board_raid[col_max[N - 1], play_raid[1] + 1][1] != "." and \
                                            curr_board_raid[col_max[N - 1], play_raid[1] + 1][1] != current_player:
                                curr_board_raid[col_max[N - 1], play_raid[1] + 1][1] = current_player
                            if curr_board_raid[col_max[N - 2], play_raid[1]][1] != "." and \
                                            curr_board_raid[col_max[N - 2], play_raid[1]][1] != current_player:
                                curr_board_raid[col_max[N - 2], play_raid[1]][1] = current_player
                                #("raid right edge")

                    elif ((play_raid[0] != "A" and play_raid[0] != col_max[N - 1]) and (
                            play_raid[1] == N or play_raid[1] == 1)):
                        if play_raid[1] == 1:
                            a = col_max.index(play_raid[0])

                            if curr_board_raid[col_max[a - 1], play_raid[1]][1] != "." and \
                                            curr_board_raid[col_max[a - 1], play_raid[1]][1] != current_player:
                                curr_board_raid[col_max[a - 1], play_raid[1]][1] = current_player
                            if curr_board_raid[col_max[a + 1], play_raid[1]][1] != "." and \
                                            curr_board_raid[col_max[a + 1], play_raid[1]][1] != current_player:
                                curr_board_raid[col_max[a + 1], play_raid[1]][1] = current_player
                            if curr_board_raid[play_raid[0], play_raid[1] + 1][1] != "." and \
                                            curr_board_raid[play_raid[0], play_raid[1] + 1][1] != current_player:
                                curr_board_raid[play_raid[0], play_raid[1] + 1][1] = current_player

                                #("top edge raid")
                        elif play_raid[1] == N:
                            b = col_max.index(play_raid[0])
                            if curr_board_raid[col_max[b - 1], play_raid[1]][1] != "." and \
                                            curr_board_raid[col_max[b - 1], play_raid[1]][1] != current_player:
                                curr_board_raid[col_max[b - 1], play_raid[1]][1] = current_player
                            if curr_board_raid[col_max[b + 1], play_raid[1]][1] != "." and \
                                            curr_board_raid[col_max[b + 1], play_raid[1]][1] != current_player:
                                curr_board_raid[col_max[b + 1], play_raid[1]][1] = current_player
                            if curr_board_raid[play_raid[0], play_raid[1] - 1][1] != "." and \
                                            curr_board_raid[play_raid[0], play_raid[1] - 1][1] != current_player:
                                curr_board_raid[play_raid[0], play_raid[1] - 1][1] = current_player

                                #("bottom edge raid")
                    else:
                        c = col_max.index(play_raid[0])
                        if curr_board_raid[col_max[c - 1], play_raid[1]][1] != "." and \
                                        curr_board_raid[col_max[c - 1], play_raid[1]][1] != current_player:
                            curr_board_raid[col_max[c - 1], play_raid[1]][1] = current_player
                        if curr_board_raid[col_max[c + 1], play_raid[1]][1] != "." and \
                                        curr_board_raid[col_max[c + 1], play_raid[1]][1] != current_player:
                            curr_board_raid[col_max[c + 1], play_raid[1]][1] = current_player
                        if curr_board_raid[play_raid[0], play_raid[1] - 1][1] != "." and \
                                        curr_board_raid[play_raid[0], play_raid[1] - 1][1] != current_player:
                            curr_board_raid[play_raid[0], play_raid[1] - 1][1] = current_player
                        if curr_board_raid[play_raid[0], play_raid[1] + 1][1] != "." and \
                                        curr_board_raid[play_raid[0], play_raid[1] + 1][1] != current_player:
                            curr_board_raid[play_raid[0], play_raid[1] + 1][1] = current_player

                    curr_board_raid[keys] = [curr_board_raid[keys][0], current_player, "Raid"]
                    frontier_queue.append(curr_board_raid)
        return frontier_queue       # new boards updated in the queue


#************** Calculation of total game score while function reaches leaf nodes*************
    def utility (leaf_board,player_1,player_2):

        score = 0
        sum_player_1 = 0
        sum_player_2 = 0
        m =  leaf_board

        for keys in leaf_board:

            if leaf_board[keys][1] != ".":
                if leaf_board[keys][1]== player_1:
                    sum_player_1 = sum_player_1 + leaf_board[keys][0]

                elif leaf_board[keys][1] == player_2:
                    sum_player_2 = sum_player_2 + leaf_board[keys][0]

        score = sum_player_1-sum_player_2   #score = current player - other player

        return score

# **************************************** RECURSIVE APPROACH TO MIIMAX ************************************************

    def MINIMAXX(board,depth,player_1,player_2,cutoff):
        game={}
        a_list=[]
        b_list=[]
        v=max_value_MIN(board,cutoff,depth,player_1,game,a_list,b_list)

        k = game[a_list[0]][0]

        for fot in k:
            if len(k[fot])!=2:

                #Writing data to the output File - Program_Output.txt
                out_file.write(str(fot[0]))
                out_file.write(str(fot[1]))
                out_file.write(str(" "))
                out_file.write(str(k[fot][2]))

        count_final = 0
        for fot_2 in k:

            if count_final % N ==0:
                out_file.write('\n')
            out_file.write(str(k[fot_2][1]))
            count_final = count_final +1

    # **********MAX function of MiniMax***************
    def max_value_MIN(board,cutoff,depth,player,game,a_list,b_list):
        player = player_1


        if cutoff ==depth:
            score = utility(board, player_1, player_2)
            return score


        else:
            cutoff = cutoff+1
            v=-1000000000000000000000000
            F_Q=make_new_boards(board,player)
            for i in F_Q:
                interim_1 = min_value_MIN(i,cutoff,depth,player,game,a_list,b_list)
                v= max(v,interim_1)

                if cutoff == 1:
                    if v in game.keys():
                        game[v].append(i)
                    else:
                        game[v] = [i]
                    a_list.insert(0,v)


            return v

    # **********MIN function of MiniMax***************
    def min_value_MIN(board,cutoff,depth,player,game,a_list,b_list):
        player = player_2
        if cutoff == depth:
            score = utility(board,player_1,player_2)

            return score
            #goto utility
        else:
            cutoff = cutoff +1
            v=10000000000000000000000000
            f_q = make_new_boards(board,player)
            for j in f_q:
                interim_2 = max_value_MIN(j,cutoff,depth,player,game,a_list,b_list)
                v= min(v,interim_2)
            return v


#**************************Recursive Alpha-Beta Approach*****************************

    def alphabeta(board, alpha, beta, depth, player_1, player_2, cutoff):
        game = {}
        a_list = []
        b_list = []
        v = max_value(board, alpha, beta, cutoff, depth, player_1, game, a_list, b_list)
        # print(v)

        # print(a_list[0])

        #print(game[a_list[0]][0])
        k = game[a_list[0]][0]

        for fot in k:
            if len(k[fot]) != 2:
                # print(fot)
                # print(fot[0])
                out_file.write(str(fot[0]))
                out_file.write(str(fot[1]))
                out_file.write(str(" "))
                out_file.write(str(k[fot][2]))
                # print(fot[1])
        count_final = 0
        for fot_2 in k:

            if count_final % N == 0:
                out_file.write('\n')
            out_file.write(str(k[fot_2][1]))
            count_final = count_final + 1

    def max_value(board, alpha, beta, cutoff, depth, player, game, a_list, b_list):
        player = player_1

        if cutoff == depth:
            score = utility(board, player_1, player_2)
            return score

            # goto utility

        else:
            cutoff = cutoff + 1
            v = -1000000000000000000000000
            F_Q = make_new_boards(board, player)
            for i in F_Q:
                interim_1 = min_value(i, alpha, beta, cutoff, depth, player, game, a_list, b_list)
                v = max(v, interim_1)

                if v >= beta:

                    break
                else:
                    alpha = max(alpha, v)
                    # print("it is cutoff", cutoff)
                    # print(alpha,"alpha")
                    # print(i)
                    if cutoff == 1:
                        if alpha in game.keys():
                            game[alpha].append(i)
                        else:
                            game[alpha] = [i]

                    a_list.insert(0, alpha)

            return v

    def min_value(board, alpha, beta, cutoff, depth, player, game, a_list, b_list):
        player = player_2
        if cutoff == depth:
            score = utility(board, player_1, player_2)

            return score
            # goto utility
        else:
            cutoff = cutoff + 1
            v = 10000000000000000000000000
            f_q = make_new_boards(board, player)
            for j in f_q:
                interim_2 = max_value(j, alpha, beta, cutoff, depth, player, game, a_list, b_list)
                v = min(v, interim_2)

                if v <= alpha:
                    break

                else:
                    beta = min(beta, v)
                    # print(beta,"beta")
                    b_list.insert(0, beta)

                """if beta in game.keys():
                    game[beta].append(j)
                else:
                    game[beta] = [j]"""

            return v
#********************To Determine which keys for stake and raid***************************
    def action(board,player,N,curr_stake_keys,curr_raid_keys):

        for keys in board:
            if board[keys][1] == ".":
                #all empty cells can have stake
                curr_stake_keys.append(list(keys))

                # *****raid check**** only possible if current player's piece is adjacent**

                #central peices
                if (keys[1] != 1 and keys[1] != N and keys[0]!= col_max[0] and keys[0]!=col_max[N-1]): #not boundary keys

                    check_col=col_max.index(keys[0])
                    check_row = row_max.index(keys[1])
                    if (board[col_max[check_col-1],keys[1]][1] == player or board[col_max[check_col+1],keys[1]][1] == player or board[keys[0],row_max[check_row - 1]][1] == player or board[keys[0],row_max[check_row + 1]][1] == player):

                        curr_raid_keys.append(list(keys))

                #corner pieces
                elif (keys[1] == 1  and keys[0] == "A" ):
                    check_col = col_max.index(keys[0])
                    check_row = row_max.index(keys[1])

                    if (board[col_max[check_col+1],keys[1]][1] == player or board[keys[0],row_max[check_row + 1]][1] == player):

                        curr_raid_keys.append(list(keys))

                elif (keys[1] == N and keys[0] == "A"):
                    check_col = col_max.index(keys[0])
                    check_row = row_max.index(keys[1])

                    if (board[col_max[check_col + 1], keys[1]][1] == player or board[keys[0], row_max[check_row - 1]][
                        1] == player):

                        curr_raid_keys.append(list(keys))


                elif (keys[1] == 1 and keys[0] == col_max[N-1] ):
                    check_col = col_max.index(keys[0])
                    check_row = row_max.index(keys[1])

                    if (board[col_max[check_col-1],keys[1]][1] == player or board[keys[0],row_max[check_row + 1]][1] == player):

                        curr_raid_keys.append(list(keys))

                elif (keys[1] == N and keys[0] == col_max[N - 1]):
                    check_col = col_max.index(keys[0])
                    check_row = row_max.index(keys[1])

                    if (board[col_max[check_col - 1], keys[1]][1] == player or board[keys[0], row_max[check_row - 1]][
                        1] == player):

                        curr_raid_keys.append(list(keys))

                #Checking Edges

                else:
                    check_col = col_max.index(keys[0])
                    check_row = row_max.index(keys[1])

                    if keys[0] == "A":

                        if (board[col_max[check_col+1],keys[1]][1] == player or board[keys[0],row_max[check_row - 1]][1] == player or board[keys[0],row_max[check_row + 1]][1] == player):

                            curr_raid_keys.append(list(keys))
                    elif keys[1] == 1:
                        if (board[col_max[check_col - 1], keys[1]][1] == player or board[col_max[check_col + 1], keys[1]][
                            1] == player or board[keys[0], row_max[check_row + 1]][1] == player):

                            curr_raid_keys.append(list(keys))

                    elif keys[0]==col_max[N-1]:
                        if (board[col_max[check_col - 1], keys[1]][1] == player or board[keys[0], row_max[check_row - 1]][1] == player or
                                    board[keys[0], row_max[check_row + 1]][1] == player):

                            curr_raid_keys.append(list(keys))
                    elif keys[1] == N:
                        if (board[col_max[check_col - 1], keys[1]][1] == player or board[col_max[check_col + 1], keys[1]][
                            1] == player or board[keys[0], row_max[check_row - 1]][1] == player):

                            curr_raid_keys.append(list(keys))



        #opening an output file

    out_file = open("program_out.txt", "w")


#****Reading data from input file*********
    MODE = in_file.readline().split('\n')[0]        # selecting mode to play
    YOUPLAY = in_file.readline().split('\n')[0]     #the person for whom we need to find the best possible move
    DEPTH = int(in_file.readline().split('\n')[0])  #depth or number of plays till we have to seach


#***************Making the board*********************
    base_board=OrderedDict()
    cell_val = []
    cell_state = []
    key = []
    curr_stake_keys=[]
    curr_raid_keys=[]
    game_state = OrderedDict()
    game_tree=OrderedDict()

    """Spliting to obtain each element of the board. Lines are right now was 498561, after splitting 49,85,61 and
    states like X.. would change to X,.,."""


    for i in range(N):
        line = in_file.readline().split('\n')[0]
        cell_val.append(line.split(" "))

         #check for more cases
        for j in range(N):

            base_board[col_max[j],row_max[i]] = [int(cell_val[i][j])]

    for i in range(N):
        state = list(in_file.readline().split('\n')[0])

        cell_state.append(state)
        for j in range(N):
            base_board[col_max[j],row_max[i]] = base_board[col_max[j],row_max[i]]+[cell_state[i][j]]

    #print("Key =", key)
    #print("CellVal=" , cell_val)
    #print("Cellstate",cell_state)
    #print("board", base_board)
    frontier.append(base_board)
    game_state[0]=[base_board]
    game_tree[0]=[base_board]

#****setting up other player***
    player_1 = YOUPLAY
    if YOUPLAY == "X":
        player_2 = "O"
    elif YOUPLAY =="O":
        player_2 = "X"

    alpha=-100000000000000000000000000000000000000000
    beta = 100000000000000000000000000000000000000000


    counter_depth = 0
    for key_1 in base_board.keys():
        if base_board[key_1][1]==".":
            counter_depth = counter_depth+1

    #if only 1 place is empty and asked to search for 5 plays then program resets the depth to number of empty places

    if counter_depth < DEPTH:
        DEPTH = counter_depth

    #**********NOT using iterative approach**********
    #if MODE == "MINIMAXX"
    #minimax(base_board,YOUPLAY,DEPTH,N,curr_stake_keys, curr_raid_keys,cutoff,frontier,game_state,player_1,player_2)


    #***Using recursive approaches****
    if MODE == "MINIMAX":
        MINIMAXX(base_board, DEPTH, player_1, player_2, cutoff)


    elif MODE == "ALPHABETA":
        alphabeta(base_board, alpha, beta, DEPTH, player_1, player_2, cutoff)

    out_file.close()

#***if file is run on a single input*****
if __name__ == "__main__":
    in_file = open("input.txt", "r")
    N = int(in_file.readline().split('\n')[0])
    main(in_file,N)




