#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)

    if (temp_int < 0):
        raise Exception("Caught input_temperature error: "
                        f" {temp_int}°C is too cold for plants (min 0°C)\n")
    elif (temp_int > 40):
        raise Exception("Caught input_temperature error:"
                        f" {temp_int}°C is too hot for plants (max 40°C)\n")

    return (temp_int)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    print("Input data is '25'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}°C")

    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except Exception as error:
        print(f"Caught input temperature: {error}\n")

    try:
        print("Input data is '100'")
        temp = input_temperature("100")
    except Exception as error:
        print(f"{error}")

    try:
        print("Input data is '-50'")
        temp = input_temperature("-50")
    except Exception as error:
        print(f"{error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
