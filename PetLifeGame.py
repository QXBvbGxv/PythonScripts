import os
import time


#Different variables for Intro
nameSet = False
ageSet = False
happinessSet = False
hungerSet = False
thirstSet = False
cleanlinessSet = False
fatigueSet = False
logInTime = time.time()
justOpened = True
TimeSinceLogOut = 0

hasDied = False

#Pet name
petName = ''

#Life Variables
happiness = 75
hunger = 75
thirst = 75
cleanliness = 75
fatigue = 75

#Dead Function
def death_function(name):
    print('You did not take care of ' + name + ' and it has died')
    print('Your save file will now be deleted')
    print('Thank you for playing')
    os.remove('save.txt')
    hasDied = True
    return hasDied



#Open File

print('Welcome to Petlife')
print('Press ENTER to start or type "/delete" to delete your current pet')
print('Type "/exit" to stop program')
inp = input('>>> ')
if inp == '/delete':
    print('Are you sure? y/n: ')
    deleteCheck = input('>>> ')
    if deleteCheck == 'y':
        os.remove('save.txt')
        print('Save deleted')
    print('Type ENTER to start a new pet or tpe "/exit" to stop program')
    inp = input('>>> ')
with open('./save.txt', 'a+') as saveFile:
    while inp != '/exit':

        #Intro:
        if justOpened == True:

            for Line in open('./save.txt', 'r'):
                
                #Intro: Check if there is a name if so display it
                if 'Name' in Line:
                    print('Pet name: ' + Line[5:-1])
                    petName = Line[5:-1]
                    nameSet = True

                #Intro: Check if there is an age/Birthday if so display it  
                if 'Age' in Line:
                    birthEpoch = float(time.time()) - float(Line[4:-1])
                    birthEpochTime = float(Line[4:-1])
                    print('Pet age: ' + str(round(birthEpoch)) +' seconds old')
                    ageSet = True

                if 'LogOutTime' in Line:
                    TimeSinceLogOut = float(logInTime) - float(Line[11:-1])
                    print('You have been offline for ' + str(round(TimeSinceLogOut)) + ' seconds')
                    deductionAmount = round(TimeSinceLogOut / 300)

                if 'Happiness' in Line:
                    happiness = int(Line[10:-1])
                    happiness -= deductionAmount
                    print(petName + '\'s happiness = ' + str(happiness))
                    happinessSet = True
                
                if 'Hunger' in Line:
                    hunger = int(Line[7:-1])
                    hunger -= deductionAmount
                    print(petName + '\'s hunger = ' + str(hunger))
                    hungerSet = True

                if 'Thirst' in Line:
                    thirst = int(Line[7:-1])
                    thirst -= deductionAmount
                    print(petName + '\'s thirst = ' + str(thirst))
                    thirstSet = True

                if 'Cleanliness' in Line:
                    cleanliness = int(Line[12:-1])
                    print(petName + '\'s cleanliness = ' + str(cleanliness))
                    cleanlinessSet = True

                if 'Fatigue' in Line:
                    fatigue = int(Line[8:-1])
                    fatigue += deductionAmount
                    print(petName + '\'s fatigue = ' + str(fatigue))
                    fatigueSet = True

                #print(happiness, hunger, thirst, cleanliness, fatigue)
            
            #Intro: If there is no name set one
            if nameSet == False:
                print('Give your pet a name')
                petName = input('>>> ')
                print('Name ' + petName + '\n', file=saveFile)
                nameSet = True

            #Intro: If there is no age stuff set 
            if ageSet == False:
                birthEpoch = time.time()
                birthEpochTime = birthEpoch
                print('Age ' + str(birthEpoch) + '\n', file=saveFile)
                ageSet = True

            #Intro: all other sets
            if happinessSet == False:
                print('Happiness ' + str(happiness) + '\n', file=saveFile)
                happinessSet = True

            if hungerSet == False:
                print('Hunger ' + str(hunger) + '\n', file=saveFile)
                hungerSet = True

            if thirstSet == False:
                print('Thirst ' + str(thirst) + '\n', file=saveFile)
                thirstSet = True

            if cleanlinessSet == False:
                print('Cleanliness ' + str(cleanliness) + '\n', file=saveFile)
                cleanlinessSet = True

            if fatigueSet == False:
                print('Fatigue ' + str(fatigue) + '\n', file=saveFile)
                fatigueSet = True

            justOpened = False

        #Check if dead
        if happiness <= 0:
            death_function(petName)
        if hunger <= 0:
            death_function(petName)
        if thirst <= 0:
            death_function(petName)
        if cleanliness <= 0:
            death_function(petName)
        if fatigue <= 0:
            death_function(petName)

        inp = input('>>> ')

        #Help
        if inp == '/help':
            print('These are the commands that you can use')
            print('"/help" - list different commands')
            print('"/eat" - feed your pet food')
            print('"/drink" - feed your pet water')
            print('"/clean" - clean your pet')
            print('"/play" - play with your pet')
            print('"/stat" - see your pet\'s stats')

        #Take care of your pet
        if inp == '/eat':
            print('You fed ' + petName + '!')
            hunger += 25

        if inp == '/drink':
            print('You gave ' + petName + ' a drink!')
            thirst += 25

        if inp == '/clean':
            print('You cleaned ' + petName + '!')
            cleanliness += 25
            happiness += 15

        if inp == '/play':
            print('You played with ' + petName + '!')
            happiness += 25
            cleanliness -= 25
            thirst -= 15
            hunger -= 10
            fatigue -= 20
        
        if inp == '/stat':
           print('Name: ' + petName)
           print('Pet age: ' + str(round(birthEpoch)) + ' seconds old')
           print(petName + '\'s happiness = ' + str(happiness))
           print(petName + '\'s hunger = ' + str(hunger))
           print(petName + '\'s thirst = ' + str(thirst))
           print(petName + '\'s cleanliness = ' + str(cleanliness))
           print(petName + '\'s fatigue = ' + str(fatigue))


        if hunger > 100:
            hunger = 100
        if thirst > 100:
            thirst = 100
        if cleanliness > 100:
            cleanliness = 100
        if happiness > 100:
            happiness = 100
        
        if hasDied == True:
            inp = '/exit'
        
#Log out time
logOutTime = time.time()
        
    #Append all changes
with open('./save.txt', 'w') as saveFile:
    print('', file=saveFile)
    print('Name ' + petName + '\n', file=saveFile)
    print('Age ' + str(birthEpochTime) + '\n', file=saveFile)
    print('LogOutTime ' + str(logOutTime) + '\n', file=saveFile)
    print('Happiness ' + str(happiness) + '\n', file=saveFile)
    print('Thirst ' + str(thirst) + '\n', file=saveFile)
    print('Cleanliness ' + str(cleanliness) + '\n', file=saveFile)
    print('Fatigue ' + str(fatigue) + '\n', file=saveFile)
