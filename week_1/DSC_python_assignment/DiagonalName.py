from colorama import Fore,Style
sp=""
s=input("Please Enter your name: ")
for i in range(len(s)):
    for j in range (i+1):
        print(Fore.LIGHTMAGENTA_EX+sp+s[i])
        sp+="  "
        break
print (Style.RESET_ALL)
