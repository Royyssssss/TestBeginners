Question 1

print("You are exploring a rainforest in search of treasure." 
"Legend has it that there are some buried on a nearby island.")
print("you come across the lake.")

Question 2

print("Do you want to swim across, or wait for the boat? ") 
action = input("(swim/wait)")
if action == "swim":
    print("You get eaten by a hungry shark. Game over. ")
elif action == "wait":
    print("A boat arrives and you arrive at the island safely.")

Question 3

  print("Do you want to venture inside or walk on?")
    action = input("(venture/walk):")
    if action == "venture":
        print ("You are squished by boulders never to be seen again. Game over.")
    if action == "walk":
        print ('You’re at a crossroads.')
Question 4
 print ('Do you go left, right, or straight?')
        action = input("(left/right/straight):")
        if action == "left":
            print("You are trampled by a herd of wildebeest. Game over.")
        elif action == "straight":
            print("You get stung by a poisonous wasp. Game over.")
        elif action == "right":
            print("You march on and find the buried treasure! Yippee!!")

Full Code
print("You are exploring a rainforest in search of treasure." 
"Legend has it that there are some buried on a nearby island.")
print("you come across the lake.")
print("Do you want to swim across, or wait for the boat? ") 
action = input("(swim/wait):")
if action == "swim":
    print("You get eaten by a hungry shark. Game over. ")
elif action == "wait":
    print("A boat arrives and you arrive at the island safely.")
    print ("You come to a cave.")
    print("Do you want to venture inside or walk on?")
    action = input("(venture/walk):")
    if action == "venture":
        print ("You are squished by boulders never to be seen again. Game over.")
    if action == "walk":
        print ('You’re at a crossroads.')
        print ('Do you go left, right, or straight?')
        action = input("(left/right/straight):")
        if action == "left":
            print("You are trampled by a herd of wildebeest. Game over.")
        elif action == "straight":
            print("You get stung by a poisonous wasp. Game over.")
        elif action == "right":
            print("You march on and find the buried treasure! Yippee!!")
