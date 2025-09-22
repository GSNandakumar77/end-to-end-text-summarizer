📝 End-to-End Text Summarizer with Google Pegasus (Samsum Dataset)

This repository contains an end-to-end abstractive text summarization system built using Google’s Pegasus model fine-tuned on the Samsum dataset, and deployed with FastAPI for real-time inference.

🚀 Key Features

Preprocessing and training on the Samsum dataset

Fine-tuning Pegasus Seq2Seq model for dialogue summarization

Training pipeline with Hugging Face Trainer API

Saving & loading of trained model and tokenizer

FastAPI endpoint for real-time text summarization

Modular design for easy extension and deployment

📂 Project Structure
├── config/                 # Config files (paths, parameters)
├── src/                    # Core training, preprocessing & utility scripts
├── artifacts/              # Saved models, tokenizers, and logs
├── app.py                  # FastAPI app for serving the model
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

⚙️ Tech Stack

Python

Hugging Face Transformers

Datasets

PyTorch

FastAPI

Uvicorn (for running the API server)

📊 Dataset

Samsum Dataset → a large collection of messenger-style conversations with human-written summaries.
📌 Samsum Dataset on HuggingFace

🔥 Training Workflow

Load Pegasus tokenizer & model checkpoint

Load and preprocess Samsum dataset

Train model with Trainer API

Save model & tokenizer into artifacts

Expose inference API with FastAPI

▶️ Running the API
1. Install dependencies
pip install -r requirements.txt

2. Start FastAPI server
uvicorn app:app --reload

3. Test the API

Send a POST request to /summarize:

Request:

{
  "text": "Hi, I just wanted to let you know that the meeting is rescheduled for tomorrow at 10am."
}


Response:

{
  "summary": "Meeting rescheduled for tomorrow at 10am."
}

🌟 Applications

Customer support chat summarization

Meeting notes generation

Conversational AI preprocessing

Dialogue compression for mobile devices
