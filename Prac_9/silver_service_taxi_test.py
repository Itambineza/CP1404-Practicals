from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi_fare():
    # Create a SilverServiceTaxi object with fanciness of 4
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)

    # Drive the taxi for 18 km
    my_silver_taxi.drive(18)

    # Calculate the fare
    fare = my_silver_taxi.get_fare()

    # Print the actual fare for debugging
    print(f"Actual fare: {fare}")

    # Assert the fare calculation is correct
    assert fare == 148.50, "Fare calculation is incorrect"

# Run the test
test_silver_service_taxi_fare()


