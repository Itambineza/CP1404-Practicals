from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    # Create a list to store taxi objects
    taxis = []

    # Add some taxi instances to the list
    taxis.append(Taxi("Prius", 100, 1.23))  # Assuming a price_per_km value of 1.23
    taxis.append(SilverServiceTaxi("Hummer", 200, 4))
    taxis.append(Taxi("Corolla", 150, 1.35))  # Assuming a price_per_km value of 1.35

    print("Let's drive!")
    current_taxi = None
    bill = 0

    # Menu loop
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i}: {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print(f"You chose {current_taxi}")
        elif choice == 'd':
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                bill += fare
            else:
                print("Please choose a taxi first!")

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    for taxi in taxis:
        print(f"{taxi.name}: {taxi}")


if __name__ == "__main__":
    main()
