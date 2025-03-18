import streamlit as st
import google.generativeai as genai

# Set your Gemini API key directly (Not secure; better to use st.secrets)
genai.configure(api_key="AIzaSyCU_9Gi-5MXNb2C46Dre998MoiMjg3g-W8")  # Replace with a valid API key

def retriever_info(query):
    return f"Relevant information about '{query}'"

def rag_query(query):
    retrieved_info = retriever_info(query)
    augmented_prompt = f"User query: {query}. Retrieved information: {retrieved_info}"

    model = genai.GenerativeModel("gemini-1.5-pro")  # Use the correct model

    response = model.generate_content(
        augmented_prompt,  # Gemini API accepts the query directly as a string
        generation_config={
            "temperature": 0.2,  # Controls randomness (0.0 = deterministic, 1.0 = most random)
            "top_p": 0.9,  # Controls diversity of output
            "top_k": 40  # Another way to limit randomness
        }
    )

    return response.text.strip() if hasattr(response, "text") else "No response generated."

# Streamlit UI
st.title("RAG Prompt Query Interface ")
user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    if user_input:
        response = rag_query(user_input)
        st.write("Response:", response)
    else:
        st.warning("Please enter a query.")
