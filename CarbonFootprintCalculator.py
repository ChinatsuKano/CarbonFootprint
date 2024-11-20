def calculate_transport_emissions(miles, vehicle_type="car"):
    """
    Calculate CO2 emissions from transportation.
    """
    emission_factors = {
        "car": 0.404,  # kg CO2 per mile
        "bus": 0.089,  # kg CO2 per mile
        "train": 0.041, # kg CO2 per mile
        "bike": 0.0    # kg CO2 per mile (biking has no emissions)
    }
    return miles * emission_factors.get(vehicle_type, 0.404)


def calculate_electricity_emissions(kwh, country="US"):
    """
    Calculate CO2 emissions from electricity usage.
    """
    emission_factors = {
        "US": 0.92,   # kg CO2 per kWh
        "EU": 0.3,    # kg CO2 per kWh
        "China": 0.95 # kg CO2 per kWh
    }
    return kwh * emission_factors.get(country, 0.92)


def calculate_waste_emissions(kilograms, waste_type="general"):
    """
    Calculate CO2 emissions from waste management.
    """
    emission_factors = {
        "general": 2.5,     # kg CO2 per kg of waste
        "recycled": 0.5,    # kg CO2 per kg of waste
        "composted": 0.2    # kg CO2 per kg of waste
    }
    return kilograms * emission_factors.get(waste_type, 2.5)


def categorize_emissions(total_emissions):
    """
    Categorize the total emissions as minimal, moderate, or excess.
    """
    if total_emissions < 100:
        return "Minimal"
    elif 100 <= total_emissions < 500:
        return "Moderate"
    else:
        return "Excess"


def main():
    print("Welcome to the Carbon Footprint Calculator")

    # Transportation
    miles = float(input("Enter miles traveled by car: "))
    transport_emissions = calculate_transport_emissions(miles, "car")

    # Electricity
    kwh = float(input("Enter electricity usage in kWh: "))
    country = input("Enter your country (US, EU, or China): ")
    electricity_emissions = calculate_electricity_emissions(kwh, country)

    # Waste
    kilograms = float(input("Enter waste produced in kg: "))
    waste_type = input("Enter type of waste (general, recycled, composted): ")
    waste_emissions = calculate_waste_emissions(kilograms, waste_type)

    # Total emissions
    total_emissions = transport_emissions + electricity_emissions + waste_emissions

    # Categorize emissions
    category = categorize_emissions(total_emissions)

    print(f"\nYour estimated carbon footprint is: {total_emissions:.2f} kg CO2")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
