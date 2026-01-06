import streamlit as st
import yt_dlp
import os

# --- TUNISIAN NEON & FLAG STYLING ---
st.set_page_config(page_title="Habbet Eli t7ebb | Bilel Jelassi", page_icon="🇹🇳", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    .main { background-color: #0a0a0a; }
    
    /* Neon Titles */
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
        margin-bottom: 30px;
    }

    /* Platform Dashboard Tabs */
    .platform-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-bottom: 25px;
    }
    .badge {
        padding: 8px 15px;
        border-radius: 20px;
        font-family: 'Orbitron', sans-serif;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        border: 1px solid #444;
        background: #1e1e1e; /* Dark background even in light mode */
        color: #ffee00;      /* Yellow text is now always visible */
        margin: 5px;
        display: inline-block;
    }
    .badge-active {
        border-color: #ff0000;
        box-shadow: 0 0 15px #ff0000;
        color: #ffffff;
    }
    .badge:hover {
        color: #fff;
        border-color: #ff0000;
        box-shadow: 0 0 10px #ff0000;
    }
    .badge-active {
        color: #fff;
        border-color: #ffee00;
        box-shadow: 0 0 10px #ffee00;
        background: rgba(255, 238, 0, 0.1);
    }

    /* Buttons and Cards */
    .stButton>button {
        background: linear-gradient(90deg, #ff0000, #cc0000);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        height: 50px;
        border: 1px solid white;
        width: 100%;
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
        font-family: 'Orbitron', sans-serif;
    }
    .android-hype {
        background-color: #0d1a0d;
        border: 2px dashed #00ff00;
        color: #00ff00 !important;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-family: 'Orbitron', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER & PLATFORM TABS ---
st.markdown('<p style="text-align: center; font-size: 40px; margin:0;">🇹🇳</p>', unsafe_allow_html=True)
st.markdown('<h1 class="neon-title">HABBET ELI T7EBB</h1>', unsafe_allow_html=True)
st.markdown('<p class="neon-name">ENGINEERED BY BILEL JELASSI</p>', unsafe_allow_html=True)

# Creative Platform Dashboard
st.markdown("""
<div class="platform-container">
    <div class="badge badge-active">TikTok</div>
    <div class="badge badge-active">Facebook</div>
    <div class="badge badge-active">Instagram</div>
    <div class="badge badge-active">Twitter / X</div>
    <div class="badge">YouTube</div>
    <div class="badge">Dailymotion</div>
    <div class="badge">Vimeo</div>
    <div class="badge">SoundCloud</div>
</div>
""", unsafe_allow_html=True)

# --- USER INPUTS ---
url = st.text_input("PASTE LINK BELOW", placeholder="https://tiktok.com/@user/video/...")

# --- DYNAMIC YOUTUBE ALERT ---
if "youtube.com" in url or "youtu.be" in url:
    st.error("⚠️ **YouTube Cloud Restriction Detected**")
    st.info("YouTube frequently blocks cloud servers like this one. If the extraction fails below, please use our **Windows Desktop Application** for a 100% success rate on YouTube!")
    
    col_win, col_and = st.columns(2)
    with col_win:
        st.markdown('<a href="https://github.com/Billybu092/Habbet-web/releases/download/v1.0.0/Habbet_Eli_t7ebb_Setup.exe" class="win-download">📥 WINDOWS APP (FREE)</a>', unsafe_allow_html=True)
    with col_and:
        st.markdown('<div class="android-hype">📱 ANDROID APP<br>COMING SOON!<br>STAY TUNED :)</div>', unsafe_allow_html=True)
    st.divider()

# --- SELECTORS ---
col_f, col_q = st.columns(2)
with col_f:
    fmt = st.selectbox("FORMAT", ["MP4 (Video)", "MP3 (Audio)"])
with col_q:
    if fmt == "MP4 (Video)":
        quality = st.selectbox("RESOLUTION", ["Best", "1080p", "720p", "480p"])
    else:
        quality = st.selectbox("BITRATE", ["320kbps", "256kbps", "192kbps", "128kbps"])

# --- EXTRACTION ENGINE ---
if st.button("🚀 LAUNCH EXTRACTION"):
    if not url:
        st.error("Missing Link!")
    else:
        try:
            with st.spinner("Extracting..."):
                save_path = "downloads"
                if not os.path.exists(save_path): os.makedirs(save_path)
                
                res = quality.replace("p", "")
                bit_val = quality.replace("kbps", "")

                ydl_opts = {
                    'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                    'quiet': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                }

                if "MP3" in fmt:
                    ydl_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': bit_val}]
                    })
                else:
                    ydl_opts.update({'format': f'best[height<={res}]' if res != "Best" else 'best'})

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    file_path = ydl.prepare_filename(info)
                    if "MP3" in fmt: file_path = file_path.rsplit('.', 1)[0] + '.mp3'

                with open(file_path, "rb") as f:
                    st.balloons()
                    st.success("Success! 🇹🇳")
                    st.download_button(label="📥 DOWNLOAD NOW", data=f, file_name=os.path.basename(file_path))

        except Exception:
            st.error("🚨 Server Blocked. Use the Windows App link for YouTube!")

# --- FOOTER ---
st.divider()
st.markdown('<div style="text-align: center;"><a href="https://www.buymeacoffee.com/BilelJelassi" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" style="height: 45px !important;" ></a></div>', unsafe_allow_html=True)


