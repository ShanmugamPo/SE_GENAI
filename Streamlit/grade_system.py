import streamlit as st

st.title(":orange[Welcome to the Grade Calculator]")
mark_input = st.text_input("Enter your mark (0 - 100):")
if st.button("Calculate Grade"):
    try:
        mark = float(mark_input)

        if mark < 0 or mark > 100:
            st.error("Invalid mark. Please enter a value between 0 and 100.")
        elif mark >= 90:
            st.success(f"Mark: {mark} → Grade: A")
            st.image("CM_Vijay.png", width=100)  # Display image for grade C
            st.markdown("<p style='color: black; padding: 5px; display: inline-block;'>Taramana Sambhavam!</p>", unsafe_allow_html=True)

        elif mark >= 80:
            st.success(f"Mark: {mark} → Grade: B")
            st.balloons()  # Display balloons animation for grade A
            st.markdown("<p style='color: black; padding: 5px; display: inline-block;'>Congratulations!</p>", unsafe_allow_html=True)

        elif mark >= 70:
            st.warning(f"Mark: {mark} → Grade: C")
            st.markdown("<p style='color: black; padding: 5px; display: inline-block;'>You can do better!</p>", unsafe_allow_html=True)
        elif mark >= 60:
            st.warning(f"Mark: {mark} → Grade: D")
            st.markdown("<p style='color: black; padding: 5px; display: inline-block;'>Innum padikanum!</p>", unsafe_allow_html=True)
        else:
            st.error(f"Mark: {mark} → Grade: E")
            st.markdown("<p style='color: black; padding: 5px; display: inline-block;'>Sorry to say, You have failed. Better luck next time!</p>", unsafe_allow_html=True)
    except ValueError:
        st.error("Please enter a valid numeric input.")