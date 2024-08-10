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
        routine = {
            "Morning Routine": [
                "Cleanse with a gentle foaming cleanser.",
                "Apply a lightweight, oil-free moisturizer.",
                "Use a broad-spectrum sunscreen (SPF 30+)."
            ],
            "Evening Routine": [
                "Cleanse with a salicylic acid cleanser.",
                "Apply a lightweight, oil-free moisturizer.",
                "Use a clay mask once a week to control excess oil."
            ]
        }
    elif skin_type == "Dry":
        problems = ["Flaky Skin", "Redness", "Tightness"]
        advice = (
            "Use gentle, hydrating cleansers, "
            "apply moisturizer regularly, "
            "and avoid hot showers."
        )
        routine = {
            "Morning Routine": [
                "Cleanse with a hydrating cleanser.",
                "Apply a rich moisturizer.",
                "Use a broad-spectrum sunscreen (SPF 30+)."
            ],
            "Evening Routine": [
                "Cleanse with a creamy cleanser.",
                "Apply a hydrating serum.",
                "Use a rich night cream."
            ]
        }
    elif skin_type == "Combination":
        problems = ["Shiny T-zone", "Dry Cheeks", "Occasional Breakouts"]
        advice = (
            "Use a mild cleanser, "
            "balance moisturizing for oily and dry areas, "
            "and exfoliate gently."
        )
        routine = {
            "Morning Routine": [
                "Cleanse with a balanced cleanser.",
                "Apply a lightweight moisturizer to dry areas.",
                "Use a broad-spectrum sunscreen (SPF 30+)."
            ],
            "Evening Routine": [
                "Cleanse with a gentle cleanser.",
                "Apply a light moisturizer to dry areas.",
                "Use a clay mask on the T-zone once a week."
            ]
        }
    elif skin_type == "Sensitive":
        problems = ["Redness", "Irritation", "Allergic Reactions"]
        advice = (
            "Use fragrance-free and hypoallergenic products, "
            "avoid harsh exfoliants, "
            "and test new products on a small area first."
        )
        routine = {
            "Morning Routine": [
                "Cleanse with a gentle, fragrance-free cleanser.",
                "Apply a soothing serum.",
                "Use a broad-spectrum sunscreen (SPF 30+) for sensitive skin."
            ],
            "Evening Routine": [
                "Cleanse with a gentle, hydrating cleanser.",
                "Apply a calming moisturizer.",
                "Use a soothing mask once a week."
            ]
        }
    else:  # Normal skin
        problems = ["Occasional Dryness", "Occasional Oiliness"]
        advice = (
            "Maintain a balanced skincare routine, "
            "stay hydrated, "
            "and protect your skin with sunscreen."
        )
        routine = {
            "Morning Routine": [
                "Cleanse with a mild cleanser.",
                "Apply a lightweight moisturizer.",
                "Use a broad-spectrum sunscreen (SPF 30+)."
            ],
            "Evening Routine": [
                "Cleanse with a gentle cleanser.",
                "Apply a nourishing night cream.",
                "Use an exfoliating mask once a week."
            ]
        }

    return problems, advice, routine

# Streamlit app
st.title("Skin Care Advisor")
st.write("Identify potential skin-related problems, get skincare advice, and discover a personalized skincare routine based on your skin type.")

# User input
skin_type = st.selectbox("Select your skin type:", ["Normal", "Oily", "Dry", "Combination", "Sensitive"])
known_allergies = st.text_input("Do you have any known allergies? (e.g., nuts, fragrances)")

# Get skincare advice
problems, advice, routine = get_skincare_advice(skin_type)

# Display results
st.subheader("Potential Skin Problems")
st.write(", ".join(problems))

st.subheader("Skincare Advice")
st.write(advice)

if known_allergies:
    st.warning(f"Warning: Be cautious of products containing ingredients you may be allergic to, such as {known_allergies}. Always patch test new products before full use.")

st.subheader("Suggested Skincare Routine")

# Display morning routine
st.write("**Morning Routine:**")
for step in routine["Morning Routine"]:
    st.write(f"- {step}")

# Display evening routine
st.write("**Evening Routine:**")
for step in routine["Evening Routine"]:
    st.write(f"- {step}")

st.write("Remember, this is a general guide. For personalized advice, consult a dermatologist.")
