import streamlit as st

st.markdown("<h1 style='text-align: center;'>BMI Calculator App</h1>", unsafe_allow_html=True)

st.image("bmi.png", caption="Calculate your BMI")
weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (cm):")

if st.button("Calculate BMI"):
    if height <= 0:
        st.error("Height must be greater than zero.")
    else:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")

