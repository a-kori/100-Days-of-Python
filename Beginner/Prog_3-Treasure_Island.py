print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("\nWelcome to the Treasure Island!")
print("Your mission here is to get all the questions right to find the hidden treasure!\n")

print('''You have arrived at the island, but have neither a map, nor an idea, where to go. Suddenly, you see a stranger approaching and greeting
you with a cheerful "Ahoi!" This is how pirates say "Hello", but he doesn't look like one. Actually, he is also looking for the treasure - just
like you! He even agrees to help you, if you guess, what country he is from! Any ideas? 
a : Czech Republic
b : Poland
c : Slovenia
''')

if input("Enter a single letter a, b or c. All the other characters will be taken for wrong answers: ") == "a" :

    print('''\nSo far so good! Your new companion agrees to team up! On the map he has, he shows you that the path to the treasure lies through a dark,
thick forest. There, in the middle of your journey, you are confronted by a madman, who is crazy about the "Pirates of the Caribbean" movies. And
he won't let you through unless you tell him, which of the following phrases were actually improvised by the actor Johnny Depp, and have never been in 
the initial script of the movies!
a : "Take what ye can - give nothin' back!"
b : "CAPTAIN Jack Sparrow!"
c : "Savvy?"
    ''')

    if input("Your answer: ") == "c" :
        print('''\nLucky dodge! Now that you have passed the madman, there is only a few days' journey left to your desired treasure! However, you're running short of
all your food and water supplies. What do you choose to do first?
a : Go deeper into the forest, probabably full of berries, edible insects etc.
b : Find a nearby river to collect water.
c : Eat the Czech guy and tell no-one about it.
        ''')

        input = input("Your answer: ")

        if input == "a" :
            print('''Water is the first thing you need to survive in the wild. So, it would be better to collect water first. But you both went to the forest and were
immediately eaten by tigers... Bad luck!''')
        elif input == "b" :
            print('''That's right! Water comes first! Besides, you were lucky enough to catch some fish in the river and cook it! On the next day, full of energy and
enthusiasm, you continued your journey and finally found the treasure! Congratulations!''')
        elif input == "c" :
            print("Interesting choice! Too bad for you though, as you can't read the map and got lost in the woods afterwards... Ever thought about collecting berries?")
        else :
            print(f"Whatever {input} means, that's not correct! You didn't find the treasure... :(")

    else :
        print("Oof, the madman didn't like your lack of enthusiam for Captain Jack Sparrow's quotes... You now have an hour to leave the island - hurry!")     

else :
    print("Oops... Apparently, you got it wrong, as he walked away with an offended face... Better luck next time!")
    




