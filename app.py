import streamlit as st
import yt_dlp
import os

# --- BILEL'S NEON PREMIUM BRANDING ---
st.set_page_config(page_title="Habbet Eli t7ebb | Bilel Jelassi", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #050505; }
    .title-text { 
        color: #ffffff; 
        font-family: 'Arial Black'; 
        text-align: center; 
        font-size: 45px; 
        text-shadow: 0 0 10px #ffee00;
    }
    .special-name { 
        color: #ffee00; 
        font-family: 'Courier New'; 
        text-align: center; 
        font-size: 24px; 
        font-weight: bold;
        text-shadow: 0 0 20px #ffee00, 0 0 30px #ffcc00; /* NEON GLOW */
        letter-spacing: 5px;
    }
    .stButton>button { 
        background: linear-gradient(45deg, #ffee00, #ff9900); 
        color: black; 
        font-weight: bold; 
        border-radius: 10px; 
        border: none;
        height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title-text">Habbet Eli t7ebb</h1>', unsafe_allow_html=True)
st.markdown('<p class="special-name">ENGINEERED BY BILEL JELASSI</p>', unsafe_allow_html=True)

# --- MULTI-PLATFORM INPUT ---
url = st.text_input("PASTE ANY LINK (YouTube, TikTok, FB, Instagram, etc.)", placeholder="https://...")

col1, col2 = st.columns(2)
with col1:
    fmt = st.selectbox("FORMAT", ["MP3 (Audio)", "MP4 (Video)"])
with col2:
    quality = st.selectbox("QUALITY", ["Best Available", "1080p", "720p", "480p"])

if st.button("🚀 EXTRACT NOW"):
    if not url:
        st.warning("Please paste a link first!")
    else:
        try:
            with st.spinner("Bilel is fighting the servers..."):
                save_path = "downloads"
                if not os.path.exists(save_path): os.makedirs(save_path)

                # These options use a "Mobile User Agent" to bypass YouTube's PC block
                ydl_opts = {
                    'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                    'quiet': True,
                    'no_warnings': True,
                    'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
                    'referer': 'https://www.google.com/',
                }

                if fmt == "MP3 (Audio)":
                    ydl_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]
                    })
                else:
                    # 'best' is safer for web apps to avoid FFMPEG merge errors
                    ydl_opts.update({'format': 'best'})

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    file_path = ydl.prepare_filename(info)
                    if fmt == "MP3 (Audio)": file_path = file_path.rsplit('.', 1)[0] + '.mp3'

                with open(file_path, "rb") as f:
                    st.balloons()
                    st.success("Success! 🙂")
                    st.download_button(label="📥 DOWNLOAD NOW", data=f, file_name=os.path.basename(file_path))

        except Exception as e:
            st.error("YouTube is currently blocking this server. Try a TikTok or FB link, or try again in 5 minutes!")

# --- DONATION ---
st.divider()
st.markdown('<div style="text-align: center;"><a href="https://www.buymeacoffee.com/BilelJelassi"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="160"></a></div>', unsafe_allow_html=True)
