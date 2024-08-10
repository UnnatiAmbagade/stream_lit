import streamlit as st

# Function to give skincare advice based on skin type
def get_skincare_advice(skin_type):
    if skin_type == "Oily":
        problems = ["Acne", "Blackheads", "Large Pores"]
        advice = (
            "Use oil-free and non-comedogenic products, "
            "cleanse your face twice daily, "
            "and avoid heavy creams."
        )
    elif skin_type == "Dry":
        problems = ["Flaky Skin", "Redness", "Tightness"]
        advice = (
            "Use gentle, hydrating cleansers, "
            "apply moisturizer regularly, "
            "and avoid hot showers."
        )
    elif skin_type == "Combination":
        problems = ["Shiny T-zone", "Dry Cheeks", "Occasional Breakouts"]
        advice = (
            "Use a mild cleanser, "
            "balance moisturizing for oily and dry areas, "
            "and exfoliate gently."
        )
    elif skin_type == "Sensitive":
        problems = ["Redness", "Irritation", "Allergic Reactions"]
        advice = (
            "Use fragrance-free and hypoallergenic products, "
            "avoid harsh exfoliants, "
            "and test new products on a small area first."
        )
    else:  # Normal skin
        problems = ["Occasional Dryness", "Occasional Oiliness"]
        advice = (
            "Maintain a balanced skincare routine, "
            "stay hydrated, "
            "and protect your skin with sunscreen."
        )

    return problems, advice

# Streamlit app
st.title("Skin Care Advisor")
st.write("Identify potential skin-related problems and get proper skincare advice based on your skin type.")

# User input
skin_type = st.selectbox("Select your skin type:", ["Normal", "Oily", "Dry", "Combination", "Sensitive"])
known_allergies = st.text_input("Do you have any known allergies? (e.g., nuts, fragrances)")

# Get skincare advice
problems, advice = get_skincare_advice(skin_type)

# Display results
st.subheader("Potential Skin Problems")
st.write(", ".join(problems))

st.subheader("Skincare Advice")
st.write(advice)

if known_allergies:
    st.warning(f"Warning: Be cautious of products containing ingredients you may be allergic to, such as {known_allergies}. Always patch test new products before full use.")

st.write("Remember, this is a general guide. For personalized advice, consult a dermatologist.")
