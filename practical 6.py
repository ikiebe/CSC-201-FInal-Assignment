def main():
#line 3 and 4 is to initialise our variables
    scores= []
    students= []
#line 6 to 20 is a loop to check our function given
    while True:
        name = input("enter students name (or press enter to finish):")
        if name == "":
            break
        score= int(input("enter students exam score:"))
        if score== 999 or score > 100:
             break
    students.append(name)
    scores.append(score)
#line 16 and 17 is to count the class average
    if len(scores)> 0:
        class_average = sum(scores)/ len(scores)
# the remaining code is to print our output
        print("\nstudents report")
        for i in range(len(students)):
                print("{}:{}".format(students[i],scores[i]))
        print("\n class average score is:{:.2f}".format(class_average))
    else:
        print("no data enetered")
#this is to close the function we defined
if __name__ == "__main__":
    main()