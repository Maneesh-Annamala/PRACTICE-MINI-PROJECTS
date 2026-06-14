# Store candidates and votes
candidates = {
    "trump": 0,
    "modi": 0,
    "putin": 0,
}

# Get total voters
try:
    number_of_voters = int(input("Enter how many voters are there to vote: "))

except ValueError:
    print("You need to enter numbers only")
    exit()

# Show voting instructions
print("There are 3 candidates in the selection choose wisely and elect your leader")

print(
    "1.To vote Donald Trump enter 'trump'"
    "\n2.To vote Narendra Modi enter 'modi'"
    "\n3.To vote Putin enter 'putin'"
    )

# Start voting
for i in range(number_of_voters):

    while True:

        vote = input("1.Donald Trump\n2.Narendra Modi\n3.Putin\nPlease choose one option: ").lower()

        # Count vote
        if vote in candidates:
            candidates[vote] += 1
            break

        else:
            print("Please choose between them")

highest_votes = float("-inf")
winner = ""
tie_checking = []

# Find highest vote count
for name, votes in candidates.items():
    if votes > highest_votes:
        highest_votes = votes
        winner = name

# Check for tie
for names, votes in candidates.items():
    if votes == highest_votes:
        tie_checking.append(names)

# Show result
if len(tie_checking) == 1:
    print(f"The election winner is {winner} with {highest_votes} votes")

else:
    print(f"There is a tie between {tie_checking}")