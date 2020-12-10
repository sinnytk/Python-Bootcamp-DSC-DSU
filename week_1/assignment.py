# Assignment # 1
## function to print a string diagonally
name = input('Enter Your Name:')
def diagonalPrint(name):
    print(f'Name is: {name}')
    print('\nYour name diagonaly print as: ')
    for i in range(len(name)):
        if(i == 0):
            print(name[i])
        else:
            print(' '*(i-1),name[i])
diagonalPrint(name)

## function to print a string reverse diagonally
def reverseDiagonalPrint(name):
    print('\nYour name reverse diagonaly print as: ')
    for i in range(len(name),-1,-1):
        if(i == 0):
            print(name[i])
        else:
            print(' '*(i-1),name[i-1])
reverseDiagonalPrint(name)

# Assignment 2
## Create a program to take as input 5 student records:


# Assignment 3
## A function that will print lyrics of given song with 1 second delay between each line.
song = "Tere Jaane Ka Gam,Aur Na Aane Ka Gam, Phir Zamaane Ka Gam, Kya Karein?, Meri Dehleez Se Hokar, Bahaarein Jab Gujarti Hai, Yahan Kya Dhup Kya Saawan, Hawayein Bhi Barashti Hai, Hume Puchhon Kya Hota Hai, Bina Dil Ke Jiye Jaana, Bahot Aayi Gayi Yaadein, Magar Iss Baar Tum Hi Aana"
def printSong(song):
    import time 
    songparagraph = song.split(', ')
    print('Your Song is:')
    for i in range(len(songparagraph)):
        print(songparagraph[i])
        time.sleep(1)
printSong(song)