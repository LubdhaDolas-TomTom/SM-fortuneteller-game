import random
luckdate = random.randint(1,31)
namebank = []
first = ["Anagh ", "Madhavi ", "Shashi ","Megha " , "Santosh" ,"Martin ","Rob ","Lubdha "]
lastname = ["Ant-Man,","The Avenger,","Batman,","Black Panther,","Captain America,","Doctor Strange,","Iron Man,"]
rand = random.randint(0,8)
randname = first[rand]+ "" + lastname[rand]
namebank.append(randname)
luckyText = " "

luckyTextNumber = random.randint(1,9)
if luckyTextNumber == 1:
 luckyText = "today is a good day to plan new things and work on them"

if luckyTextNumber == 2:
   luckyText = "Your day will end with a smile"  

if luckyTextNumber == 3:
   luckyText = "You are advised to be a little hotter right now so that you can understand what really makes you feel better. It is a good time to make big moves."

if luckyTextNumber == 4:
   luckyText ="One of the most positive of the star signs is you Sagittarius,Lucky you"

if luckyTextNumber == 5:
   luckyText ="will be free and come out from this messy situation"


if luckyTextNumber == 6:
   luckyText = "You will meet and enjoy company with your loved once"

if luckyTextNumber == 7:
   luckyText = "today is your day, what you wish will come true"

if luckyTextNumber == 8:
   luckyText = "Today you will have a great day, alot of work and work that will payoff"

if luckyTextNumber == 9:
   luckyText = "No need to Think of today , just enjoy"

print(f"Hello {randname} {luckyText}. Your lucky number is {luckdate}")
