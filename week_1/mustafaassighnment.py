def diagonal():
    string = input('please inpyt your string:')
    for i in range(len(string)):
        print(f'{" " * i}{string[i]}')
total=[]
def highestfunc():
    highest = 0
    id = 0
    if(x==int(num)-1):
     for i in range(int(num)):
        if (int(total[i].get("marks")) > int(highest)):
            highest = int(total[x].get("marks"))
            id = i
     print(f'{total[id].get("name")} with rollno.{total[id].get("rollno")} got highest marks which were {total[id].get("marks")}' )
def lowestfunc():
    lowest = 101
    id = 0
    if (x == int(num)-1):
     for i in range(int(num)):
        if (int(total[i].get("marks")) < int(lowest)):
            lowest = int(total[x].get("marks"))
            id = x
     print(f'{total[id].get("name")} with rollno.{total[id].get("rollno")} got lowest marks which were {total[id].get("marks")}')
def inputrollno():
 total[x]["rollno"]=input('Enter Rollno.: ')

def inputname():
     total[x]["name"] = input('Enter Name: ')
def inputage():
    total[x]["age"]=input('Enter Age: ')
def inputmarks():
    total[x]["marks"]=input('Enter Marks: ')
def averagefunc():
    sum = 0
    if (x == int(num)-1):
     for i in range(int(num)):
        sum += int(total[i].get("marks"))
        average = sum / int(num)
     print(f'average is  {average}')

def main():
        globals()['student%s' % x] = {'name': 'not asigned1', 'age': 'not assigned', 'rollno': 'not assigned',
                                      'marks': 'not assigned'}
        total.append(globals()['student%s' % x])
        inputrollno()
        inputname()
        inputage()
        inputmarks()
        highestfunc()
        lowestfunc()
        averagefunc()
        if (x == int(num) - 1):
            print('**roll_num** |     **name**    |  **age**  | **marks**')
            for i in range(int(num)):
                print(
                    f'{total[i].get("rollno").center(13)}|{total[i].get("name").center(17)}|{total[i].get("age").center(11)}|{total[i].get("marks").center(10)}')

diagonal()
print('programn 2:')
num = input('Total students : ')
for x in range(int(num)):
    main()
print('programn 3:')
import time
print('Muntazir lyrics')
song ='''Jahan se shru ki bth vahein per akr khatam ab tk zindagi ne 
dikhein mjhe srif sitam ghumtam ghutab se me apni qismat se lurr rha tha 
(piyarr ki doOr ) KO SUlli bana kr chahr rha tha main rahoon ya na Rahoon 
tujhe fikar nhi hoti agr hoti tu kya tu meri tarha nhi rotti jece may jagta 
hoon khOoAb mein tere any k darr se ziyada tar ghr se bahir hi rehny laga me 
durr se nasha kiya milla sakOoN waqti toour ka hoNy laga seenye me dard phir 
bari zor ka phir saar ki tarf apni pistol ka nashye me intezar karoun teri 
bowl ka mera hall poch r koi bth kr galti se bhi mjhe yd kr maroun hath pair 
me rat bhr yar me aj bhi tera moutbar yaqeen kr meri bth ka me dil ka bilkul 
burra nhi hoon jahan se tune choura me aj bhi wahein khaara hOon
Chorous:
Kya ho a gar dil mein tere mjhe le kr kxh nhi hae thori thori hi sahi pr sansy 
abhi chal rhein hein Ashiq mera ek maxar r ishqi meri qaber hae dye bhi jaow ab 
hazri srif teri muntazir hein

Ankheina uddhi ek diyan dil waja marr da aja pardesiyan wasta hi pyr da saan mere tujhe se
Haye teno me pukar daa dekh lye tu ve murr kr hall ki hae yar da

Dekho ratoon me haye ek tanhai ek ajeeb se dekho adaoon me russvai ek ajeeb si q hae 
tu doour ho k bhi mere qareeb si pyar na hoto laga dollat bhi gareeb si kash by kash 
nass me by bass tu kry mjhe bay bss chal hans dye khedye yr ab un pe bhi lagy ana dye 
ab gaarab per yar ab tu hi krdye meri koi musqil assan meri is shaqus se chota dye jan 
meri q k jo jan meri wo tu mjhe janti nhi sb k sch ko sch r mere sch ko sch manti nhi 
kix kam ki yeh shikayat jab koi sunny wala hi nhi tu jabse gae hae mne moth ko kabhi 
talla nhi manzil dikh rahi hae per wahan jany ka rasta hi nhi hae log shikwa krtein hein 
kehtein hein #shariq tu hansta hi nhi hae teri masoomi meri khamoshi tujhe ab se passand 
haae na sham andhera r na khamoshi passand hae

Chorous:
Kya ho a gar dil mein tere mjhe le kr kxh nhi hae thori thori hi sahi pr sansy abhi chal rhein hein
Ashiq mera ek mazaar r ishqi meri qaber hae dye bhi jaow ab hazri srif teri muntazir hein... shouck 
thein yar kch fakirri ka kch ishq nye dar dar roll dyea kch sajna qasssar na chori thi kch zaheir
 rkhi bhan gholl diya kxh asye viranye musqil thein kch bth me ghumm ka touk bhi tha kch sheir(city) 
 k log bhi zalim thein kxh mjhe marny ka shock bhi tha


Kya ya ho a gar dil mein tere mjhe le kr kxh nhi hae thori thori hi sahi pr sansy 
abhi chal rhein hein ashiq mera ek maxar r ishqi meri qabar hae dye bhi jaow ab 
hazri srif teri muntazir hein'''
songlyr=song.splitlines()

for i in songlyr:
    time.sleep(1.5)
    print(i)    