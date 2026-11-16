# Anaé CREPELLE CL10

# 1. What goes in? 
#    The scenarios_C.csv file uses commas as separators. The columns are Event, Day, Decision 1-3, Reputation 1-3, Budget 1-3, and Outcome 1-3. The numerical impacts are formatted as text strings with symbols (e.g., "-800 EUR", "+15 pts"), so they must be stripped of text and converted to integers before computation.
# 2. What happens?
#    - The program loads the CSV into a list of dictionaries and randomizes the order.
#    - For up to 10 days, it displays the current gauges, the situation, and the 3 options.
#    - It uses a while loop to force a valid 'A', 'B', or 'C' input.
#    - It unpacks the choice's tuple to update the budget and reputation, capping reputation at 100.
#    - It breaks early if either gauge drops to 0 or below.
# 3. What comes out?
#    The player sees a final summary screen with their game status (survived or fired), their final score/title, and their best and worst moves. Finally, a single comma-separated line is appended to 'results.csv' containing their name, final budget, final reputation, title, and the date.
# 4. What could go wrong?
#    - The player types 'Z' or '1': The input loop rejects it and asks again until valid.
#    - A gauge drops below 0: The game checks conditions after every choice and immediately stops the loop, triggering the "Fired" screen.
#    - The CSV file is missing or renamed: A try/except block catches the FileNotFoundError and safely alerts the player instead of fatally crashing.


import random
import csv
import datetime


#your code below

def parse_impact(value_str):
    """Converts a string like '-800 EUR' or '+15 pts' to an integer[cite: 3, 9]."""
    cleaned = value_str.replace(" EUR", "").replace(" pts", "").replace("+", "").strip()
    return int(cleaned)

def load_scenarios(filename):
    """Reads the CSV and returns a list of scenario dictionaries with tuple options[cite: 3, 8]."""
    scenarios = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                event = row['Event']
                # Each option is stored as a tuple: (text, budget_change, reputation_change, feedback)[cite: 8]
                opt_a = (row['Decision 1'], parse_impact(row['Budget 1']), parse_impact(row['Reputation 1']), row['Outcome 1'])
                opt_b = (row['Decision 2'], parse_impact(row['Budget 2']), parse_impact(row['Reputation 2']), row['Outcome 2'])
                opt_c = (row['Decision 3'], parse_impact(row['Budget 3']), parse_impact(row['Reputation 3']), row['Outcome 3'])
                
                scenarios.append({'event': event, 'A': opt_a, 'B': opt_b, 'C': opt_c})
    except FileNotFoundError:
        print(f"Error: Could not find {filename}. Please check your file directory.")
    return scenarios

def get_valid_choice():
    """Asks the player for A, B, or C until a valid answer is provided[cite: 5]."""
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ['A', 'B', 'C']:
            return choice
        print("Invalid input. Please type A, B or C.")

def apply_choice(choice_tuple, current_budget, current_rep):
    """Calculates and returns the new budget and reputation as a tuple[cite: 8]."""
    budget_change = choice_tuple[1]
    rep_change = choice_tuple[2]
    
    new_budget = current_budget + budget_change
    new_rep = min(current_rep + rep_change, 100) # Reputation can never go above 100[cite: 5]
    
    return new_budget, new_rep

def calculate_title(budget, reputation):
    """Returns the player's title based on their final score[cite: 6]."""
    score = reputation + (budget // 200)
    if score < 95:
        return "Eternal Intern", score
    elif 95 <= score <= 119:
        return "Growth Hacker", score
    elif 120 <= score <= 139:
        return "CMO Material", score
    else:
        return "Viral Legend", score

def save_result(name, budget, reputation, title):
    """Appends the final game result to results.csv[cite: 5]."""
    today = datetime.date.today().isoformat()
    with open('results.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, budget, reputation, title, today])

# --- MAIN GAME LOOP ---

def main():
    print("=== SURVIVE THE QUARTER ===")
    name = input("Enter your name: ") # Ask the player's name[cite: 5]
    
    # Feature 2d: Difficulty setup
    difficulty = input("Choose difficulty - Easy (15,000 EUR) or Hard (6,000 EUR)? Type E or H: ").strip().upper()
    budget = 15000 if difficulty == 'E' else 6000
    reputation = 50
    
    scenarios = load_scenarios('scenarios_C.csv')
    if not scenarios:
        return 
    
    random.shuffle(scenarios) # Shuffle them and play 10 days[cite: 5]
    game_days = min(10, len(scenarios))
    history = []
    survived = True
    
    for day in range(1, game_days + 1):
        scenario = scenarios[day - 1]
        
        # Display the UI[cite: 5]
        print(f"\n--- Day {day} ---")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(scenario['event'])
        print(f"A: {scenario['A'][0]}")
        print(f"B: {scenario['B'][0]}")
        print(f"C: {scenario['C'][0]}")
        
        choice_letter = get_valid_choice()
        
        # Unpack the chosen option tuple[cite: 8]
        choice_tuple = scenario[choice_letter]
        choice_text, budget_change, rep_change, feedback = choice_tuple
        
        # Apply impacts via a function returning a tuple[cite: 8]
        budget, reputation = apply_choice(choice_tuple, budget, reputation)
            
        print(f"\n> {feedback}")
        print(f"Budget {budget_change:+d} EUR, Reputation {rep_change:+d}")
        
        # Keep history to find the best and worst moves[cite: 6, 8]
        # Tuples are sorted element by element, so reputation change goes first
        history.append((rep_change, day, choice_text))
        
        # Check game over conditions[cite: 5, 6]
        if budget <= 0 or reputation <= 0:
            print("\n" + "="*30)
            print("GAME OVER. You are fired.")
            reason = "You ran out of money!" if budget <= 0 else "Your reputation hit zero!"
            print(reason)
            survived = False
            break
            
    # --- END GAME ---
    print("\n" + "="*30)
    if survived:
        print("Quarter survived, Lil Jedi!")
        print(f"Budget left: {budget} EUR, Reputation: {reputation}/100")
        
        title, score = calculate_title(budget, reputation)
        print(f"Final score: {score}")
        print(f"{name}, your title: {title}")
        
        best_move = max(history)
        worst_move = min(history)
        
        print(f"Best move: day {best_move[1]}, '{best_move[2]}' ({best_move[0]:+d})")
        print(f"Worst move: day {worst_move[1]}, '{worst_move[2]}' ({worst_move[0]:+d})")
        
        save_result(name, budget, reputation, title)
        print("Saved in results.csv")

if __name__ == "__main__":
    main()