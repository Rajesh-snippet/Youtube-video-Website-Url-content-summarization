import validators
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_community.document_loaders import UnstructuredURLLoader
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

## Streamlit APP
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

prompt_template = """
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])


def extract_video_id(url):
    """Extract YouTube video ID from URL"""
    parsed = urlparse(url)
    if parsed.hostname in ("youtu.be",):
        return parsed.path[1:]
    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(parsed.query).get("v", [None])[0]
    return None


def get_youtube_transcript(url):
    """Fetch transcript using youtube_transcript_api v1.2.4"""
    video_id = extract_video_id(url)
    if not video_id:
        raise ValueError("Could not extract video ID from the URL. Please check the URL and try again.")

    ytt_api = YouTubeTranscriptApi()
    fetched = ytt_api.fetch(video_id)
    transcript = " ".join([snippet.text for snippet in fetched])
    return transcript


if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide both the Groq API Key and a URL to get started.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YouTube video URL or a website URL.")
    else:
        try:
            with st.spinner("Fetching and summarizing content..."):

                ## Initialize LLM and chain inside button click (after API key is available)
                llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)
                chain = prompt | llm | StrOutputParser()

                ## Load content based on URL type
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    combined_text = get_youtube_transcript(generic_url)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                        }
                    )
                    docs = loader.load()
                    combined_text = " ".join([doc.page_content for doc in docs])

                ## Guard against empty content
                if not combined_text.strip():
                    st.error("Could not extract any content from the URL. The video may have no captions, or the website may be blocking access.")
                else:
                    output_summary = chain.invoke({"text": combined_text})
                    st.success(output_summary)

        except ValueError as ve:
            st.exception(f"URL Error: {ve}")
        except Exception as e:
            st.exception(f"Exception: {e}")