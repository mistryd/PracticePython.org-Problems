gameStatus = True

print "Hello and Welcome to Daniyal's Rock Paper Scissors Showdown"

p1 = raw_input("Player 1, enter your name: ")
p2 = raw_input("Player 2, enter your name: ")

print "\nNow lets get \n \n"

move1 = ''
move2 = ''

while gameStatus:
    print p1 + " enter your move (r for rock, p for paper, and s for scissors)"

    move1 = raw_input()

    print "\n" + p2 + " enter your move (r for rock, p for paper, and s for scissors)"

    move2 = raw_input()

    if move1 == 'r':
        if move2 == 'r':
            print "Draw! Go again!! \n"
        elif move2 == 'p':
            print p2 + " wins, congrats!"
            gameStatus = False
        elif move2 == 's':
            print p1 + " wins, congrats!"
            gameStatus = False
        else:
            print p2 + " entered an illegal move... try again :("

    elif move1 == 'p':
        if move2 == 'p':
            print "Draw! Go again!! \n"
        elif move2 == 's':
            print p2 + " wins, congrats!"
            gameStatus = False
        elif move2 == 'r':
            print p1 + " wins, congrats!"
            gameStatus = False
        else:
            print p2 + " entered an illegal move... try again :("

    elif move1 == 's':
        if move2 == 's':
            print "Draw! Go again!!"
        elif move2 == 'r':
            print p2 + " wins, congrats!"
        elif move2 == 'p':
            print p1 + " wins, congrats!"
        else:
            print p2 + " entered an illegal move... try again :("

