# %%
# imports and variables
import subprocess
new_name = ""
updated_name = ""

# functions
subprocess.run(["powershell", "pwd"], shell=True)

#  rename
def rename_file(newname):
    subprocess.run(["powershell", "Rename-Item subtitle.txt \"{}\"".format(updated_name)])

#  move
def move_file(newname):
    subprocess.run(["powershell", "Move-Item \"{}\" toupload".format(newname)])

print("                        :=*+=-. :##*=.=+-*.   .                \n"
    "                     -====-::+####==##+#*####=  +-                 \n"
    "                  .::-=###############+ .+####+ =#=                \n"
    "              :+*###+-:::=*##+:::-*#####=.+####-=##:               \n"
    "                :-+*##*++*#####*+=+#############*##=               \n"
    "         .-=*############################****######+               \n"
    "        .:+##*++###*=--=*###*=:::=**=:.       .-+###+:             \n"
    "        -**: .:=##*===+*###+  .--.                -*###=:.         \n"
    "      -####################:  *##*.      :*#*:      .=*####*+++**=.\n"
    "     -----+#######*########+...::.       +###*          :-=++#####=\n"
    "     .-+#######*: -##########+----        :-:               :*##*= \n"
    "  .-*###*+=+##*:-*##############=:                      .-=*###-   \n"
    "   .+#*: :+##########*::######+:..           .:=++++++*#####+:     \n"
    "  -###**####++######+ .*####*-..               .:-=*#####*.        \n"
    " +###+*###*. *######-=#####+:..              ..::+###+-*##+        \n"
    "==:.-*####.:*###*-########=...            .::::-###=    +##*       \n"
    "  :*###=*#*####* .#######=...           .:----=###:      +##+      \n"
    "-------------------------------------------------------------------\n"
    "             HackHog's .txt renamer and mover 1.02\n"
    "-------------------------------------------------------------------\n\n")

# actual code

new_name = input("What do you want to name the new file? ")
if new_name == "exit":
    quit()
updated_name = "{}.txt".format(new_name)
rename_file(updated_name)
move_file(updated_name)
print("Success! Thank you for using my tool!")