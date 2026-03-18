import streamlit as st
import random

# --- 🧠 PERSISTENCE LAYER ---
if 'points' not in st.session_state:
    st.session_state.points = 10  # Starting capital
if 'streak' not in st.session_state:
    st.session_state.streak = 0

# --- 🎭 TEACHER NARRATIVE ENGINE ---
def get_reaction(result, teacher):
    lines = {
        "CRITICAL": [
            f"🌟 {teacher}: 'This is... moving. I'm canceling the midterm.'", 
            f"🌟 {teacher}: 'I am forwarding this to the board as a work of genius.'"
        ],
        "SUCCESS": [
            f"✅ {teacher}: 'Fine. But I expect double effort next time.'", 
            f"✅ {teacher}: 'Your creativity is your only passing grade today.'"
        ],
        "FAIL": [
            f"❌ {teacher}: 'Nice try. See you in detention.'", 
            f"❌ {teacher}: 'I've heard this one three times this week. Zero.'"
        ]
    }
    return random.choice(lines[result])

# --- 🖥️ UI FRONTEND ---
st.set_page_config(page_title="Academic RNG", page_icon="📝")
st.title("🛡️ Academic RNG: The Excuse Engine")
st.caption("A completely serious academic tool. Definitely. (v1.0)")

# Sidebar Stats & Shop
st.sidebar.header("🕹️ Player Stats")
st.sidebar.metric("Current Streak", st.session_state.streak)
st.sidebar.metric("Bribe Points", st.session_state.points)

st.sidebar.divider()
st.sidebar.subheader("💰 The Black Market")
bribe_amount = st.sidebar.slider(
    "Spend points for +% Success?", 0, st.session_state.points, 0
)

# Main Inputs
teacher = st.text_input("Target Teacher Name", "Prof. Higgins")
risk = st.select_slider(
    "Select Risk Level", 
    options=[1, 2, 3], 
    value=1,
    help="1: Safe, 2: Risky, 3: Career-Ending"
)

# --- 🚀 DEPLOY EXCUSE LOGIC ---
if st.button("🚀 DEPLOY STRATEGY"):
    # Probability logic
    base_chance = (70 / risk) + (bribe_amount * 3)
    st.session_state.points -= bribe_amount
    
    roll = random.random() * 100
    
    # Outcome determination
    if roll < 7:  # Critical Success
        res = "CRITICAL"
        st.session_state.streak += 2
        st.session_state.points += (20 * risk)
        st.balloons()
    elif roll < base_chance:  # Normal Success
        res = "SUCCESS"
        st.session_state.streak += 1
        st.session_state.points += (5 * risk)
    else:  # Fail
        res = "FAIL"
        if st.session_state.streak > 0:
            st.warning(f"💔 STREAK BROKEN! You reached {st.session_state.streak}.")
        st.session_state.streak = 0
    
    # Teacher reaction
    st.divider()
    st.info(get_reaction(res, teacher))

# Optional: Theme / styling
st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: #00ffcc;
    }
    </style>
    """,
    unsafe_allow_html=True
)