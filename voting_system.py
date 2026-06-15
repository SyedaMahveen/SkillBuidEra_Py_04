voters = {}
votes = {
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0
}

def register_voter():
    voter_id = input("Enter Voter ID: ")

    if voter_id in voters:
        print("Voter already registered.")
    else:
        voters[voter_id] = False
        print("Registration successful!")

def cast_vote():
    voter_id = input("Enter Voter ID: ")

    if voter_id not in voters:
        print("Voter not registered.")
        return

    if voters[voter_id]:
        print("You have already voted.")
        return

    print("\nCandidates:")
    print("1. Candidate A")
    print("2. Candidate B")
    print("3. Candidate C")

    choice = input("Choose candidate (1-3): ")

    if choice == "1":
        votes["Candidate A"] += 1

    elif choice == "2":
        votes["Candidate B"] += 1

    elif choice == "3":
        votes["Candidate C"] += 1

    else:
        print("Invalid choice.")
        return

    voters[voter_id] = True
    print("Vote cast successfully!")

def show_results():
    print("\n===== ELECTION RESULTS =====")

    for candidate, count in votes.items():
        print(f"{candidate}: {count} vote(s)")

while True:
    print("\n===== VOTING SYSTEM =====")
    print("1. Register Voter")
    print("2. Cast Vote")
    print("3. Show Results")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_voter()

    elif choice == "2":
        cast_vote()

    elif choice == "3":
        show_results()

    elif choice == "4":
        print("Thank you for using Voting System!")
        break

    else:
        print("Invalid choice.")
