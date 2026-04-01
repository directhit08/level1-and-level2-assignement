def rainfall_advisory():
    rainfall = float(input("Enter rainfall amount (mm): "))
    temperature = float(input("Enter temperature (°C): "))

    if rainfall < 200:
        print("Advisory: Irrigation Required")
    elif rainfall >= 200 and temperature > 30:
        print("Advisory: Monitor Soil")
    else:
        print("Advisory: Normal Conditions")

rainfall_advisory()