#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
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

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
