import random

# secret is now between 0 and 20 (inclusive)
max_tries = 5

def play_game():
    secret = random.randint(0, 20)
    guess = None
    tries = 0

    print("\nGuess a number between 0 and 20.")

    while guess != secret and tries < max_tries:
        try:
            raw = input("Your guess (0-20): ").strip()
            guess = int(raw)
        except ValueError:
            # non-integer inputs do not count as tries
            print("Please enter a valid integer between 0 and 20.")
            continue

        # out-of-range guesses DO count as tries now
        if guess < 0 or guess > 20:
            tries += 1
            print(f"{guess} is out of range — it counts as a try. ({tries}/{max_tries})")
            continue

        # count only valid, in-range guesses
        tries += 1

        if guess < secret:
            print(f"Too low! ({tries}/{max_tries})")
        elif guess > secret:
            print(f"Too high! ({tries}/{max_tries})")
        else:
            print(f"Correct! 🎉 ({tries}/{max_tries})")

    if guess != secret:
        print("Sorry, you've reached the maximum number of tries. The number was", secret)
    else:
        print(f"You guessed it in {tries} tries!")


if __name__ == '__main__':
    # main replay loop
    while True:
        play_game()

        # ask to retry
        try:
            again = input("Play again? (y/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()  # for a clean newline
            break

        if not again or again[0] != 'y':
            print('Goodbye!')
            break