import screenspace as ss
import style as s
import time

def main():
    ss.Player.overwrite(ss.Back.BLACK + ss.Fore.WHITE)
    ss.Player.clear_screen()
    ss.Player.overwrite()
    lines = [s.Fore.LIGHTMAGENTA_EX + """  
  _____                                        _   _   _               _____            _     _                       ___  
 |  __ \                                      | | (_) | |             |  __ \          | |   | |                     |__ \ 
 | |  | |   ___      _   _    ___    _   _    | |  _  | | __   ___    | |__) |  _   _  | |_  | |__     ___    _ __      ) |
 | |  | |  / _ \    | | | |  / _ \  | | | |   | | | | | |/ /  / _ \   |  ___/  | | | | | __| | '_ \   / _ \  | '_ \    / / 
 | |__| | | (_) |   | |_| | | (_) | | |_| |   | | | | |   <  |  __/   | |      | |_| | | |_  | | | | | (_) | | | | |  |_|  
 |_____/   \___/     \__, |  \___/   \__,_|   |_| |_| |_|\_\  \___|   |_|       \__, |  \__| |_| |_|  \___/  |_| |_|  (_)  
                      __/ |                                                      __/ |                                     
                     |___/                                                      |___/                                      """, 
             s.Fore.RED + """
  _____                                        _   _   _                                 
 |  __ \                                      | | (_) | |                                
 | |  | |   ___      _   _    ___    _   _    | |  _  | | __   ___                       
 | |  | |  / _ \    | | | |  / _ \  | | | |   | | | | | |/ /  / _ \                      
 | |__| | | (_) |   | |_| | | (_) | | |_| |   | | | | |   <  |  __/                      
 |_____/   \___/     \__, |  \___/   \__,_|   |_| |_| |_|\_\  \___|                 ___  
 | |                  __/ |         | |                                            |__ \ 
 | |__     ___     __|___/_ __    __| |     __ _    __ _   _ __ ___     ___   ___     ) |
 | '_ \   / _ \   / _` | | '__|  / _` |    / _` |  / _` | | '_ ` _ \   / _ \ / __|   / / 
 | |_) | | (_) | | (_| | | |    | (_| |   | (_| | | (_| | | | | | | | |  __/ \__ \  |_|  
 |_.__/   \___/   \__,_| |_|     \__,_|    \__, |  \__,_| |_| |_| |_|  \___| |___/  (_)  
                                            __/ |                                        
                                           |___/                                                                 
""", 
             s.Fore.YELLOW + """
  _____                                        _   _   _                             _                           
 |  __ \                                      | | (_) | |                           | |                          
 | |  | |   ___      _   _    ___    _   _    | |  _  | | __   ___     _ __    ___  | |_   _ __    ___    ______ 
 | |  | |  / _ \    | | | |  / _ \  | | | |   | | | | | |/ /  / _ \   | '__|  / _ \ | __| | '__|  / _ \  |______|
 | |__| | | (_) |   | |_| | | (_) | | |_| |   | | | | |   <  |  __/   | |    |  __/ | |_  | |    | (_) |         
 |_____/   \___/     \__, |  \___/   \__,_|   |_| |_| |_|\_\  \___|   |_|     \___|  \__| |_|     \___/          
                      __/ |                                                                                      
        _            |___/           _                                              ___                          
       | |           | |            | |                                            |__ \                         
  ___  | |_   _   _  | |   ___    __| |     __ _    __ _   _ __ ___     ___   ___     ) |                        
 / __| | __| | | | | | |  / _ \  / _` |    / _` |  / _` | | '_ ` _ \   / _ \ / __|   / /                         
 \__ \ | |_  | |_| | | | |  __/ | (_| |   | (_| | | (_| | | | | | | | |  __/ \__ \  |_|                          
 |___/  \__|  \__, | |_|  \___|  \__,_|    \__, |  \__,_| |_| |_| |_|  \___| |___/  (_)                          
               __/ |                        __/ |                                                                
              |___/                        |___/                                                                 
""",
             s.Fore.GREEN + """
                       _                                       _                                                                             
                      | |                                     | |                                                                            
   ___    _ __      __| |   ___      _   _    ___    _   _    | |   ___   __   __   ___      __ _    __ _   _ __ ___     ___   ___           
  / _ \  | '__|    / _` |  / _ \    | | | |  / _ \  | | | |   | |  / _ \  \ \ / /  / _ \    / _` |  / _` | | '_ ` _ \   / _ \ / __|          
 | (_) | | |      | (_| | | (_) |   | |_| | | (_) | | |_| |   | | | (_) |  \ V /  |  __/   | (_| | | (_| | | | | | | | |  __/ \__ \          
  \___/  |_|       \__,_|  \___/     \__, |  \___/   \__,_|   |_|  \___/    \_/    \___|    \__, |  \__,_| |_| |_| |_|  \___| |___/          
             _   _     _              __/ |                                    _             __/ |       _             _                ___  
            (_) | |   | |            |___/                                    | |           |___/       | |           | |              |__ \ 
 __      __  _  | |_  | |__      _ __ ___     __ _   _ __    _   _     _ __   | |   __ _   _   _   ___  | |_   _   _  | |   ___   ___     ) |
 \ \ /\ / / | | | __| | '_ \    | '_ ` _ \   / _` | | '_ \  | | | |   | '_ \  | |  / _` | | | | | / __| | __| | | | | | |  / _ \ / __|   / / 
  \ V  V /  | | | |_  | | | |   | | | | | | | (_| | | | | | | |_| |   | |_) | | | | (_| | | |_| | \__ \ | |_  | |_| | | | |  __/ \__ \  |_|  
   \_/\_/   |_|  \__| |_| |_|   |_| |_| |_|  \__,_| |_| |_|  \__, |   | .__/  |_|  \__,_|  \__, | |___/  \__|  \__, | |_|  \___| |___/  (_)  
                                                              __/ |   | |                   __/ |               __/ |                        
                                                             |___/    |_|                  |___/               |___/                         
""",
             s.Fore.CYAN + """
 __     __                  _   _   _     _                                                           
 \ \   / /                 ( ) | | | |   | |                                                          
  \ \_/ /    ___    _   _  |/  | | | |   | |   ___   __   __   ___                                    
   \   /    / _ \  | | | |     | | | |   | |  / _ \  \ \ / /  / _ \                                   
    | |    | (_) | | |_| |     | | | |   | | | (_) |  \ V /  |  __/     _                             
    |_|     \___/   \__,_|     |_| |_|   |_|  \___/    \_/    \___|    (_)                            
  _ __    _ __    ___     __ _   _ __    __ _   _ __ ___    _ __ ___    _   _ __     __ _             
 | '_ \  | '__|  / _ \   / _` | | '__|  / _` | | '_ ` _ \  | '_ ` _ \  | | | '_ \   / _` |            
 | |_) | | |    | (_) | | (_| | | |    | (_| | | | | | | | | | | | | | | | | | | | | (_| |  _   _   _ 
 | .__/  |_|     \___/   \__, | |_|     \__,_| |_| |_| |_| |_| |_| |_| |_| |_| |_|  \__, | (_) (_) (_)
 | |                      __/ |                                                      __/ |            
 |_|                     |___/                                                      |___/             
"""
             ]
    locations = [2, 12, 27, 10, 25]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            ss.Player.overwrite(f"\033[{locations[i]}H"+lines[i][:j])
            time.sleep(0.001)
        input("\n\n\n")
        if(i == 2):
            ss.Player.clear_screen()

    ss.Player.clear_screen()
    ss.Player.overwrite("\033[13;H"+s.Fore.YELLOW) 
   
    lines = """
$$$$$$$$\ $$$$$$$$\ $$$$$$$\  $$\      $$\ $$$$$$\ $$\   $$\  $$$$$$\  $$\         ┌┼┐    
\__$$  __|$$  _____|$$  __$$\ $$$\    $$$ |\_$$  _|$$$\  $$ |$$  __$$\ $$ |        └┼┐    
   $$ |   $$ |      $$ |  $$ |$$$$\  $$$$ |  $$ |  $$$$\ $$ |$$ /  $$ |$$ |        └┼┘                 ┌┼┐
   $$ |   $$$$$\    $$$$$$$  |$$\$$\$$ $$ |  $$ |  $$ $$\$$ |$$$$$$$$ |$$ |                            └┼┐
   $$ |   $$  __|   $$  __$$< $$ \$$$  $$ |  $$ |  $$ \$$$$ |$$  __$$ |$$ |                ┌┼┐         └┼┘
   $$ |   $$ |      $$ |  $$ |$$ |\$  /$$ |  $$ |  $$ |\$$$ |$$ |  $$ |$$ |                └┼┐
   $$ |   $$$$$$$$\ $$ |  $$ |$$ | \_/ $$ |$$$$$$\ $$ | \$$ |$$ |  $$ |$$$$$$$$\           └┼┘
   \__|   \________|\__|  \__|\__|     \__|\______|\__|  \__|\__|  \__|\________|      
                                                                                                     
                                $$\      $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\  $$\       $$\     $$\   
         ┌┼┐                    $$$\    $$$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$ |      \$$\   $$  |  
         └┼┐                    $$$$\  $$$$ |$$ /  $$ |$$$$\ $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ |       \$$\ $$  /   
         └┼┘                    $$\$$\$$ $$ |$$ |  $$ |$$ $$\$$ |$$ |  $$ |$$$$$$$  |$$ |  $$ |$$ |        \$$$$  /    
                   ┌┼┐          $$ \$$$  $$ |$$ |  $$ |$$ \$$$$ |$$ |  $$ |$$  ____/ $$ |  $$ |$$ |         \$$  /     
                   └┼┐          $$ |\$  /$$ |$$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |          $$ |      
                   └┼┘          $$ | \_/ $$ | $$$$$$  |$$ | \$$ | $$$$$$  |$$ |       $$$$$$  |$$$$$$$$\     $$ |      
                                \__|     \__| \______/ \__|  \__| \______/ \__|       \______/ \________|    \__|                                                                                                                                                                                                                                         
"""

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            print(lines[i][j], end="")
            time.sleep(0.001)
    input()
    ss.Player.clear_screen()

    print(ss.Fore.CYAN + """ 
 __          __  _               _       _           _______   __  __   ___  
 \ \        / / | |             | |     (_)         |__   __| |  \/  | |__ \ 
  \ \  /\  / /  | |__     __ _  | |_     _   ___       | |    | \  / |    ) |
   \ \/  \/ /   | '_ \   / _` | | __|   | | / __|      | |    | |\/| |   / / 
    \  /\  /    | | | | | (_| | | |_    | | \__ \      | |    | |  | |  |_|  
     \/  \/     |_| |_|  \__,_|  \__|   |_| |___/      |_|    |_|  |_|  (_)    """)
    
    input("\n\n\n")

    print(ss.Fore.MAGENTA + """
  _    _                            _                          _   _                                 _      ___  
 | |  | |                          | |                        (_) | |                               | |    |__ \ 
 | |__| |   ___   __      __     __| |   ___     ___   ___     _  | |_    __      __   ___    _ __  | | __    ) |
 |  __  |  / _ \  \ \ /\ / /    / _` |  / _ \   / _ \ / __|   | | | __|   \ \ /\ / /  / _ \  | '__| | |/ /   / / 
 | |  | | | (_) |  \ V  V /    | (_| | | (_) | |  __/ \__ \   | | | |_     \ V  V /  | (_) | | |    |   <   |_|  
 |_|  |_|  \___/    \_/\_/      \__,_|  \___/   \___| |___/   |_|  \__|     \_/\_/    \___/  |_|    |_|\_\  (_)  """)
    
    input("\n\n\n")

    print(ss.Fore.LIGHTRED_EX + """
 __          __  _               _                  _   _   _     _____                    _       _                   _           ___  
 \ \        / / | |             | |                (_) | | | |   |_   _|                  | |     | |                 | |         |__ \ 
  \ \  /\  / /  | |__     __ _  | |_    __      __  _  | | | |     | |       __ _    ___  | |_    | |_    ___       __| |   ___      ) |
   \ \/  \/ /   | '_ \   / _` | | __|   \ \ /\ / / | | | | | |     | |      / _` |  / _ \ | __|   | __|  / _ \     / _` |  / _ \    / / 
    \  /\  /    | | | | | (_| | | |_     \ V  V /  | | | | | |    _| |_    | (_| | |  __/ | |_    | |_  | (_) |   | (_| | | (_) |  |_|  
     \/  \/     |_| |_|  \__,_|  \__|     \_/\_/   |_| |_| |_|   |_____|    \__, |  \___|  \__|    \__|  \___/     \__,_|  \___/   (_)  
                                                                             __/ |                                                      
                                                                            |___/                                                       """)
    input()

    ss.Player.clear_screen()

    print(ss.Fore.LIGHTYELLOW_EX + """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X
X  X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X  X 
X X X X X X X X X X X X X X X X X  ______   X X X X X X X X X X X X X X X X
X  X X X X X X X X X X X X X X  .-"      "-.   X X X X X X X X X X X X X  X 
X X X X X X X X X     X X X X  /            \   X X X X X X X X X X X X X X              _     _                    _      _                   _ 
X  X X X X X X X   _   X X X  |              | X X X X  _  X X X X X X X  X      /\     | |   | |                  | |    (_)                 | |
X X X X X X X X   ( \   X X   |,  .-.  .-.  ,|  X X    / )  X X X X X X X X     /  \    | |_  | |_    __ _    ___  | | __  _   _ __     __ _  | |
X  X X X X X X X   > "=._     | )(__/  \__)( |     _.=" <  X X X X X X X  X    / /\ \   | __| | __|  / _` |  / __| | |/ / | | | '_ \   / _` | | |
X X X X X X X X   (_/"=._"=._ |/     /\     \| _.="_.="\_)  X X X X X X X X   / ____ \  | |_  | |_  | (_| | | (__  |   <  | | | | | | | (_| | |_|
X  X X X X X X X         "=._ (_     ^^     _)"_.="        X X X X X X X  X  /_/    \_\  \__|  \__|  \__,_|  \___| |_|\_\ |_| |_| |_|  \__, | (_)
X X X X X X X X X X X X X    "=\__|IIIIII|__/="   X X X X X X X X X X X X X                                                             __/ |    
X  X X X X X X X X X X X    _.="| \IIIIII/ |"=._   X X X X X X X X X X X  X                                                            |___/     
X X X X X X X X   _     _.="_.="\          /"=._"=._     _  X X X X X X X X
X  X X X X X X   ( \_.="_.="     `--------`     "=._"=._/ )  X X X X X X  X 
X X X X X X X X   > _.="      X X X X X X X X X     "=._ <    X X X X X X X
X  X X X X X X X (_/   X X X X X X X X X X X X X X X X  \_)  X X X X X X  X 
X X X X X X X X     X X X X X X X X X X X X X X X X X X     X X X X X X X X
X  X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X  X 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""")

    input("\n\n\n")

    print(ss.Fore.LIGHTGREEN_EX + """

                                  _____           
                          _____  |K  WW|          
                  _____  |Q  ww| | ^ {)|                 
           _____ |J  ww| | ^ {(| |(.)%%| _____
          |10 ^ || ^ {)| |(.)%%| | |%%%||A .  |
          |^ ^ ^||(.)% | | |%%%| |_%%%>|| /.\ |
          |^ ^ ^|| | % | |_%%%O|        |(_._)|
          |^ ^ ^||__%%[|                |  |  |           _____            _                    _ 
          |___0I|                       |____V|          |  __ \          | |                  | |
                                     _____               | |__) |   ___   | | __   ___   _ __  | |
         _____                _____ |6    |              |  ___/   / _ \  | |/ /  / _ \ | '__| | |
        |2    | _____        |5    || & & |              | |      | (_) | |   <  |  __/ | |    |_|
        |  &  ||3    | _____ | & & || & & | _____        |_|       \___/  |_|\_\  \___| |_|    (_)
        |     || & & ||4    ||  &  || & & ||7    |
        |  &  ||     || & & || & & ||____9|| & & | _____
        |____Z||  &  ||     ||____S|       |& & &||8    | _____
               |____E|| & & |              | & & ||& & &||9    |
                      |____h|              |____L|| & & ||& & &|
                                                  |& & &||& & &|
                                                  |____8||& & &|
                                                         |____6|      
""")
    
    input("\n\n\n")
    ss.Player.clear_screen()
    print(ss.Fore.LIGHTGREEN_EX + """                                                                                                                           
                                                                                =@####@                                                    @@@@@#  
                 +#%%%%%%%@     =%%%%#######*    +%%+           *%%#          *%%%%%%@@@@*                                                @@- :@*:=
                @@@@%**@%%@@    #@@@@%%%%%%%*    #@@%           #@@#          #+      @@@@*                                              .@@.  @@@@
               @@@%             #@@@             #@@%           #@@#                    @@%                                              +@@.  +@@@
               #@@@             #@@%             #@@%           #@@#                    @@%                                             .@@@      .
               +@@@@#           #@@@             #@@%           #@@#                   @@@#                                          : +@@*        
                 #@@@@%%%       #@@@%##%%%%*     #@@%           #@@#              ##%@@@%#                                      #@@@@@@@@             
                    %%@@@@%#    #@@@@%%%%%%+     #@@%           #@@#              %@@@%                                        @@=   .:.           
                       +%@@@#   #@@@             #@@%           #@@#              %@@                                         =@+                  
                         @@@%   #@@%             #@@%           #@@#              *%%                               ++:*@@:  %@@                   
                         @@@#   #@@@             #@@@           #@@%                                              @@@@@@@@@*@@@                    
               @%%%@  #@@@@%    #@@@@%%%####+    #@@@%######+   #@@@%######+     -%%%#                           .@%    *@@@@#                     
               @%%%@@@#%%%=     #%%%%%%%%%%%#=   -%%%%%%%%%%%:  +%%%%%%%%%%*     #%%%+                           @@*       ++                      
                                                                                                                 @@                                
                                                                                                      .        .@@.                                
                                                                                                   +@@@@      .@@.                                 
                                                                                                 =@@* -@#+ -@@@@                                   
                                                                                             :@@@*     *@@@@*                                      
                                                                                             @@@        @@@                                        
                                                                                            @@#                                                    
                                                                                           @@.                                                     
                                                                                       :.@@%                                                       
                                                :--                           @@@@@= =@@@+                                                         
                                               @@@@@#=:                   .+@@@    @@@@=                                                           
                                              =@@ -%@@@@                .@@@=                                                                      
                                             .@@.   :#@@@%          .@#.#@@                                                                        
                                            +@@      -@@@@          @@@@@@                                                                         
                                        @@@@@@:       *@@@*        .@@@@@@                                                                         
                                      :@@-              %@@        +@+-@@%         *%%%%%%%%%*        *%#*          *%*   =#%*        #%%#*     @@@
                                     =@@                +@@        %@  @@-         %@@@####%@@@#      %@@@          %@%    %@@%       @@@+      @@@
                                   @@@+                  @@#     =@@%              %@@       @@@#     %@@@          %@%     @@@%     @@@#       @@@
                           @@@#-  -@%                    @@@@@@@@@@*               %@%       @@@#     %@@@          %@%     %@@@%   @@@@        @@@
                         .@@@@.@@*@@=                     @@@@@@@@                 %@@      #@@%      %@@@          %@%       @@@* #@@%         %@@
                         @@= @@@@@@@                      -@@@%+                   %@@@%#%%@@@@       %@@@          %@%       %@@@@@@%          @@@
                        @@     %@@@=                        .                      %@@%%%%#%%@@@*     %@@@          %@%        @@@@@%           @@@
                       @@*      @@@                                                %@@       @@@@*    %@@@          @@%         @@@@            @@@
                      +@@                                                          %@%        *@@%    %@@@         %@@%         %@@%            @@@
                      %@=                                                          %@@        @@@#    +@@@        #@@@#         %@@%               
                  @@@@@+                                                           %@@%*@%%%#@@@%      %@@@@#+ *#%@@@*          %@@%            @@@
                 @@%-                                                              *%%%%%#%%%%%=         @%%%###%%%#            *%%*            @@@
               -@@+                                                                                                                                        
              %@@.                                                                                                                                                
                                                                                                                                       """)

    input()
    ss.Player.clear_screen()
    print(ss.Fore.LIGHTBLUE_EX + """                                                   
                                                                                   ▒██        █                                                      
                                                                                 ████         █              █                                       
                                       ░███████████████████████    ░██▒     █ ▓██                           █      █                                 
                                ▓██                             ▓████   █  ███▓█               ░           ▓       █                                 
                            ██    ░█████████████████████ █  ░█████ █  █     █░ █ █             █                             ███████                 
                         █    ████▓▓░▓▓░█   ░█ ██ ▒  █ █  ██         ██      █ █  ██           █          █       █                   █▓             
                      █   ████▓░ ▒ █ █   ▒ ░█  ██ ████  █     ▒█  ▓░▓█                         █         █               █               █           
                   █   ███▓  ▒ █   █ █ █ █  █           ██░ ███   █▓████   █                   █        █        █      █                 █          
                 █  ███░░░▒██▒ ▓ █     █ █  █   ██████      ██  ████    ▓██                    █                ▒                         █          
               █  ███░░ ▒█ █       ██  █ █    ███          ███       ████                              ▒        █     █                              
     █████▓  ▒  ██▒░▒ ▓██      ███    ██ █▒░▒▓█ ██  █            █████▒                         █    █          █    █                               
  █ ██     ░  ██▓ ░▒ ▓█   ██          ██  █▓▓██      █      ████████                             ████           ▓                                    
   █▒█ ▓██  ██▓   █    ███  █         █░ █ ██ ▒   █      ███▓▓ █ █                                                                        █          
    ██ ██  ██░░▒▒▒█ █████        █ ▒  █    █      █   ████  ▓███                                                                          █          
     ██▒ ██░ ▓ █    █      ░           █                  ███                                                                            █           
     █  ██░▒▒░█ ▓ █ ██▓  █   ██          ███  █        ██                                                                               █            
       ▓░▒      ██       █     █  ██     █▒██    ░████  █  █                                                                           █             
    ░█▒  ▒ █ ███      █     ▓█          █ █     ▓███ ▒▓▓█  █                                                                          █              
   █ ▒░▒▓ █░ █  ██  █   ▓██   ░  ▒   ░░█     ████    █░█   █                                                                         █               
  █ ▓   ▒ █ ░       ██               ██▒   ███         █   █                                                                       ▓█                
   ▒▒▒▒  █ █ ▒█           ▓ █       ▒   ███                                                                                        █                 
 █ █░ ▓ █ ██  █ ▒ ██ ▒            █    █ █                                                                                       ░█                  
  ▓░░█            ▒     ██           ██                   ______   _         _       _                   _                        █                    
  █▒▒█   ███ █▓ ▒ █           ██ ███                     |  ____| (_)       | |     (_)                 | |                      █      ██ █           
  █   ▒██              ░█  ███  █                        | |__     _   ___  | |__    _   _ __     __ _  | |                    ▒█  ██████▒▓██          
 ░█ ▓█ ░  ██ ██      █  ███                              |  __|   | | / __| | '_ \  | | | '_ \   / _` | | |                   █▒      ░    █           
  █▒ █ █   █      ██████  █▒                             | |      | | \__ \ | | | | | | | | | | | (_| | |_|                  █       ██   ███          
  █    █       ███ █░  ███▓                              |_|      |_| |___/ |_| |_| |_| |_| |_|  \__, | (_)                ███        █   █            
  █▓ █ ▒██    █  █  ███▓▓▒                                                                        __/ |                    █▓▓█       ▒░  ██           
 ░▓█        █  ██░ ▓▒░█▓░ █                                                                      |___/                    █ ████    ██▒    ░███        
 █ █ ██ █    ███         █                                                                                                █  ░██████░        ▓         
 █ ▒      ██ █     █     ░                                                                                               ██      ░            ▒██       
  █ █       █         ▓                                                                                                  ███  ░   ▒░░          █        
   ██ ▒    ██                                                                                                        █ ░██  ███████▒          ▓█        
    ██░█  ██░▒                                                                                                      ░ ▓ █       ██            █         
     █    █  ██████  █                                                                                                            █░         █         
      ██▒     ▒░     █                                                                                                            █░       ░██         
        ██  ██▒▒█▓   █░                                                                                                            ░       ▒█          
           █░  ▓    ███                                                                                                          ██░       █           
            █░░    █▒█                                                                                                          ██░       ░█           
            █░█   ██ █                                                                                                         ██        ░██           
             █ ░    ▓█                                                                                                        ██         █             
              █    ██                                                                                                         █          █             
               ██  ██                                                                                                  █   █ ██          ██   █        
                 ███                                                                                              █  █       █████████████      █  █   
                  ░                                                                                                     █  █▓             ▒  █░        """)
    input()

    ss.Player.clear_screen()

    ss.Player.overwrite(ss.Fore.LIGHTRED_EX + """
                         _                                _                                        _                                         
     /\                 | |                              | |                                      | |                                        
    /  \     _ __     __| |    _ __ ___    _   _    ___  | |__          _ __ ___    _   _    ___  | |__      _ __ ___     ___    _ __    ___ 
   / /\ \   | '_ \   / _` |   | '_ ` _ \  | | | |  / __| | '_ \        | '_ ` _ \  | | | |  / __| | '_ \    | '_ ` _ \   / _ \  | '__|  / _ \\
  / ____ \  | | | | | (_| |   | | | | | | | |_| | | (__  | | | |  _    | | | | | | | |_| | | (__  | | | |   | | | | | | | (_) | | |    |  __/
 /_/    \_\ |_| |_|  \__,_|   |_| |_| |_|  \__,_|  \___| |_| |_| ( )   |_| |_| |_|  \__,_|  \___| |_| |_|   |_| |_| |_|  \___/  |_|     \___|
                                                                 |/                                                                          
                                                                                                                                             """)
    
    input()
    print(ss.Fore.LIGHTGREEN_EX + """
                                                   ___________    ____
                                            ______/   \__//   \__/____\\
                                          _/   \_/  :           //____\\\\
                                         /|      :  :  ..      /        \\
                                        | |     ::     ::      \        /           ▓██   ██▓ ▒█████   █    ██ 
                                        | |     :|     ||     \ \______/             ▒██  ██▒▒██▒  ██▒ ██  ▓██▒
                                        | |     ||     ||      |\  /  |               ▒██ ██░▒██░  ██▒▓██  ▒██░
                                         \|     ||     ||      |   / | \              ░ ▐██▓░▒██   ██░▓▓█  ░██░
                                          |     ||     ||      |  / /_\ \             ░ ██▒▓░░ ████▓▒░▒▒█████▓ 
                                          | ___ || ___ ||      | /  /    \             ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ 
                                           \_-_/  \_-_/ | ____ |/__/      \          ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░ 
                                                        _\_--_/    \      /          ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░ 
                                                       /____             /           ░ ░         ░ ░     ░     
                                                      /     \           /            ░ ░                       
                                                      \______\_________/
""")
    print("Type exit to quit")