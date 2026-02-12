---
title: FAQ
---

# ❓ Frequently Asked Questions

---

## 🔑 Do I need an API key?

No API key is required from end users.

The application securely uses a Google Gemini API key stored in the server environment (`st.secrets`). Users do not need to configure anything.

---

## 🗺️ What roadmap format gets exported?

The roadmap is exported as:

**`.mmd` — Mermaid flowchart format**

Compatible with:

- ✅ Mermaid Live Editor (mermaid.live)
- ✅ GitHub Markdown
- ✅ VS Code Mermaid preview
- ✅ Documentation systems
- ✅ Obsidian

---

## 📄 What file formats are supported?

You can upload:

- `.pdf`
- `.docx`
- `.txt`
- `.py`
- `.js`
- `.md`

---

## 📦 Are there file size limits?

File size limits are determined by Streamlit Cloud hosting constraints.

If deploying privately, limits depend on your server configuration.

---

## 💰 Is it free to use?

Yes — the hosted version is free to access.

No signup required. No user API key required.

---

## ⏱️ How fast is processing?

Typical processing times:

| Input Type | Estimated Time |
|------------|----------------|
| Short text | < 1 second |
| PDF (10 pages) | ~2 seconds |
| DOCX (20 pages) | ~2–3 seconds |
| Roadmap generation | 1–3 seconds |

Actual speed depends on document length and AI response time.

---

## 🛠️ Can I deploy it myself?

Yes.

1. Clone the repository  
2. Install dependencies  
3. Set your `GOOGLE_API_KEY`  
4. Run:


streamlit run app4.py
