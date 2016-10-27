import Board_game

import unittest


class TestBoardGame(unittest.TestCase):


    def test_board(self):

        print("test"+str(counter))

        c="input_"+str(counter)+".txt"  #changing input file
        in_file = open(c,"r")           #input file
        N = int(in_file.readline().split('\n')[0])
        Board_game.main(in_file,N)
        S="output_"+str(counter)+".txt" #changing output file
        check_file=open(S,"r")          #correct output file to check from

        file_from_program = open("program_out.txt","r")

        #checking each line in both txt files
        for line_check in range(int(N+1)):

            self.assertEqual(check_file.readline(),file_from_program.readline(),msg = "test case not passed")

        in_file.close()
        check_file.close()
        file_from_program.close()

#*********************Running for 10 different test cases****************************
if __name__ == "__main__":
    test_boards=10
    #for m in range(1,test_boards):
    for counter in range(1,test_boards+1):
        unittest.main(exit=False)




"""The purpose of this test file is to generate and test 10 standard outputs against the program_out.txt file
generated by the program. Initially unit testing was performed over N = even and N = odd. Some test cases take around
1 Minute to generate completely."""




