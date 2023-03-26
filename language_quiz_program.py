def main():
    correct = 0
    print("Enter the number in English which corresponds to the number in french")
    numbers = {"un": "one", "deux": "two", "trois": "three", "quatre": "four", "cinq": "five",
               "six": "six", "sept": "seven", "huit": "eight", "neuf": "nine", "dix": "ten"}

    for num in numbers:
        answer = input("What is the equivalent of " + num + ":  ")
        answer = answer.lower()
        if numbers[num] == answer:
            print("Correct\n")
            correct += 1
        else:
            print("Incorrect. The answer was " + numbers[num] + "\n")
    print("You got " + str(correct))
    if correct == 10 or correct == 9:
        print("A")
    elif correct == 8:
        print("B")
    elif correct == 7:
        print("C")
    elif correct == 6:
        print("D")
    else:
        print("F")


main()
