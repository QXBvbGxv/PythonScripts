#Binary and Denary translator
#Program by QXBvbGxv
#I hope you like it :)
#Ignore my crapy variables


while True: #Script won't end
    i = input('1 for b to d and 0 for d to b: ')
    # '1' translates from Binary to Deanry
    # '0' translates from Denary to Binary

    #Binary to Denary script
    if i == '1':
        #initiation stuff
        n = 1
        e = 0
        i = input('') #Type any Binary sequence in (with spaces between 1's and 0's)
        l = i.split()
        for b in l[::-1]:
            if b == '1':
                e = e + n
            n = n * 2
        print(e)
        print('')

    #Denary to Binary  
    elif i == '0':
        #Initiation stuff
        a = True
        l = [1]
        r = 1
        s = []
        o = 0
        i = int(input('')) #Type any number in
        #This bit (below) will make the script be able to have no maximum
        while a == True:
            for yeet in range(1):
                r = r * 2 #This is the sequence for binary "1, 2, 4, 8, 16..."
                l.append(r)
                o = 0
                s = [] 
            for n in l[::-1]: #Read the sequence for binary
                if n + o <= i:
                    s.append('1') #Add a 1
                    o = o + n
                elif n + o > i:
                    s.append('0') #Add a 0
            if o == i:
                a = False
        #Prints out everything
        for x in s:
            print(x + ' ', end='')
        print('')
        print('')
