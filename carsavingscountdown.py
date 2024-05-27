import os
import json


#define a motivational string for later on
motivation = """
You can save money and you have the strength to do so.
You just need to look within and work through this turmoil and save more.
you only need to grind and put a little more away before you reach your goal.
Just imagine you at the wheel of a motor you will truly enjoy.
If not that, just imagine the smile on your face when you floor it...
"""

#define a path for the savings information to be saved to (json)
savings_figures = "savings.json"

#function to load savings from file
def load_savings():
    if os.path.exists(savings_figures):
        with open(savings_figures, 'r') as file:
            return json.load(file)
    else:
        return {"goal": 0, "saved": 0}

#function to save savings to file
def save_savings(savings):
    with open(savings_figures, 'w') as file:
        json.dump(savings, file)

#function to display savings progress
def display_progress(savings):
    goal = savings["goal"]
    saved = savings["saved"]
    if goal == 0:
        print("\nYou haven't set a savings goal yet.\n")
    else:
        progress = (saved / goal) * 100
        print(f"\nGoal: £{goal}")
        print(f"Saved: £{saved}")
        print(f"Progress: {progress:.2f}%")

#function to update savings figure, within savings.json
def update_savings(savings):
    new_saved = float(input("\nEnter the new savings amount: "))
    savings["saved"] = new_saved
    save_savings(savings)
    print("\nsavings.json updated successfully.")

#function to update the goal figure, within savings.json
def update_goal(savings):
    new_goal = float(input("\nEnter the new goal amount: "))
    savings["goal"] = new_goal
    save_savings(savings)
    print("\nsavings.json updated successfully.")

#main menu code which calls other functions and also prints current status
def main():
    savings = load_savings()
    display_progress(savings) #print savings progress when main menu is called
    
    while True:
        print("")
        
        print("\n0. Print the all of the metrics and exit")
        print("1. Update your savings amount?")
        print("2. Update your goal amount?")
        print("3. Motivate me, I am sad :(")
        print("4. Exit only")

        
        choice = input("\nEnter your choice (0-4): ").strip()
        if choice == "0":
            display_progress(savings)
            break
        elif choice == "1":
            update_savings(savings)
        elif choice == "2":
            update_goal(savings)
        elif choice == "3":
            print(motivation.upper())
        elif choice == "4":
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
