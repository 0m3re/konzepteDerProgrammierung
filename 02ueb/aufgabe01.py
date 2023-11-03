print("\nThe choices: \n"
                            "1: Division with 0\n"
                            "2: Overflow\n"
                            "3: Rounding Error\n"
                            "4; Underflow\n"
                            "5: Exit")
                    userChoice = input("Your choice: ")
                    if userChoice == "1":
                        while True:
                            print("\nThe choices:\n"
                                    "1: int\n"
                                    "2: float\n"
                                    "3: complex\n"
                                    "4: Exit")
                            userChoice = input("What do you chose? ")
                            if userChoice == "1":
                                try:
                                    print(1/0)
                                except Exception as e:
                                    print(f"\033[91m[int error] {e}\033[0m")
                            elif userChoice == "2":
                                try:
                                    print(1.0/0.0)
                                except Exception as e:
                                    print(f"\033[91m[float error] {e}\033[0m")
                            elif userChoice == "3":
                                try:
                                    print(1j/0j)
                                except Exception as e:
                                    print(f"\033[91m[complex error] {e}\033[0m")
                            elif userChoice == "4":
                                break
                    elif userChoice == "2":
                        x = 1.79e308
                        y = x * 2
                        print("We multiplied", x, "by 2. Result:", y)
                        print(f"\033[91mOverflow occurred.\033[0m")
                    elif userChoice == "3":
                        x = 0.1
                        y = 0.2
                        z = 0.3
                        verifyAddition = x + y == z
                        print("We added", x, "and", y, "and compared it to", z, " Result:", verifyAddition)
                        print(f"\033[91mA rounding error occurred.\033[0m")
                    elif userChoice == "4":
                        x = 1.0
                        bufferValue = x
                        while x > 0:
                            x = x / 2.0
                            print("x/2 =", x)
                        print("We continuously divided", bufferValue, "by 2 until the result was too close to zero to be represented accurately.")
                        print(f"\033[91mUnderflow occurred.\033[0m")
                    elif userChoice == "5":
                        break
                    else:
                        print("Your choice does not exist. Enter a number between 1 and 5.")
