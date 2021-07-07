#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", )
name = f.readline()

f_invited_names = open("../Mail Merge Project Start/Input/Names/invited_names.txt")
i = 1
line = True
while line:
    line = f_invited_names.readline(i)
    i += 1
    print(line)




