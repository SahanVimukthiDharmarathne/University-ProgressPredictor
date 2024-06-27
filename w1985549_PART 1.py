# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Westminster ID: w1985549   # Name : Thantrige Sahan Vimukthi Dharmarathne   # IIT Number :20222165
# Date: 04.21.2023
count_of_Progress = 0
count_of_trailer = 0
count_of_module_retriever = 0
count_of_Exclude = 0

while True:
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
            print("Progress")
        elif Pass_credits == 100:
            count_of_trailer += 1
            print("Progress(module trailer)")
        elif Fail_credits >= 80:
            count_of_Exclude += 1
            print("Exclude")
        elif Fail_credits < 80:
            count_of_module_retriever += 1
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

    







