# Udemy 100 Days of Code - Python Day 3 Project
# Treasure Island (Choose your own adventure game)

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure Island...')
print('Your mission is to find the treasure.')

step_one = input('You find yourself on a deserted island. Your back is to the ocean. To your left are ruins, and to your right is a jungle. Do you go "right" or "left"? ').lower()
if step_one == 'left':
    print('''       _.-""}
      / "" ;
  .-"` __] ',               ___
  I_ ""__.`-,;             |   |
    I_.,-"ii"{             !___!
    | ||  ||  |        ,    | |
    | ||  ||  |       .;    | |
    | ||  ||  |       | \   | |
    | ||  ||  |       |  |  | |
    | ||  ||  |       |  |  | |   __
    | ||  ||  |       |  |  | |  |  |
    | ||  ||  |   ;|  |  |  | |  |  |
    | ||  ||  |"\_/`,_|  |  | |  |  |  ___.--""`\
    | ||  ||  |       |  |\.| |=,|  |""          `,
    | ||  ||  |       |  |  | |  |  |____________.-+.__
   _:_!|_,'!__!       |  |  | |_,!  !         __,I   `"|
  :     |      `-""`,.!__!-,!_!_ '--'`,_,--"""         |
  |     ;___          `"-.-'    `,_.-'"            _..-'
   `-._ |   """--,,_     |`""-.--'|         __.--""
       `"--..__     ""--.|    |   |_,_  _.-'
               ""--.._   `-,__!_.-' _,""      fsc
                      ""--,____.--'"''')
    print('You wander into the ruins and are immediately killed by an ancient trap. Sorry...')
    print('Game Over.')
    exit
elif step_one == 'right':
    step_two = input('You walk to, and find relief from the sun, within the jungle. There\'s many trees with fruit at the top that you could climb, and a lake filled by a waterfall you can explore. Do you "climb" a tree for fruit or explore the "waterfall"? ').lower()
    if step_two == 'climb':
        print('You almost reach the top and grab some fruit but grab a slippery branch and plunge to your death. Guess you\'re not a great climber...')
        print('''              _{\ _{\{\/}/}/}__
             {/{/\}{/{/\}(\}{/\} _
            {/{/\}{/{/\}(_)\}{/{/\}  _
         {\{/(\}\}{/{/\}\}{/){/\}\} /\}
        {/{/(_)/}{\{/)\}{\(_){/}/}/}/}
       _{\{/{/{\{/{/(_)/}/}/}{\(/}/}/}
      {/{/{\{\{\(/}{\{\/}/}{\}(_){\/}\}
      _{\{/{\{/(_)\}/}{/{/{/\}\})\}{/\}
     {/{/{\{\(/}{/{\{\{\/})/}{\(_)/}/}\}
      {\{\/}(_){\{\{\/}/}(_){\/}{\/}/})/}
       {/{\{\/}{/{\{\{\/}/}{\{\/}/}\}(_)
      {/{\{\/}{/){\{\{\/}/}{\{\(/}/}\}/}
       {/{\{\/}(_){\{\{\(/}/}{\(_)/}/}\}
         {/({/{\{/{\{\/}(_){\/}/}\}/}(\}
          (_){/{\/}{\{\/}/}{\{\)/}/}(_)
            {/{/{\{\/}{/{\{\{\(_)/}
             {/{\{\{\/}/}{\{\\}/}
              {){/ {\/}{\/} \}\}
              (_)  \.-'.-/
          __...--- |'-.-'| --...__
   _...--"   .-'   |'-.-'|  ' -.  ""--..__
 -"    ' .  . '    |.'-._| '  . .  '   jro
 .  '-  '    .--'  | '-.'|    .  '  . '
          ' ..     |'-_.-|
  .  '  .       _.-|-._ -|-._  .  '  .
              .'   |'- .-|   '.
  ..-'   ' .  '.   `-._.-�   .'  '  - .
   .-' '        '-._______.-'     '  .
        .      ~,
    .       .   |\   .    ' '-.
    ___________/  \____________
   /  Why is it, when you want \
  |  something, it is so damn   |
  |    much work to get it?     |
   \___________________________/''')
        print('Game Over.')
    elif step_two == 'waterfall':
        print('''
                          _.._
   _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
      --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
     ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
     .-~~-.          ------     /          '    . `     `    `  \
    (_^..^_)-------           /  '    '      '      `
Lester||||AMC       --------/     '     '   ''')
        print('You explore the waterfall and find there\'s a cave behind it. Upon entering the cave, you see there\'s two paths; one to the right, and one to the left.')
        step_three = input('Which path do you choose, "left" or "right"? ').lower()
        if step_three == 'left':
            print('Lucky you. At the end of the short path, there is a hidden treasure chest, filled with treasure beyond your wildest dreams.')
            print('It\'ll probably be a big pain in the ass, but you begin to haul the treasure chest up and out and hope to God someone comes to find you on the island...')
        elif step_three == 'right':
            print('The light grows dimmer and dimmer, but you continue on...that is until you take that one fatal step into a hole and fall to your death.')
            print(''' ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \ms          |            \ *
 ********************************************************************************''')
            print('Game Over')
