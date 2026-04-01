🦜 YouTube & Website Content Summarizer (GenAI)

A simple GenAI-powered web app that summarizes content from YouTube videos and websites into concise, meaningful insights using Large Language Models (LLMs).

🚀 Features:
🔗 Accepts both YouTube URLs and website links
📄 Extracts:
YouTube transcripts
Webpage content
✨ Generates a clear 300-word summary
⚡ Fast and interactive UI using Streamlit
🧠 Powered by LLM (LLaMA 3.3 via Groq)

🛠️ Tech Stack:
Python
Streamlit – UI framework
LangChain – LLM orchestration
Groq API – LLaMA 3.3 model
YouTube Transcript API – transcript extraction
UnstructuredURLLoader – website content extraction

📂 Project Structure
├── app.py                 # Main Streamlit application
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

⚙️ Installation & Setup:
1. Clone the repository
git clone https://github.com/your-username/yt-website-summarizer.git
cd yt-website-summarizer
2. Create a virtual environment
conda create -p venv python=3.10 -y
conda activate ./venv
3. Install dependencies
pip install -r requirements.txt
4. Run the app
streamlit run app.py

🔑 Usage:
Enter your Groq API Key in the sidebar
Paste a YouTube or Website URL
Click "Summarize"
Get a clean summary in seconds

🧠 How It Works:
Detects whether the input is a YouTube link or a website
For YouTube:
Extracts video ID
Fetches transcript using YouTube Transcript API
For websites:
Loads content using LangChain’s URL loader
Sends extracted text to LLM with a prompt
Returns a structured summary

⚠️ Limitations:
Some YouTube videos may not have transcripts
Certain websites may block scraping
Output quality depends on input content and prompt

🔮 Future Improvements:
🌍 Multi-language summaries
📌 Key insights / bullet-point extraction
📊 Summary length customization
🧾 Download summaries (PDF/Text)
🎯 Better error handling
