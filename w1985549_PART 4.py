# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Westminster ID: w1985549   # Name : Thantrige Sahan Vimukthi Dharmarathne   # IIT Number :20222165
# Date: 04.21.2023
count_of_Progress = 0
count_of_trailer = 0
count_of_module_retriever = 0
count_of_Exclude = 0
Progress_of_list_1 = []
Trailer_of_list_2 = []
Module_retriever_of_list_3 = []
Exclude_of_list_4= []
Progression_outcome_Dictionary = {}
while True:
    #Getting student's Uow number as a input 
    Uow_Number = input("Enter your UoW number: ")
    try:
        #Main inputs and checking them is that they are in correct range
        Pass_credits = int(input("Enter number of Pass credits : "))
        if Pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range")
            continue
        Defer_credits = int(input("Enter number of Defer credits : "))
        if Defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range")
            continue
        Fail_credits = int(input("Enter number of Fail credits : "))
        if Fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range")
            continue

        #Checking the input total
        total = Pass_credits + Defer_credits + Fail_credits

        if total != 120:
            print("Total Incorrect")
            continue

        #Checking the progression outcomes
        elif Pass_credits == 120:
            count_of_Progress += 1
            Progress_of_list_1.append([Pass_credits, Defer_credits, Fail_credits])
            Progression_outcome_Dictionary[Uow_Number] = f"Progress - {Pass_credits}, {Defer_credits}, {Fail_credits}"
            print("Progress")
        elif Pass_credits == 100:
            count_of_trailer += 1
            Trailer_of_list_2.append([Pass_credits, Defer_credits, Fail_credits])
            Progression_outcome_Dictionary[Uow_Number] = f"Trailer - {Pass_credits}, {Defer_credits}, {Fail_credits}"
            print("Progress(module trailer)")
        elif Fail_credits >= 80:
            count_of_Exclude += 1
            Exclude_of_list_4.append([Pass_credits, Defer_credits, Fail_credits])
            Progression_outcome_Dictionary[Uow_Number] = f"Exclude - {Pass_credits}, {Defer_credits}, {Fail_credits}"
            print("Exclude")
        elif Fail_credits < 80:
            count_of_module_retriever += 1
            Module_retriever_of_list_3.append([Pass_credits, Defer_credits, Fail_credits])
            Progression_outcome_Dictionary[Uow_Number] = f"Module retriever - {Pass_credits}, {Defer_credits}, {Fail_credits}"
            print("Module retriever")

        #Checking the multiple outcomes
        continue_of_program = input("Would you like to enter another set of data ? \n Enter 'y' for yes or 'q' to quit and view results: ").lower()
        if continue_of_program == "y":
            continue
        elif continue_of_program == "q":
            break
        else:
            print("invalid input")
            continue_of_program = input("Would you like to enter another set of data ? \n Enter 'y' for yes or 'q' to quit and view results: ").lower()
    except ValueError:
        print("Integer required")

#Histogram
print("-----------------------------------------------------------------------")
print("Histogram")
print(f"Progress {count_of_Progress}", ":", "*" * count_of_Progress)
print(f"Trailer {count_of_trailer}", ":", "*" * count_of_trailer)
print(f"Retriever {count_of_module_retriever}", ":", "*" * count_of_module_retriever)
print(f"Excluded {count_of_Exclude}", ":", "*" * count_of_Exclude)
print(count_of_Progress + count_of_trailer + count_of_module_retriever + count_of_Exclude, "outcomes in total.")
print("-----------------------------------------------------------------------")

#Printing the list(Part 2-List)
print("Part 2:")
for unit in Progress_of_list_1:
    print(f"Progress - {unit[0]}, {unit[1]}, {unit[2]}")

for unit in Trailer_of_list_2:
    print(f"Progress (module trailer) - {unit[0]}, {unit[1]}, {unit[2]}")
    
for unit in Module_retriever_of_list_3:
    print(f"Module retriever - {unit[0]}, {unit[1]}, {unit[2]}")

for unit in Exclude_of_list_4:
    print(f"Exclude - {unit[0]}, {unit[1]}, {unit[2]}")
print("-----------------------------------------------------------------------")

#Creating the text file(Part 3-Text File)
with open("Outcome of Progression.txt", "w") as file:
    file.write("Part 3: \n")
    for unit in Progress_of_list_1:
        file.write(f"Progress - {unit[0]}, {unit[1]}, {unit[2]}\n")

    for unit in Trailer_of_list_2:
        file.write(f"Progress (module trailer) - {unit[0]}, {unit[1]}, {unit[2]}\n")
        
    for unit in Module_retriever_of_list_3:
        file.write(f"Module retriever - {unit[0]}, {unit[1]}, {unit[2]}\n")

    for unit in Exclude_of_list_4:
        file.write(f"Exclude - {unit[0]}, {unit[1]}, {unit[2]}\n")
f = open("Outcome of Progression.txt", "r")
print(f.read())
print("-----------------------------------------------------------------------")

#Printing the Dictionary(Part 4-Dictionary)
print("Part 4:")
for UoWnumber,Outputs in Progression_outcome_Dictionary.items():
    print(f"{UoWnumber} : {Outputs}", end=" ")






