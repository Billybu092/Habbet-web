import streamlit as st
import yt_dlp
import os
import time

# --- BILEL'S WEB STYLING ---
st.set_page_config(page_title="Habbet Eli t7ebb | Bilel Jelassi", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #0a0a0a; }
    h1 { color: #ffee00; font-family: 'Arial Black'; text-align: center; }
    p { color: #888; text-align: center; font-weight: bold; }
    .stButton>button { background-color: #ffee00; color: black; width: 100%; border-radius: 5px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("Habbet Eli t7ebb")
st.markdown("<p>ENGINEERED BY BILEL JELASSI</p>", unsafe_allow_html=True)

# --- USER INPUTS ---
url = st.text_input("PASTE YOUR LINK HERE", placeholder="https://youtube.com/...")

col1, col2 = st.columns(2)
with col1:
    fmt = st.selectbox("FORMAT", ["MP4 (Video)", "MP3 (Audio)"])
with col2:
    if fmt == "MP4 (Video)":
        quality = st.selectbox("RESOLUTION", ["2160p", "1440p", "1080p", "720p", "480p"])
    else:
        quality = st.selectbox("BITRATE", ["320kbps", "256kbps", "192kbps", "128kbps"])

# --- EXTRACTION ENGINE ---
if st.button("EXTRACT NOW"):
    if not url:
        st.error("Bilel says: Please paste a link first!")
    else:
        try:
            with st.spinner("Bilel is serving your coffee..."):
                save_path = "downloads"
                if not os.path.exists(save_path): os.makedirs(save_path)
                
                res = quality.replace("p", "")
                bitrate = quality.replace("kbps", "")
                
                ydl_opts = {
                    'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                    'quiet': True
                }

                if "MP3" in fmt:
                    ydl_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': bitrate}]
                    })
                else:
                    ydl_opts.update({'format': f'bestvideo[height<={res}]+bestaudio/best'})

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    file_path = ydl.prepare_filename(info)
                    if "MP3" in fmt: file_path = file_path.rsplit('.', 1)[0] + '.mp3'

                with open(file_path, "rb") as f:
                    st.balloons()
                    st.success("You file downloaded succefully 🙂")
                    st.download_button(label="📥 SAVE FILE TO DEVICE", data=f, file_name=os.path.basename(file_path))
                    
        except Exception as e:
            st.error(f"SYSTEM ERROR: {e}")

st.divider()
st.markdown("[☕ Support the Project (Donate)](https://www.buymeacoffee.com/BilelJelassi)")