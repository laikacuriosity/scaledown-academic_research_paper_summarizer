import streamlit as st
import os
import PyPDF2
import docx2txt
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit_mermaid as smd

@st.cache_resource
def load_summarizer():
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def extract_pdf_text(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_doc_text(uploaded_file):
    return docx2txt.process(uploaded_file)

def generate_roadmap_mermaid(text, detail_level="medium"):
    level_map = {
        "Simple": "Simple",
        "Medium": "Medium", 
        "Detailed": "Detailed"
    }
    internal_level = level_map.get(detail_level, "Medium")
    
    levels = {
        "Simple": "Keep simple: 3 main components, 1-2 subs each",
        "Medium": "Detailed: 3 main components, 2-3 subs each", 
        "Detailed": "Comprehensive: 3 main + detailed subcomponents"
    }
    
    prompt = ChatPromptTemplate.from_template(f"""
    Create Mermaid FLOWCHART roadmap from architecture text.
    {levels[internal_level]}
    
    Structure like:
    flowchart TD
      A[" ARCHITECTURE"] --> B["Main Component 1"]
      A --> C["Main Component 2"] 
      A --> D["Main Component 3"]
      B --> B1["Subcomponent"]
    
    Text: {{text}}
    Return ONLY valid Mermaid flowchart code (no ``` wrapper).
    """)
    
    chain = prompt | load_summarizer() | StrOutputParser()
    mermaid_code = chain.invoke({"text": text})
    return mermaid_code.strip("```mermaid").strip("```").strip()

st.title("Research Paper Summarization Tool")
st.markdown("")


tab1, tab2, tab3, tab4 = st.tabs(["Text", "PDF", "DOCX", "📎 File"])

with tab1:
    st.caption("*Want to see this as an interactive mindmap? Enable 'Generate Interactive Roadmap' in sidebar*")
    st.text_area("Paste your technical content:", height=300, key="text_input")

with tab2:
    st.caption("*Want to see this as an interactive mindmap? Enable 'Generate Interactive Roadmap' in sidebar*")
    uploaded_pdf = st.file_uploader("Upload PDF", type="pdf", key="pdf_input")
    if uploaded_pdf: 
        with st.spinner("Reading..."): 
            st.session_state.text_content = extract_pdf_text(uploaded_pdf)

with tab3:
    st.caption("*Want to see this as an interactive mindmap? Enable 'Generate Interactive Roadmap' in sidebar*")
    uploaded_docx = st.file_uploader("Upload DOCX", type="docx", key="docx_input")
    if uploaded_docx: 
        with st.spinner("Reading..."): 
            st.session_state.text_content = extract_doc_text(uploaded_docx)

with tab4:
    st.caption("*Want to see this as an interactive mindmap? Enable 'Generate Interactive Roadmap' in sidebar*")
    uploaded_file = st.file_uploader("Upload file", type=['txt','py','md','js'], key="file_input")
    if uploaded_file: 
        st.session_state.text_content = uploaded_file.read().decode("utf-8")


if 'text_content' in st.session_state:
    text = st.session_state.text_content
else:
    text = ""


with st.sidebar:
    st.header("⚙️ Settings")
    show_roadmap = st.checkbox("Generate Interactive Roadmap", value=False)
    
    if show_roadmap:
        detail_level = st.selectbox("Roadmap detail:", 
                                  ["Simple", "Medium", "Detailed"])
    else:
        detail_level = "Medium"
    
    # Summary Length Control
    st.subheader("Summary Length")
    summary_mode = st.radio("Choose:", 
                           [
                               "Simple (50-100 words)", 
                               "Medium (150-300 words)", 
                               "Detailed (400-600 words)",
                               "Custom"
                           ], index=1)
    
    if summary_mode == "Custom":
        custom_words = st.slider("Word count:", 25, 1000, 200, step=25)
        summary_words = custom_words
    else:
        word_ranges = {
            "Simple (50-100 words)": 75,
            "Medium (150-300 words)": 225, 
            "Detailed (400-600 words)": 500
        }
        summary_words = word_ranges[summary_mode]

    # Reset Button
    st.markdown("---")
    if st.button("Reset", key="sidebar_reset", help="Clear everything"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


button_label = "Summarize + Generate Roadmap (~{} words)" if show_roadmap else "Summarize Text (~{} words)"
if st.button(button_label.format(summary_words), type="primary", use_container_width=True):
    if text.strip():
        # Generate summary
        summary_prompt = ChatPromptTemplate.from_template(f"""
        ARCHITECTURE SUMMARY (exactly ~{summary_words} words, bullet points):
        Focus on: components, structure, flows, design patterns.
        Text: {{text}}
        """)
        
        summary = (summary_prompt | load_summarizer() | StrOutputParser()).invoke({"text": text})
        
        if show_roadmap:
            col1, col2 = st.columns([1, 1.2])
            with col1:
                st.success(f"**Summary (~{summary_words} words)**")
                st.markdown(summary)
                st.download_button("Download Summary", data=summary, file_name="summary.txt")
            
            with col2:
                st.success("**Interactive Roadmap**")
                with st.spinner("Generating..."):
                    mermaid_code = generate_roadmap_mermaid(text, detail_level)
                smd.st_mermaid(mermaid_code, height=700)
                st.download_button("Download Roadmap", data=mermaid_code, file_name="roadmap.mmd")
        else:
            st.success(f"**Summary (~{summary_words} words)**")
            st.markdown(summary)
            st.download_button("Download Summary", data=summary, file_name="summary.txt")
