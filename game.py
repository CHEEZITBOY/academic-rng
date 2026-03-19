import streamlit as st
import random

# --- 🧠 PERSISTENCE LAYER ---
if 'points' not in st.session_state:
    st.session_state.points = 10
if 'streak' not in st.session_state:
    st.session_state.streak = 0

# --- 🎭 EXCUSE GENERATOR ---
def generate_excuse(teacher, risk):
    openings = [
        "I regret to inform you",
        "With deepest apologies",
        "Please understand",
        "I must explain that"
    ]

    if risk == 1:
        events = [
            "a minor issue with my laptop",
            "a brief internet outage",
            "a small but devastating scheduling error"
        ]
    elif risk == 2:
        events = [
            "an aggressive flock of geometry-hating pigeons",
            "a rogue AI in my calculator",
            "a highly suspicious power fluctuation"
        ]
    else:
        events = [
            "a rift in the space-time continuum",
            "a sentient toaster uprising",
            "an interdimensional goose invasion"
        ]

    details = [
        "that specifically targeted my homework",
        "at the exact moment I tried to submit it",
        "in a way I cannot fully explain"
    ]

    return f"Dear {teacher}, {random.choice(openings)}, my homework was lost due to {random.choice(events)} {random.choice(details)}."

# --- 🎭 TEACHER REACTIONS ---
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

# --- 🖥️ UI SETUP ---
st.set_page_config(page_title="Academic RNG", page_icon="📝")

st.title("🛡️ Academic RNG: The Excuse Engine")
st.caption("A completely serious academic tool. Definitely. (v1.0)")

# --- SIDEBAR ---
st.sidebar.header("🕹️ Player Stats")
st.sidebar.metric("Current Streak", st.session_state.streak)
st.sidebar.metric("Bribe Points", st.session_state.points)

st.sidebar.divider()
st.sidebar.subheader("💰 The Black Market")

bribe_amount = st.sidebar.slider(
    "Spend points for +% Success?", 
    0, 
    st.session_state.points, 
    0
)

# --- MAIN INPUTS ---
teacher = st.text_input("Target Teacher Name", "Prof. Higgins")

risk = st.select_slider(
    "Select Risk Level",
    options=[1, 2, 3],
    value=1,
    format_func=lambda x: ["Safe", "Risky", "Career-Ending"][x-1]
)

# --- 🚀 MAIN BUTTON ---
if st.button("🚀 DEPLOY STRATEGY"):

    # Generate excuse first
    excuse_text = generate_excuse(teacher, risk)

    st.write("📄 **Generated Excuse:**")
    st.code(excuse_text)

    # Probability logic
    base_chance = (70 / risk) + (bribe_amount * 3)
    st.session_state.points -= bribe_amount

    roll = random.random() * 100

    # Outcome logic
    if roll < 7:
        result = "CRITICAL"
        st.session_state.streak += 2
        st.session_state.points += (20 * risk)
        st.balloons()

    elif roll < base_chance:
        result = "SUCCESS"
        st.session_state.streak += 1
        st.session_state.points += (5 * risk)

    else:
        result = "FAIL"
        if st.session_state.streak > 0:
            st.warning(f"💔 STREAK BROKEN! You reached {st.session_state.streak}.")
        st.session_state.streak = 0

    # --- OUTPUT ---
    st.divider()
    st.info(get_reaction(result, teacher))

# --- OPTIONAL STYLING ---
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
