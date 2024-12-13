#list = [10, 20, 30, 40, 60, 70, 80, 90, 100]
list = ["bangkok", "berlin", "dublin", "vilnus"]
low = 0
high = len(list)-1
#search = int(input("please enter a number to search for: "))
search = input("please enter a capital of a country to search for: ")
flag = False
while low <= high:
    mid = (low + high) // 2
    if list[mid] == search:
        flag = True
        #print("number has been found", mid)
        print("capital has been found")
        break
    elif list[mid] < search:
        low = mid + 1
    else:
        high = mid - 1
else:
    if flag == False:
        #print("number has not been found")
        print("capital has not been found")
        
        