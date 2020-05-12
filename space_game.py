def space_game(x):
    x = str(x)
    co = x.count(" ")
    if co//2 == 0:
        print("you won")
    else:
        print("you lose")

space_game (" I'm going with a sword judge ")
space_game("Hello")