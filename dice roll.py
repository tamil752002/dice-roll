import random
def roll():
	min_value=1
	max_value=6
	roll=random.randint(min_value,max_value)
	return roll
while True:
	players=input('enter the number of the players(2-4):')
	if players.isdigit():
		players=int(players)
		if 2<= players<=4:
			break
		else:
			print("must be between 2-4 players.")
	else:
		print("invalid input")
maxscore=50
player_scores=[0 for _ in range(players)]
while max(player_scores)<maxscore:
	for player_idx in range(players):
		print("\nplayer numbe",player_idx+1,"turn has started!")
		print("your total score is: ",player_scores[player_idx],"\n")
		current_score=0
		while True:
			should_roll=input("would you like to roll (y)")
			if should_roll !="y":
				break

			value=roll()
			if value==1:
				print( " you rolled 1 Turn done")
				current_score=0
				break
			else:
				current_score+=value
				print("you rolled a:",value)
			print(" your total scoree is:",current_score)


		player_scores[player_idx]+=current_score
		print("your total score is :",player_scores[player_idx])
	maxscore=max(player_scores)
	winning_idx=player_scores.index(maxscore)
	print("player number",winning_idx+1,"is the winner with a score of ",maxscore)






