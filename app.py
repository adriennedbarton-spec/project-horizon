import streamlit as st

from knowledge_base import get_article_content, identify_topic

from pathlib import Path

#Page configuration
st.set_page_config(page_title="Nova | Horizon", page_icon="✨", layout="wide")

#Custom styling
st.markdown(
    """
<style>
.st-key-nova_answer {
    background-color: #EAF3FF;
    border: 1px solid #C2DCFF;
    border-radius: 12px;
    padding: 20px;
}
</style>
""",
    unsafe_allow_html=True,
)


#Header
st.caption("HORIZON | TRAINING & CERTIFICATION")

left_col, right_col = st.columns([0.1, 1.5], gap="medium")

with left_col:
    st.image(Path(__file__).parent / "nova_logo.png", width=100)

with right_col:
    st.title("Meet Nova")
    st.write(
        "Your customer education assistant. Find the guidance you need to keep learning."
    )
st.divider()


#Question input
left_col, right_col = st.columns([1, 1.4], gap="large")

with left_col:
    st.subheader("How can I help?")
    st.write("Ask Nova a question about Horizon.")

    customer_role = st.selectbox(
        "Your role",
        ["learner", "instructor", "admin"],
        format_func=lambda role: role.title(),
    )

    question = st.text_input(
        "Ask Nova", placeholder="e.g., How do I earn a certification?"
    )


#Answer display
if question:
    topic = identify_topic(question)

    if topic:
        response = get_article_content(topic, customer_role)
    else:
        response = "I couldn't find an article about that topic yet."

    if isinstance(response, dict):
        article_title = response["title"]
        article_content = response["content"]
    else:
        article_title = "📖 Nova's Answer"
        article_content = response

    with right_col:
        st.subheader(article_title)

        with st.container(border=True, key="nova_answer"):
            st.write(article_content)

else:
    with right_col:
        with st.container(border=True, key="nova_answer"):
            st.subheader("Hi! I'm Nova.")
            st.write(
                "I'm here to help you navigate Horizon. Ask me about certifications, courses, learning paths, or managing your account."
            )
            st.divider()
            st.caption("Your answer will appear here once you ask a question.")


#Footer
st.divider()
st.caption("Powered by Horizon Knowledge Base | Nova v0.5")
