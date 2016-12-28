# Rock-paper-scissors-lizard-Spock
print ( "Coded by arasharn" )
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#_________________________________________________________________________________________________________________________________________________________________________________________________________
# Importing mudules and functions_________________________________________________________________________________________________________________________________________________________________________
import random
from name_to_number import name_to_number
from number_to_name import number_to_name
#_________________________________________________________________________________________________________________________________________________________________________________________________________
def rpsls(player_choice): 
    """This function decides about the computer choice 
    and the winner"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    print ( )
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Player's choice
    print ( "Player choosed "+player_choice )
    # convert the player's choice to player_number using the function name_to_number()
    player_numb = name_to_number(player_choice)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # compute random guess for comp_number
    comp_numb = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_name = number_to_name(comp_numb) 
    # print out the message for computer's choice
    print ( "Computer choosed "+ comp_name )
# Results-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # compute difference of comp_number and player_number modulo five
    dif = player_numb-comp_numb
    res = dif%5
    # Determine winner, print winner message
    if res > 2:
        print ( "Computer ("+comp_name + ") wins" )
    elif res <= 2 and res > 0:
            print ( "Player ("+player_choice+ ") wins" )
    else:
                print ( "Player and computr tie" )
#________________________________________________________________________________________________________________________________________________________________________________________________________   
# Test____________________________________________________________________________________________________________________________________________________________________________________________________
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
