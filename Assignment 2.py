while True:
    inches = float(input("Enter a value in inches (negative to exit): "))
    if inches < 0:
        print("Exiting the program.")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters} centimeters.")
