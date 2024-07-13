import pyttsx3
engine = pyttsx3.init()

wlc = 'WELCOME TO THE QUIZ GAME'
print(wlc)
engine.say(wlc)
engine.runAndWait()

import time
for seconds in range(5,0,-1):
    print(seconds)
    engine.say(seconds)
    engine.runAndWait()

#1st block

info1 = 'Your First Question Is:'
print(info1)
engine.say(info1)
engine.runAndWait()

que1= 'What is the capital of Nepal?'
print(que1)
engine.say(que1)
engine.runAndWait()

opt1 ='a.Siraha\nb.Birgunj\nc.Kathmandu\nd.None'
print(opt1)
engine.say(opt1)
engine.runAndWait()

score = 0

ans1 = input('Enter your answer:').lower()

if ans1 == 'Kathmandu'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()

#2nd block

info = 'Your Second Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'What is the largest mammal?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. Elephant\nb. Blue whale\nc. Lion\nd. Giraffe'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == 'Elephant'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()

#3rd part

info = 'Your Third Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'What is the chemical symbol for gold?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. Au\nb. Ag\nc. Hg\nd. fe'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == 'Au'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()
    
#4th part

info = 'Your Fourth Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'Who wrote Romeo and Juliet?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. William Shakespeare\nb. Jane Austen\nc. Mark Twain\nd. Charles Dickens'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == 'William Shakespeare'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()
    
#5th part

info = 'Your Fifth Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'How many continents are there?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. 5\nb. 6\nc. 7\nd. 8'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == '7'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()
    
#6th part

info = 'Your sixth Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'What is the powerhouse of the cell?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. Mitochondria\nb. Nucleus\nc. Chloroplast\nd. Ribosome'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == 'Mitochondria'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()
    
#7th part

info = 'Your seventh Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'What is the largest planet in our solar system?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. Jupiter\nb. Saturn\nc. Earth\nd. Mars'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == 'jupiter'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()
    
#8th part

info = 'Your Eighth Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'What is the national animal of China?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. Panda\nb. Tiger\nc. Dragon\nd. Elephant'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == 'Dragon'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()
    
# 9th part

info = 'Your ninth Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'Which country is known as the Land of the Rising Sun?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. Japan\nb. China\nc. India\nd. South Korea'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == 'japan'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()
    
#10th part

info = 'Your Tenth Question Is:'
print(info)
engine.say(info)
engine.runAndWait()

que= 'Who painted the Mona Lisa?'
print(que)
engine.say(que)
engine.runAndWait()

opt ='a. Vincent van Gogh\nb. Leonardo da Vinci\nc. Pablo Picasso\nd. Michelangelo'
print(opt)
engine.say(opt)
engine.runAndWait()

ans = input('Enter your answer:').lower()

if ans == 'Leonardo da Vinci'.lower():
    score += 1
    say1=('Congratulations! you won '+ str(score)+' Point')
    print(say1)
    engine.say(say1)
    engine.runAndWait()
else:
    say2 = 'Oops! Wrong Answer'
    print(say2)
    engine.say(say2)
    engine.runAndWait()
    
total = 'Your Total Score is '+ str(score)+' Out of 10'
print(total)
engine.say(total)
engine.runAndWait()