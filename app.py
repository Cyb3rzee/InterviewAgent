import streamlit as st
from agent.orchestrator import InterviewAgent

st.set_page_config(page_title="InterviewOS - Local Agent", layout="wide")

st.title("InterviewOS v0.1 — Local Agent Workspace")
st.caption("Local-first, zero-budget AI interview practice & reasoning agent.")

@st.cache_resource
def load_agent():
    return InterviewAgent(model_name="llama3.2:3b")

agent = load_agent()

question = st.text_input("Enter an interview question:", placeholder="e.g., Tell me about an API security vulnerability you identified.")

if st.button("Generate Answer", type="primary"):
    if question.strip():
        context = agent.retriever.get_context(question)
        st.subheader("Generated Response")
        
        # Stream output token-by-token instantly
        st.write_stream(agent.stream_answer(question))
        
        with st.expander("View Evidence / Retrieved Context"):
            st.code(context, language="markdown")
    else:
        st.warning("Please enter a question.")
