#1b
#i) Minimax search algorithm
#ii) Tree data structure
#iii) correctness and efficiency
#iv) asymptotic analysis
#v) Linear search and Binary search
#vi) The total iterations required to find a number would be at most log2(total_array_size), which is log2(300) in this case which gives the answer of 9
#vii) Square making algorithm


def main():
    # Set up some initial values
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2
    # Play the game
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All the pegs are moved!')

# The move_discs function displays a disc move in
# the Towers of Hanoi game.
# The paramenters are:
# num: The number of discs to move.
# from_peg: The peg to move from.
# to_peg: The peg to move to.
# temp_peg: The temporary peg.
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, to_peg, temp_peg)
        print('Move a disc from peg', from_peg, 'to peg', temp_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

# Call the main function
main()