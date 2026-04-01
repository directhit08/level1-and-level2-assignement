def rainfall_advisory():
    rainfall = float(input("Enter rainfall amount (mm): "))
    temperature = float(input("Enter temperature (°C): "))

    if rainfall < 200:
        print("Advisory: Irrigation Required")
    else:
        if temperature > 30:
            print("Advisory: Monitor Soil")
        else:
            print("Advisory: Normal Conditions")

if __name__ == "__main__":
    rainfall_advisory()