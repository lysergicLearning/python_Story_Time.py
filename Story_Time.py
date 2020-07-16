print("Welcome to storyTime!")
character_name = input("Please enter a character name: ")
character_age = input("Please enter a character age: ")

def story_1() :
    print("A CASUAL STORY")
    print("There was once a man named " + character_name + ", ")
    print("he was " + character_age + " years old. ")
    print("He really liked the name " + character_name + ", ")
    print("but didn't like being " + character_age + ".")

def story_2() :
    print("A HOOD STORY")
    print("There was once a b*tch a** foo named " + character_name + ", ")
    print("and he was " + character_age + ". ")
    print("This motherf*ckah didn't know sh*t, but he was proud to be a " + character_age + " year old b*tch named "
          + character_name + ".")

def ending() :
    print()
    print("That was a good story!")
    character_name = input("What's your name?: ")
    character_age = input("and age?: ")
    print()
    print("Nice to meEt yoU!?@#")
    print("NAME: {0} AGE: {1} , DATA NOTED FOR FUTURE PLANS.".format(character_name, character_age))
    print("...uh...whooops...ignore that")

def key() :
    sum_bs = False
    print(" 1")
    print(" 2")
    print(" 3")
    print(" 4")
    fable_type = int(input("Please enter a number from above to pick a story type: "))
    print()

    if fable_type > 4:
        print("bruh, how you gonna do me like that...")
        sum_bs = True
    elif fable_type == 1:
        story_1()
        #ending()
    elif fable_type == 2:
        story_2()
        #ending()
    elif fable_type == 3 or 4:
        story_1()
        #ending()

    if sum_bs == False:
        ending()

key()


