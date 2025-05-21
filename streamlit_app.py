import streamlit as st
import time

def happy_birthday(name):
    cake_art = [
        "       ,,,,,       ",
        "      |||||      ",
        "    @@@@@@@@@    ",
        "  @@@@@@@@@@@@@  ",
        " @@@@@@@@@@@@@@@ ",
        f"||| H A P P Y  |||",
        f"||| B I R T H D A Y |||",
        f"|||   {name.upper()}   |||",
        "^^^^^^^^^^^^^^^ "
    ]
    st.text("\nHere's a birthday cake for you:\n")
    for line in cake_art:
        st.text(line)
    st.markdown(f"### Happy Birthday, {name}! 🎉🎂🎈")

def countdown(seconds):
    countdown_placeholder = st.empty()
    for i in range(seconds, 0, -1):
        countdown_placeholder.markdown(f"## Get ready to celebrate in {i}...")
        time.sleep(1)
    countdown_placeholder.markdown("### 🎉🎉🎉")

def main():
    st.title("🎉 Happy Birthday Streamlit App 🎉")
    name = st.text_input("Enter the birthday person's name:", "")
    
    if st.button("Celebrate!"):
        if not name.strip():
            st.warning("Please enter a name.")
        else:
            countdown(5)
            happy_birthday(name)

if __name__ == "__main__":
    main()



