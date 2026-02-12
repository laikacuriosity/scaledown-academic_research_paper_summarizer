---
title: Formats
---

#  File Format Support

The Research Paper Summarization Tool supports multiple academic and technical formats.

---

##  Supported File Types

| Format | File Type | Processing Method |
|--------|----------|------------------|
| PDF    | `.pdf`   | PyPDF2 extraction |
| DOCX   | `.docx`  | docx2txt parsing |
| Text   | `.txt`   | Direct read |
| Code   | `.py` `.js` `.md` | UTF-8 decoding |

---

## 📄 PDF Processing

- Extracts full page text using **PyPDF2**
- Processes multi-page documents
- Designed for academic research papers

---

## 📝 DOCX Processing

- Uses **docx2txt**
- Supports:
  - Theses
  - Reports
  - Academic manuscripts

---

## 💻 Code & Text Files

- Python (`.py`)
- JavaScript (`.js`)
- Markdown (`.md`)
- Plain text (`.txt`)

All files are read as UTF-8 text before summarization.

---

## 🧠 Output Files

| Output | File Name | Format |
|--------|----------|--------|
| Summary | `summary.txt` | Plain text |
| Roadmap | `roadmap.mmd` | Mermaid flowchart |

---

## ⚙️ Processing Behavior

- Summary length:
  - Simple: ~75 words
  - Medium: ~225 words
  - Detailed: ~500 words
  - Custom: 25–1000 words

- Optional interactive roadmap generation
- Roadmap detail levels:
  - Simple
  - Medium
  - Detailed

---

!!! note
    File size limits are governed by Streamlit Cloud hosting constraints.
