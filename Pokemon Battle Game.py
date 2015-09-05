import random

print("Welcome to Pokemon Battle Game! ")

name = input("Trainer, What is your name? ")
pokemon = input("Choose your pokemon (Absol, Greninja, Sylveon, Mime jr or Pikachu): ")

# Data +==========================================================================+
# Data of Pokemon
if pokemon.lower() == "sylveon":
  pokemon_hp = 70
  pokemon_attacks = {"rainbow dash": 15, "tackle": 10, "super sonic": 25}
  pokemon_attack_list = ["rainbow dash", "tackle", "super sonic"]
  pokemon_weakness = "dark"
  pokemon_type = "fairy"
elif pokemon.lower() == "absol":
  pokemon_hp = 90
  pokemon_attacks = {"ice beam":15, "tackle":10, "shadow ball":20}
  pokemon_attack_list = ["ice beam", "tackle", "shadow ball"]
  pokemon_weakness = "fairy"
  pokemon_type = "dark"
elif pokemon.lower() == "pikachu":
  pokemon_hp = 55
  pokemon_attacks = {"thunder shock":25, "iron tail":35, "agility":20}
  pokemon_attack_list = ["thunder shock", "iron tail", "agility"]
  pokemon_weakness = "rock"
  pokemon_type = "electric"
elif pokemon.lower() == "greninja":
  pokemon_hp = 120
  pokemon_attacks = {"water shuriken": 15, "water gun":10, "recovery mist":-20}
  pokemon_attack_list = ["water shuriken", "water gun", "recovery mist"]
  pokemon_weakness = "grass"
  pokemon_type = "water"
elif pokemon.lower() == "mime jr":
  pokemon_hp = 180
  pokemon_attacks = {"psychic": 15, "encore":10, "sleepy lost":18}
  pokemon_attack_list = ["psychic", "encore", "sleepy lost"]
  pokemon_weakness = "dark"
  pokemon_type = "psychic"

# Enemies -------
random_number = random.randint(1, 3)

if random_number == 1:
  enemy = "darkrai"
  enemy_type = "dark"
  enemy_attacks = {"shadow ball": 30, "scare":15 , "nightmare":20 }
  enemy_attacks_list = ["shadow ball", "scare", "nightmare"]
  enemy_hp = 90
elif random_number == 2:
  enemy = "diancie"
  enemy_type = "fairie"
  enemy_attacks = {"diamond blast":20 , "fairy garden":10 , "luminous swirl":15 }
  enemy_attacks_list = ["diamond blast", "fairy garden", "luminous swirl"]
  enemy_hp = 100
elif random_number == 3:
  enemy = "regice"
  enemy_type = "ice"
  enemy_attacks = {"ice beam":30 , "rest":-20 , "focus punch":20 }
  enemy_attacks_list = ["ice beam", "rest", "focus punch"]
  enemy_hp = 70
  
  
# Data Ends +===============================================================+


# Special Attack Effects ~~~~~~~~~~~~~~~~~~~~~~~~~
enemy_save_counter = False
pokemon_save_counter = False
# Special Attack Effects End ~~~~~~~~~~~~~~~~~~~~~

count = 0

# Game Begins ++=================++ #
while pokemon_hp > 0 or enemy_hp > 0:
  count += 1 # Increment Number of Rounds
  
  # Display Stats
  print("")
  print("Round {}!".format(count))
  if count == 1:
    print("Enemy Appeared: {} HP: {}. Your Pokemon's HP: {}".format(enemy.capitalize(), enemy_hp,
                                                                   pokemon_hp))
  else:
    print("*v* {}'s HP: {}, ~v~ {}'s HP: {}".format(enemy.capitalize(),
                                                    enemy_hp, pokemon.capitalize(), pokemon_hp))
    
  print("{}'s Available Attacks:".format(pokemon.capitalize()),
        end = " ")
  for attack, damage in pokemon_attacks.items():
    print(">{}".format(attack.capitalize()), end = " ")
    
  print("")
  pokemon_attack_choice = input("What attack will your pokemon use: ").lower()
  
  for attack, damage in pokemon_attacks.items():
    
    # Pokemon Attacks -------
    if pokemon_attack_choice.lower() == attack.lower():
      print("{} uses {} (*v*)".format(pokemon.capitalize(), pokemon_attack_choice.capitalize()))
      
      if pokemon_attacks[pokemon_attack_choice] < 0:
        pokemon_hp += (-1)*pokemon_attacks[pokemon_attack_choice]
      else:
        if enemy_save_counter == False: # No save effects are enabled/true
          enemy_hp -= pokemon_attacks[pokemon_attack_choice]
      print("")
      break # end if
    else:
      pokemon_attack_fails = True
    if pokemon_attack_fails == True:
      print("{} tries to use {}. Attack Fails!".format(pokemon, pokemon_attack_choice))
  
  if enemy_hp <= 0:
    break
  
  # Enemy Attacks ------
  enemy_attack_choice = enemy_attacks_list[random.randint(1, 3) - 1]
  
  for attack, damage in enemy_attacks.items():
    if enemy_attack_choice.lower() == attack.lower():
      if enemy_attacks[enemy_attack_choice] < 0:
        enemy_hp += (-1)*enemy_attacks[enemy_attack_choice]
      else:
        if pokemon_save_counter == False: # No save effects are enabled
          pokemon_hp -= enemy_attacks[enemy_attack_choice]
      print("{} uses {} (*v*)".format(enemy.capitalize(), enemy_attack_choice.capitalize()))
      print("{}'s HP: {}, {}'s HP: {}".format(enemy.capitalize(), enemy_hp, pokemon.capitalize(), pokemon_hp))
      print("")
      break
  if pokemon_hp <= 0:
    break
  
  print("Round Ends! {>_<} ")
  print("=================")
      
    
if enemy_hp <= 0:
  result = "{} Wins! {}, You Won in {} rounds! :D".format(name, pokemon.capitalize(), count)
  print("Congratulations! You have defeated {}!".format(enemy.capitalize()))
  print("{} Wins! {}, You Won in {} rounds! :D".format(name, pokemon.capitalize(), count))
elif pokemon_hp <= 0:
  result = "{} Wins! You Lose in {} rounds! :<".format(enemy.capitalize(), count)
  print("{} has been utterly destroyed! >_<".format(pokemon.capitalize()))
  print("{} Wins! You Lose in {} rounds! :<".format(enemy.capitalize(), count))
  
  
# Email the score
import smtplib

if input("Do you want a score report emailed to you? [yes/no]: ").lower() == "yes":
  sender = "pokemon_battle@cs.usfca.edu"
  recipient = input("Please enter your email: ")
  host = "0.0.0.0"
  port = "8000"
  session = smtplib.SMTP("nexus")
  msg = "To: {} <{}>\n{}".format(name, recipient, result)
  try:
    smtpresult = session.sendmail(sender, recipient, msg)
    print("Message sent succesfully!")
  except:
    print("Message sending fails :<")
  
