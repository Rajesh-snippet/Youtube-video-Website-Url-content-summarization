<h1>🦜 YouTube & Website Content Summarizer (GenAI)</h1>

<p>
A simple GenAI-powered web app that summarizes content from 
<strong>YouTube videos</strong> and <strong>websites</strong> into concise insights using LLMs.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>Accepts both <strong>YouTube URLs</strong> and <strong>website links</strong></li>
  <li>Extracts:
    <ul>
      <li>YouTube transcripts</li>
      <li>Webpage content</li>
    </ul>
  </li>
  <li>Generates a <strong>300-word summary</strong></li>
  <li>Fast UI built with Streamlit</li>
  <li>Powered by LLaMA 3.3 via Groq</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>Streamlit</li>
  <li>LangChain</li>
  <li>Groq API (LLaMA 3.3)</li>
  <li>YouTube Transcript API</li>
  <li>UnstructuredURLLoader</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
├── app.py
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>⚙️ Installation & Setup</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/your-username/yt-website-summarizer.git
cd yt-website-summarizer
</code></pre>

<h3>2. Create virtual environment</h3>
<pre><code>conda create -p venv python=3.10 -y
conda activate ./venv
</code></pre>

<h3>3. Install dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4. Run the app</h3>
<pre><code>streamlit run app.py
</code></pre>

<hr>

<h2>🔑 Usage</h2>
<ol>
  <li>Enter your <strong>Groq API Key</strong></li>
  <li>Paste a <strong>YouTube or Website URL</strong></li>
  <li>Click <strong>Summarize</strong></li>
  <li>Get summary instantly</li>
</ol>

<hr>

<h2>🧠 How It Works</h2>
<ul>
  <li>Detects URL type (YouTube or website)</li>
  <li>Extracts transcript or webpage content</li>
  <li>Sends data to LLM with prompt</li>
  <li>Returns summarized output</li>
</ul>

<hr>

<h2>⚠️ Limitations</h2>
<ul>
  <li>Some YouTube videos may not have transcripts</li>
  <li>Some websites may block scraping</li>
  <li>Output depends on input quality</li>
</ul>

<hr>

<h2>🔮 Future Improvements</h2>
<ul>
  <li>Multi-language summaries</li>
  <li>Key insights extraction</li>
  <li>Custom summary length</li>
  <li>Download as PDF/Text</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>Feel free to fork this repo and submit a pull request.</p>

<hr>

