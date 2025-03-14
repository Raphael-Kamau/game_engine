prices = [100, 100, 100, 100, 100]

total = 0
for price in prices:
    total += price
    print(f"Total price: {total}")

numbers = [50, 20 ,30 ,30 ,20]

for item in numbers:
    print("x" * item)

columns = [20, 20 , 20, 25, 40, 50, 50]
for item in columns:
    print("x" * item)

secret_number = 10
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess:"))
    guess_count += 1
    if guess == secret_number:
        print("You won.")
        break
    else:
        print("You loose, please try again")

