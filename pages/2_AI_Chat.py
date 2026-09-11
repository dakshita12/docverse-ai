import streamlit as st

st.title("AI Chat")

st.write("Chat with your study documents")

# Chat input
user_input = st.chat_input("Ask something about your documents...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Temporary AI response
    with st.chat_message("assistant"):
        st.write("AI response will appear here.")