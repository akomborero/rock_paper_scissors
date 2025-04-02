

options = ("rock", "paper", "scissos")
player = None
computer = random.choice(options)
running = True
if player not in options:
       print("invalid choice")
while running:
        