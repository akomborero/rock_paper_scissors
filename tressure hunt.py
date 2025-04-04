print("welcome to the tressure hunt game!")

rooms = {"hallway": "You are in a dark hallway.",
         "kitchen": "You are in yhe kitchen.",
         "garden": "You re in the Beautful Garden.",
         "living_room": "You are in a living room",
         "bedroom": "You are in a Bedroom",
         "basement":  "You are in a spooky basement",
         "attick": "you are in a dusty attick",
         "backyard": "you are in a lush backyard."
         }


tressure_room = "backyard"

current_room = "hallway"

movements = {"hallway":{"north":
            "kitchen", "south":
            "living_room"},
            "kitchen":{"north":
             "garden","south":"hallway"},
             "garden": {"south":
                        "kitchen", "west":"backyard"},
                        "living_room":{"north":
                                       "hallway", "south": "bedroom"},
                                       "bedroom": {"north":
                                                   "living_room", "south": "basement", "up": "attic"},
                                                   "basement": {"north": 
                                                                "bedroom"},
                                                                "attic": {"down": "bedroom"},
                                                                "backyard":{"east": "garden"}

                                            }

puzzles = { "kitchen": "solve the puzzle to unlock the garden door.",
           'bedroom' : 'find the hidden key to unlock the basement door.'
}

puzzle_solution = {

    'kitchen' : 'answer',
    'bedroom' : 'key'
}

while True:
    print(rooms[current_room])