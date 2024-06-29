min_len = int(input("Enter minimum length of password : "))
max_len = int(input("Enter maximum length of pasword: "))
counter=0
characters = ['0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
             
file_open = open("wordlist.txt","w")

for i in characters:
    for j in characters:
        for k in characters:
            for l in characters:
                guess = str(i) + str(j) + str(k) + str(l)
                file_open.write(guess)
                file_open.write('\n')
                counter+=1
print("wordlist of {} passwords created".format(counter))