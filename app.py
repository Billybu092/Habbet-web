import streamlit as st
import yt_dlp
import os

# --- BILEL'S PREMIUM BRANDING & STYLING ---
st.set_page_config(page_title="Habbet Eli t7ebb | Bilel Jelassi", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #0a0a0a; }
    .title-text { color: #ffffff; font-family: 'Arial Black'; text-align: center; font-size: 50px; margin-bottom: 0px; }
    .special-name { 
        color: #ffee00; 
        font-family: 'Courier New'; 
        text-align: center; 
        font-size: 26px; 
        font-weight: bold;
        text-shadow: 2px 2px 15px #ffee00;
        letter-spacing: 4px;
        margin-top: -10px;
    }
    .stButton>button { background-color: #ffee00; color: black; width: 100%; border-radius: 8px; font-weight: bold; border: none; height: 50px; font-size: 18px; }
    .stButton>button:hover { background-color: #ffcc00; color: white; transform: scale(1.02); transition: 0.3s; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title-text">Habbet Eli t7ebb</h1>', unsafe_allow_html=True)
st.markdown('<p class="special-name">ENGINEERED BY BILEL JELASSI</p>', unsafe_allow_html=True)

# --- USER INTERFACE ---
st.write("")
url = st.text_input("PASTE LINK HERE (YouTube, TikTok, Instagram, Facebook, etc.)", placeholder="https://www.socialmedia.com/video/...")

col1, col2 = st.columns(2)
with col1:
    fmt = st.selectbox("FORMAT", ["MP3 (Audio)", "MP4 (Video)"])
with col2:
    if fmt == "MP4 (Video)":
        quality = st.selectbox("RESOLUTION", ["1080p", "720p", "480p", "Best Available"])
    else:
        quality = st.selectbox("BITRATE", ["320kbps", "256kbps", "192kbps", "128kbps"])

# --- EXTRACTION ENGINE ---
if st.button("EXTRACT NOW"):
    if not url:
        st.warning("Bilel says: Please paste a link first!")
    else:
        try:
            with st.spinner("Bilel is bypassing restrictions..."):
                save_path = "downloads"
                if not os.path.exists(save_path): os.makedirs(save_path)

                # Cleaning quality strings
                res = quality.replace("p", "")
                bitrate = quality.replace("kbps", "")

                ydl_opts = {
                    'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                    'quiet': True,
                    'no_warnings': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                    'referer': 'https://www.google.com/',
                }

                if fmt == "MP3 (Audio)":
                    ydl_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': bitrate if bitrate != "Best Available" else "192",
                        }],
                    })
                else:
                    # Using 'best' instead of format merging prevents the FFMPEG error on Cloud
                    if quality == "Best Available":
                        ydl_opts.update({'format': 'best'})
                    else:
                        ydl_opts.update({'format': f'best[height<={res}]'})

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    file_path = ydl.prepare_filename(info)
                    if fmt == "MP3 (Audio)":
                        file_path = file_path.rsplit('.', 1)[0] + '.mp3'

                with open(file_path, "rb") as f:
                    st.balloons()
                    st.success("Extracted successfully! 🙂")
                    st.download_button(label="📥 DOWNLOAD FILE", data=f, file_name=os.path.basename(file_path))

        except Exception as e:
            st.error("SYSTEM ERROR: This link is private or restricted. Try another public link!")

# --- DONATION SECTION ---
st.divider()
st.markdown("<h3 style='text-align: center; color: white;'>Support the Developer</h3>", unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><a href="https://www.buymeacoffee.com/BilelJelassi" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 50px !important;width: 180px !important;" ></a></div>', unsafe_allow_html=True)
