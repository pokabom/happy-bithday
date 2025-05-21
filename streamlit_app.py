import streamlit as st

st.title("HAPPIEST BIRTHDAYY")
import time
import sys

def happy_birthday(name):
    cake_art = [
        "       ,,,,,       ",
        "      |||||      ",
        "    @@@@@@@@@    ",
        "  @@@@@@@@@@@@@  ",
        " @@@@@@@@@@@@@@@ ",
        "|||||HAPPY|||||",
        "||||BIRTHDAY|||",
        "|||||" + name.upper() + "|||",
        "^^^^^^^^^^^^^^^ "
    ]
    print("\nHere's a birthday cake for you:\n")
    for line in cake_art:
        print(line)
    print("\nHappy Birthday, {}! 🎉🎂🎈\n".format(name))

def countdown(seconds):
    print("Get ready to celebrate! Countdown:")
    for i in range(seconds, 0, -1):
        print(f"{i}...", end='', flush=True)
        time.sleep(1)
    print("🎉🎉🎉")

if __name__ == "__main__":
    name = input("Enter the birthday person's name: ").strip()
    if not name:
        name = "Friend"
    countdown(5)
    happy_birthday(name)

