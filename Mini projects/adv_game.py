name=input("type your name:")
print("welcome to the adventure game", name )

ans=input("you are stuck in a sand ditch on a deserted island. DO you want to crawl out left or right? Type left/right ? : ")

if ans=="left" :
    ans=input("you make it out and see a starfish and a crab on the sand. you are hungry. Which do you eat, starfish or crab?")

    if ans=="crab" :
        ans=input("you ate it raw. fingers crossed. Food in your belly helps to see a coconut tree. you are thirsty. do you drink the coconut water ? yes or no?")
        if ans=="yes":
            print("Coconut water and raw crab don't mix. you don't survive")
        elif ans=="no":
            print("Good choice. you see a ship. you survived")
        else:
              print("not a valid option. you lose")

    elif ans=="starfish" :
        print("oh no! you immediately dont feel well. you dont survive.")
    else:
        print("not a valid option. you lose")


elif ans=="right" :
    print("That side is slippery. You fall vey far into some weired cavern. you dont survive.") 

else:
    print("not a valid option. you lose")



print("Thanks for trying")