import streamlit as st
# Page title
st.set_page_config(page_title="Skillspotter Chat", page_icon="💬")
st.title("Skillspotter 💬")
st.write("Your SME Marketplace Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_message = st.chat_input("Ask about SMEs, services, or service providers...")

# Simple chatbot logic
def skillspotter_bot(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello 👋 Welcome to Skillspotter! How can I help you?"
    elif "service" in message:
        return "Skillspotter helps you find SMEs offering services like Barbers, Electricians, Hairdressers, and Handyman."
    elif "service providers" in message:
        return "You can discover skilled professionals based on expertise, ratings, and pricing."
    elif "price" in message or "cost" in message:
        return "Service prices depend on the SME or skilled professionals. You can compare before choosing."
    elif "contact" in message:
        return "You can contact service providers directly through the Skillspotter platform."
    else:
        return "I'm here to help! Ask me about services, freelancers, or how Skillspotter works."

# When user sends a message
if user_message:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    # Bot response
    bot_reply = skillspotter_bot(user_message)

    # Save bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    # Display bot response
    with st.chat_message("assistant"):

        st.write(bot_reply)

