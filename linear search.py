#list = [4, 9, 12, 17, 23, 43]
list = ["bangkok", "dublin", "vilnus", "warsaw"]
#search = int(input("enter the number to search for: "))
search = input("enter a capital of a country to search for: ")
ind = 0
flag = False
while ind <= len(list) - 1:
    if search == list[ind]:
        flag = True
        #print("the number has been found", ind)
        print("this capital has been found", ind)
        break
    else:
        ind += 1
else:
    if flag == False:
       #print("the number has not been found")
       print("this capital has not been found")