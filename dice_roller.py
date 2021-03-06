def main():
  import random
  num_of_players = int(input('How many players?'))
  player_totals=dict()
  for j in range(0, num_of_players):
      name = input('Hello! What is your name?')
      print('Welcome ' +name+'!')
      dice_rolls = int(input('How many dice would you like to roll? '))
      dice_sum = 0
      dice_size = int(input('How many sides are the dice? '))
      for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Success!')
        else:
            print(f'You rolled a {roll}')
      print(f'You have rolled a total of {dice_sum}')
      player_totals[name] = dice_sum
  sorted_player_totals = sorted(player_totals.items(), key=lambda x: x[1], reverse=True)
  print(sorted_player_totals)
  print(f'The winner is {sorted_player_totals[0][0]}')

if __name__== "__main__":
  main()
