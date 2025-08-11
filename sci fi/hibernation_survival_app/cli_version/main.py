from hibernation_subject import HibernationSubject

def print_menu():
    print("\n=== HIBERNATION SURVIVAL ===")
    print("1. Check Vitals")
    print("2. Cut Hand")
    print("3. Administer Meds")
    print("4. Wake Subject")
    print("5. Quit")

def run_game():
    subject = HibernationSubject()
    
    while subject.is_hibernating:
        print_menu()
        choice = input("Choose action (1-5): ").strip()
        
        if choice == "1":
            print(subject.check_vitals())
        elif choice == "2":
            print(subject.cut_hand())
        elif choice == "3":
            print(subject.give_meds())
        elif choice == "4":
            print(subject.wake_up())
        elif choice == "5":
            print("🔌 Simulation terminated.")
            break
        else:
            print("❌ Invalid choice!")
        
        if subject.health <= 0:
            print("💀 Subject died in hibernation!")
            break

if __name__ == "__main__":
    run_game()