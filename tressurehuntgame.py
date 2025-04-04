
password = "kayden123"

print("Welcome to the Treasure Hunt Game!")

attempt = input("Enter the password to begin: ")

if attempt == password:
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}! Let's start the game.")

    rooms = {
        'toilet': 'You are in a dark toilet.',
        'kitchen': 'You are in a kitchen.',
        'garden': 'You are in a beautiful garden.',
        'living_room': 'You are in a cozy living room.',
        'bedroom': 'You are in a quiet bedroom.',
        'basement': 'You are in a spooky basement.',
        'attic': 'You are in a dusty attic.',
        'backyard': 'You are in a lush backyard.'
    }

    treasure_room = 'backyard'
    current_room = 'toilet'

    movements = {
        'toilet': {'north': 'kitchen', 'south': 'living_room'},
        'kitchen': {'north': 'garden', 'south': 'toilet'},
        'garden': {'south': 'kitchen', 'west': 'backyard'},
        'living_room': {'north': 'toilet', 'south': 'bedroom'},
        'bedroom': {'north': 'living_room', 'south': 'basement', 'up': 'attic'},
        'basement': {'north': 'bedroom'},
        'attic': {'down': 'bedroom'},
        'backyard': {'east': 'garden'}
    }

    puzzles = {
        'kitchen': 'Solve the puzzle to unlock the garden door.',
        'bedroom': 'Find the hidden key to unlock the basement door.'
    }

    puzzle_solutions = {
        'kitchen': 'answer',
        'bedroom': 'key'
    }

    while True:
        print(rooms[current_room])
        if current_room in puzzles:
            print(puzzles[current_room])
            solution = input(f"What's your solution, {player_name}? ").lower()
            if solution == puzzle_solutions[current_room]:
                print("Correct! You can now proceed.")
            else:
                print("Incorrect. Try again!")
                continue
        command = input(f"What do you want to do, {player_name}? (go north/south/up/down) ").lower()
        if command.startswith('go '):
            direction = command.split(' ')[1]
            if direction in movements[current_room]:
                current_room = movements[current_room][direction]
            else:
                print("You can't go that way!")
        else:
            print("Invalid command!")
        if current_room == treasure_room:
            print(f"Congratulations, {player_name}! You found the treasure!")
            break
        if current_room == 'basement':
            print(f"Sorry, {player_name}. You're stuck in the basement! Game over.")
            break
else:
    print("Incorrect password. Access denied.")
