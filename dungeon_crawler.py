import random
print("Welcome to The Mystery Dungeon of Death!")

player = {
    "attack": 5,
    "health": 25,
    "gold": 0,
    "max_hp": 25,
    "exp": 0,
    "level": 1,
    "healing" : 5,
    "dodge" : 0,
    "inventory": []
    }

def encounter():
    encounter1 = {
        "name": random.choice(["Goblin","Skeleton","Zombie"]),
        "attack": random.randint(1,5),
        "health": random.randint(10,15),
        "gold": random.randint(1,10),
        "exp": 5
        }
    encounter2 = {
        "name": random.choice(["Demon","Vampire","Werewolf"]),
        "attack": random.randint(10,15),
        "health": random.randint(30,45),
        "gold": random.randint(15,20),
        "exp": 5
        }
    encounter3 = {
        "name": random.choice(["Dragon","Lich","Giant"]),
        "attack": random.randint(20,35),
        "health": random.randint(70,105),
        "gold": random.randint(50,75),
        "exp": 5
        }
    if player["level"] < 3:
        fight(encounter1)
    elif player["level"] < 5:
        fight(encounter2)
    elif player["level"] < 7:
        fight(encounter3)
def dungeon():
    if random.randint(1,4) == 1:
        shop()
    else:
        encounter()
def shop():
    shopkeeper = {
        "name": "Shopkeeper",
        "attack": random.randint(5,10),
        "health": random.randint(15,20),
        "gold": 17,
        "exp": 15
        }
    print("Hi, welcome to the shop")
    while True:
        print(f"what would you like to buy? You have {player["gold"]} gold ")
        if not "padding" in player["inventory"]:
            print("1. 10g Armor padding")
        if not "armor" in player["inventory"]:
            print("2. 50g Steel armor")
        if not "sword" in player["inventory"]:
            print("3. 20g Sword")
        if not "magic" in player["inventory"]:
            print("4. 100g Magic enchantment")
        if not "belt" in player["inventory"]:
            print("5. 30g Dodge belt")
        if not "medkit" in player["inventory"]:
            print("6. 30g Medkit")
        print("7. attempt to steal\n8. leave\n")
        buy_item = validate_input(": ", 8)
        if buy_item == 1:
            if "padding" in player["inventory"]:
                print("already bought")
            elif player["gold"] >= 10:
                player["gold"] -= 10
                player["max_hp"] += 15
                player["inventory"].append("padding")
                shopkeeper["gold"] += 10
            else:
                print("Not enough gold")
        elif buy_item == 2:
            if "armor" in player["inventory"]:
                print("already bought")
            elif player["gold"] >= 50:
                player["gold"] -= 50
                player["max_hp"] += 60
                player["inventory"].append("armor")
                shopkeeper["gold"] += 50
            else:
                print("Not enough gold")
        elif buy_item == 3:
            if "sword" in player["inventory"]:
                print("already bought")
            elif player["gold"] >= 20:
                player["gold"] -= 20
                player["attack"] += 5
                player["inventory"].append("sword")
                shopkeeper["gold"] += 20
            else:
                print("Not enough gold")
        elif buy_item == 4:
            if "magic" in player["inventory"]:
                print("already bought")
            elif player["gold"] >= 100:
                player["gold"] -= 100
                player["attack"] += 10
                player["inventory"].append("magic")
                shopkeeper["gold"] += 100
            else:
                print("Not enough gold")
        elif buy_item == 5:
            if "belt" in player["inventory"]:
                print("already bought")
            elif player["gold"] >= 30:
                player["gold"] -= 30
                player["dodge"] += 1
                player["inventory"].append("belt")
                shopkeeper["gold"] += 30
        elif buy_item == 6:
            if "medkit" in player["inventory"]:
                print("already bought")
            elif player["gold"] >= 30:
                player["gold"] -= 30
                player["healing"] += 10
                player["inventory"].append("medkit")
                shopkeeper["gold"] += 30
        elif buy_item == 7:
            if random.randint(1,4) == 1:
                stolen_gold = round(random.randint(20,50) / 100 * shopkeeper["gold"])
                player["gold"] += stolen_gold
                print(f"You got {stolen_gold}")
            else:
                fight(shopkeeper)
                break
        elif buy_item == 8:
            break
def fight(encounter):
    while encounter["health"] > 0:
        if player["health"] < 0:
            break
        if player["health"] > player["max_hp"]:
            player["health"] = player["max_hp"]
        print(f"{encounter["name"]}\nAttack = {encounter["attack"]}\nHeath = {encounter["health"]}")
        print(f"Player attack = {player["attack"]}\nPlayer health = {player["health"]}")
        combat = validate_input("1. attack\n2. heal\n: ", 2)
        if combat == 1:
            encounter["health"] -= player["attack"]
        elif combat == 2:
            player["health"] += player["healing"]
        if random.randint(0,player["dodge"]) == 10:
            print("dodged the attack")
        else:
            player["health"] -= encounter["attack"]
    if player["health"] > 0:
        player["gold"] += encounter["gold"]
        player["exp"] += encounter["exp"]
        if player["exp"] >= 20:
            level_up()
def validate_input(prompt, limit):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input <= limit:
                return user_input
        print("invalid input")
def level_up():
    player["level"] += 1
    player["exp"]  -= 20
    player["max_hp"] = 25 * player["level"]
    player["attack"] = 5 * player["level"]
    player["healing"] = 5 * player["level"]
    print("level up!")
def game_over():
    print("You lose")
    print(f"Gold = {player["gold"]}, Level = {player["level"]}")
    player["attack"] = 5
    player["health"] = 25
    player["gold"] = 0
    player["max_hp"] = 25
    player["exp"] = 0
    player["level"] = 1
    player["healing"] = 5
    player["dodge"] = 0
    player["inventory"] =[]
while True:
    if player["health"] < 0:
       game_over()
    play_again = validate_input("1. Play again\n2. Leave\n: ", 2)
    if play_again == 1:
        dungeon()
    else:
        break
    print(f"Gold = {player["gold"]}, Level = {player["level"]}")
    decision = validate_input("1. Keep going\n2. Leave\n: ", 2)
    if decision == 1:
        dungeon()
    else:
        break
        
    
