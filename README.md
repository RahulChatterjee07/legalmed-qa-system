# 🏥📄 LegalMed QnA System

This project simulates a **multimodal Question Answering system** for legal and medical documents — designed for workflows such as personal injury cases, disability assessments, and insurance claims.

It demonstrates:
- Claude Sonnet QnA via AWS Bedrock
- Retrieval-Augmented Generation (RAG)
- Prompt templating and structured outputs
- Multimodal inputs (text + image)

---

## 🚀 Features

- 🧠 **LangChain-style prompt composition**
- 🔍 **Simulated knowledge base retrieval** using keyword matching
- 🖼️ **Base64-encoded image input support** for scanned forms
- 🧾 **Structured LLM outputs** (answer + source)
- 🔄 **Multiple question scenarios tested** for different patient reports

---

## 📂 Project Structure

```
legalmed-qa-system/
├── data/
│   ├── sample_documents/       # Mock TXT files simulating real reports
│   ├── textract_outputs/       # (reserved for layout-aware mock data)
│   └── knowledge_base/         # Context chunks used for simulated RAG
├── qa_engine/
│   ├── qa_pipeline.py          # QnA formatting logic
│   ├── retriever.py            # Retrieves relevant doc context
│   └── prompt_templates.yaml   # Claude-ready prompt instructions
├── notebooks/
│   └── demo.ipynb              # End-to-end QnA simulation
├── requirements.txt
└── README.md
```

---

## 💡 Example Output

**Question:** “When was the last assessment?”  
📄 Retrieved context:  
`"The last assessment was performed on March 12, 2024."`  
🧠 Claude Sonnet Output:
```json
{
  "answer": "March 12, 2024",
  "source": "Form A, Page 2"
}
```

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## 🧪 Run Demo

Launch the notebook and simulate a Claude Sonnet QnA session:

```bash
cd notebooks
jupyter notebook demo.ipynb
```

---

Made with ❤️ by **Rahul Chatterjee**
