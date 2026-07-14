from pyrogram import Client

# 1. YAHAN APNI DETAILS DAAL (Wapas se ek baar daal de)
api_id = 33897696           # Apna asli API ID yahan daal (Bina quotes ke)
api_hash = "16d900e51149b8a3aae502a043ce416d" # Apna asli API Hash yahan daal (Quotes ke andar)

# 2. CLIENT SETUP (Session file use karega jo pehle ban chuki hai)
app = Client("the19company_session", api_id=api_id, api_hash=api_hash)

async def main():
    async with app:
        print("🚀 Telegram se connect ho gaya!")
        
        # 3. ANDROID FILE PATH
        # Dhyan rakhna ki 'test.mp4' naam ki video tere Download folder me zaroor ho
        video_path = "/storage/emulated/0/Download/test.mp4" 
        
        # 4. TESTING TARGET: 'me' (Tere khud ke Saved Messages me jayega)
        target_chat = "me" 
        
        print("⏳ Video upload shuru ho gayi hai, terminal pe nazar rakh...")
        
        try:
            msg = await app.send_video(
                chat_id=target_chat, 
                video=video_path,
                caption="The 19 Company - Engine Test 🚀 (Saved Messages)"
            )
            print(f"🔥 Bawal! Video Uploaded! File ID: {msg.video.file_id}")
        except Exception as e:
            # Agar file nahi mili ya koi error aaya, toh yahan red color me dikhayega
            print(f"❌ Error aaya bhai: {e}")

# 5. RUN ENGINE
print("Engine start ho raha hai...")
app.run(main())
