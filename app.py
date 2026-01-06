import streamlit as st
import yt_dlp
import os

# --- TUNISIAN NEON & FLAG STYLING ---
st.set_page_config(page_title="Habbet Eli t7ebb | Bilel Jelassi", page_icon="🇹🇳")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    .main { background-color: #0a0a0a; }
    .neon-title {
        font-family: 'Orbitron', sans-serif;
        color: #fff;
        text-align: center;
        font-size: 50px;
        font-weight: 900;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000;
        margin-bottom: 0px;
    }
    .neon-name {
        font-family: 'Orbitron', sans-serif;
        color: #ffee00;
        text-align: center;
        font-size: 18px;
        letter-spacing: 5px;
        text-shadow: 0 0 10px #ffee00;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff0000, #cc0000);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        height: 50px;
        border: 1px solid white;
    }
    .win-download {
        background-color: #1e1e1e;
        border: 2px solid #ffee00;
        color: #ffee00 !important;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        text-decoration: none;
        display: block;
        font-weight: bold;
        margin-top: 10px;
        font-family: 'Orbitron', sans-serif;
    }
    .platform-badge {
        background-color: #222;
        color: #ffee00;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 12px;
        margin: 2px;
        display: inline-block;
        border: 1px solid #444;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<p style="text-align: center; font-size: 40px; margin:0;">🇹🇳</p>', unsafe_allow_html=True)
st.markdown('<h1 class="neon-title">HABBET ELI T7EBB</h1>', unsafe_allow_html=True)
st.markdown('<p class="neon-name">ENGINEERED BY BILEL JELASSI</p>', unsafe_allow_html=True)

st.markdown('<div style="text-align: center;">'
            '<span class="platform-badge">TikTok</span>'
            '<span class="platform-badge">Facebook</span>'
            '<span class="platform-badge">Instagram</span>'
            '<span class="platform-badge">YouTube</span>'
            '</div>', unsafe_allow_html=True)

st.write("")

# --- USER INPUTS ---
url = st.text_input("PASTE YOUR LINK HERE", placeholder="https://...")

# --- THE SMART YOUTUBE WARNING & WINDOWS REDIRECT ---
if "youtube.com" in url or "youtu.be" in url:
    st.error("⚠️ **YouTube Cloud Restriction Detected**")
    st.info("YouTube frequently blocks cloud servers like this one. If the extraction fails below, please use our **Windows Desktop Application** for a 100% success rate on YouTube!")
    # Replace the link below with your actual GitHub release link
    st.markdown('<a href="https://github.com/Billybu092/Project-Sentinel/raw/main/Habbet_Eli_t7ebb_Setup.exe" class="win-download">📥 DOWNLOAD WINDOWS APP (v1.0)</a>', unsafe_allow_html=True)
    st.write("")

fmt = st.selectbox("STEP 1: CHOOSE FORMAT", ["MP4 (Video)", "MP3 (Audio)"])

if fmt == "MP4 (Video)":
    quality = st.selectbox("STEP 2: SELECT RESOLUTION", ["Best Available", "1080p", "720p", "480p"])
else:
    quality = st.selectbox("STEP 2: SELECT BITRATE", ["320kbps", "256kbps", "192kbps", "128kbps"])

# --- ENGINE ---
if st.button("🚀 START EXTRACTION"):
    if not url:
        st.error("Please paste a link first!")
    else:
        try:
            with st.spinner("Bilel's Engine is processing..."):
                save_path = "downloads"
                if not os.path.exists(save_path): os.makedirs(save_path)
                
                res = quality.replace("p", "")
                bitrate = quality.replace("kbps", "")

                ydl_opts = {
                    'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                    'quiet': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                }

                if "MP3" in fmt:
                    ydl_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': bitrate}]
                    })
                else:
                    ydl_opts.update({'format': f'best[height<={res}]' if res != "Best Available" else 'best'})

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    file_path = ydl.prepare_filename(info)
                    if "MP3" in fmt: file_path = file_path.rsplit('.', 1)[0] + '.mp3'

                with open(file_path, "rb") as f:
                    st.balloons()
                    st.success("Extraction Successful! 🇹🇳")
                    st.download_button(label="📥 SAVE TO DEVICE", data=f, file_name=os.path.basename(file_path))

        except Exception as e:
            st.error("🚨 **Server Blocked:** Please use the Windows App button above for YouTube videos!")

# --- FOOTER ---
st.divider()
st.markdown('<div style="text-align: center;"><a href="https://www.buymeacoffee.com/BilelJelassi" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" style="height: 45px !important;" ></a></div>', unsafe_allow_html=True)
