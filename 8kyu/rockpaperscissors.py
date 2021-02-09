'''
Instructions: Let's play Rock, Paper, Scissors! You have to return which 
player won! In case of a draw return Draw!.

Examples:
rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!

'''
def rps(p1, p2):
    #First define all possible moves that player 1 will win
    #Draw is the case if both players play the same move
    #Else, player 2 is the winner
    if (p1 == "scissors" and p2 =="paper") or (p1 == "paper" and p2 =="rock") or (p1 == "rock" and p2 =="scissors"):
        return "Player 1 won!"
    elif p1 == p2:
        return "Draw!"
    else:
        return "Player 2 won!"