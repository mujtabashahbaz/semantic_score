import streamlit as st
import requests

# Function to call OpenAI API (using GPT-3.5 Turbo)
def get_semantic_score(blog_content, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    
    # Prepare the prompt for GPT-3.5 Turbo (Chat API)
    messages = [
        {"role": "system", "content": "You are an assistant that evaluates the semantic quality of blog content."},
        {"role": "user", "content": f"Please evaluate the semantic quality and relevance of this blog content:\n\n{blog_content}\n\nProvide a semantic score on a scale of 1 to 10, and highlight any key areas that could be improved."}
    ]
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": 500,
        "temperature": 0.5,
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI
def main():
    st.title("Blog Semantic Score Analyzer")
    
    # Ask user to input their OpenAI API key
    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    
    if api_key:
        # Get blog content input from user
        blog_content = st.text_area("Paste your blog content here:", height=300)
        
        if st.button("Evaluate Semantic Score"):
            if blog_content:
                st.info("Analyzing the semantic score... please wait.")
                
                # Get semantic score from OpenAI API
                semantic_feedback = get_semantic_score(blog_content, api_key)
                
                # Display the result
                st.subheader("Semantic Analysis Result:")
                st.write(semantic_feedback)
            else:
                st.warning("Please paste your blog content to analyze.")

if __name__ == "__main__":
    main()
