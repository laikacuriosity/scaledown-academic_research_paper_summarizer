# Academic Research Paper Summarizer Tool: AI-powered summaries + interactive mindmaps for research papers, PDFs & technical docs.<br>

Find a Live Demo here:<br>
https://academicresearchpapersummarizertool.streamlit.app/<br>

workflow:<br>
Upload file → set Word count → enable Mindmaps → Summarize!<br>


Features:<br>

 **PDF/DOCX/Text** support <br>
Custom word count (25-1000 words) <br>
Generate Interactive Mermaid mindmaps<br>
3 different range of detail levels<br>
Download results and mindmaps<br>


## Run on Your System<br>

pip install -r requirements.txt
streamlit run app4.py

For AI asisstance:<br>

1. Get free Google API key: https://aistudio.google.com/app/apikey<br>
2. Create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_api_key_here"
streamlit run app.py

## Folder structure
```
├── app.py              # Main app
└── requirements.txt    # Dependencies
```

## Tech Stack
```
Frontend: Streamlit + Mermaid.js<br>
AI: Google Gemini 2.5 Flash<br>
Extraction: PyPDF2 + docx2txt<br>
Deployed: Streamlit Cloud<br>
```<br>
<br>
## Dependencies
```
streamlit<br>
streamlit-mermaid<br>
langchain-google-genai<br>
langchain-core<br>
PyPDF2<br>
docx2txt<br>
```

## Contribute
Fork → Edit → PR



