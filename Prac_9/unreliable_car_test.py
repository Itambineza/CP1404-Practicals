from unreliable_car import UnreliableCar

def main():
    # Create an UnreliableCar object
    my_car = UnreliableCar("Unreliable Car", 100, 70)  # 70% reliability

    # Drive the car 50 km
    distance_driven = my_car.drive(50)
    if distance_driven > 0:
        print(f"Successfully drove {distance_driven} km.")
    else:
        print("Car failed to drive due to reliability.")

    # Attempt to drive the car 50 km again
    distance_driven = my_car.drive(50)
    if distance_driven > 0:
        print(f"Successfully drove {distance_driven} km.")
    else:
        print("Car failed to drive due to reliability.")

    # Attempt to drive the car 50 km once more
    distance_driven = my_car.drive(50)
    if distance_driven > 0:
        print(f"Successfully drove {distance_driven} km.")
    else:
        print("Car failed to drive due to reliability.")

if __name__ == "__main__":
    main()