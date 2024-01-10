"""
Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.
Range - Number of notes(n) : n(1 = n = 1000000)
"""
def count_notes(amount):
    notes = [500, 200, 100, 50, 20, 10]
    note_count = []

    for note in notes:
        count, amount = divmod(amount, note)
        note_count.append((note, count))

    return note_count

def main():
    try:
        amount = int(input("Enter the amount: "))
        if not (1 <= amount <= 1000000):
            raise ValueError("Amount should be between 1 and 1000000")

        result = count_notes(amount)
        print("Number of notes:")
        for note, count in result:
            print(f"{note} - {count} notes")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


