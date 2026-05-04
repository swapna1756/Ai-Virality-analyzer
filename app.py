import streamlit as st
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="AI Virality Analyzer", page_icon="🔥", layout="centered")

# 🎨 UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}
h1 {
    text-align: center;
    color: white;
}
.stButton button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Virality Analyzer 🦋")
st.write("Analyze text, images, and videos for viral potential")

text = st.text_area("Enter your content", height=150)
uploaded_file = st.file_uploader("Upload Image or Video", type=["jpg", "png", "mp4"])

# Show file
if uploaded_file:
    if uploaded_file.type.startswith("image"):
        st.image(uploaded_file)
    elif uploaded_file.type.startswith("video"):
        st.video(uploaded_file)

# 🚀 Analyze
if st.button("🚀 Analyze"):
    if text.strip() == "" and not uploaded_file:
        st.warning("⚠️ Please enter content or upload a file")
    else:
        feedback = []

        # ===== SCORES =====
        hook_score = 0
        emotion_score = 0
        question_score = 0
        length_score = 0
        audience_score = 0
        file_score = 0

        # ===== HOOK =====
        hook_text = text[:50].lower()
        if any(word in hook_text for word in ["stop", "wait", "don't", "you won't"]):
            hook_score = 30
            feedback.append("🔥 Strong hook in first 3 seconds")
        else:
            feedback.append("❌ Weak hook — improve opening line")

        # ===== EMOTION =====
        if any(word in text.lower() for word in ["amazing", "shocking", "secret", "life"]):
            emotion_score = 20
            feedback.append("✅ Emotional words present")
        else:
            feedback.append("❌ Add emotional triggers")

        # ===== QUESTION =====
        if "?" in text:
            question_score = 20
            feedback.append("✅ Question increases engagement")
        else:
            feedback.append("❌ Add a question")

        # ===== LENGTH =====
        if len(text) < 80:
            length_score = 15
            feedback.append("✅ Good short content")
        else:
            feedback.append("❌ Make content shorter")

        # ===== AUDIENCE =====
        if "you" in text.lower():
            audience_score = 15
            feedback.append("✅ Targets audience well")
        else:
            feedback.append("❌ Use 'you'")

        # ===== FILE =====
        if uploaded_file:
            if uploaded_file.type.startswith("image"):
                file_score = 10
                feedback.append("🖼️ Image boosts engagement")
            elif uploaded_file.type.startswith("video"):
                file_score = 15
                feedback.append("🎥 Video increases viral potential")

        # ===== FINAL SCORE =====
        final_score = min(
            hook_score + emotion_score + question_score + length_score + audience_score + file_score,
            100
        )

        # ===== SCORE =====
        st.subheader(f"🔥 Viral Score: {final_score}/100")
        st.progress(final_score / 100)

        st.caption("Score based on hook, emotion, engagement, and structure analysis")
        st.caption("AI model simulates virality using engagement heuristics")
        st.caption("Future version will use real AI models for video frame analysis and trend prediction")

        # ===== VIRAL LEVEL =====
        if final_score > 80:
            st.success("🚀 High chance to go viral!")
        elif final_score > 50:
            st.warning("⚡ Moderate viral potential")
        else:
            st.error("❌ Low viral potential")

        st.divider()

        # ===== HOOK =====
        st.markdown("### 🎬 Hook Analysis")
        if hook_score > 0:
            st.success("Strong first 3 seconds hook")
        else:
            st.error("Weak opening — improve first 3 seconds")

        # ===== PACING =====
        st.markdown("### ⏱️ Pacing Analysis")
        if len(text) < 60:
            st.success("Fast-paced content")
        elif len(text) < 120:
            st.warning("Moderate pacing")
        else:
            st.error("Too slow — reduce length")

        st.divider()

        # ===== THUMBNAIL =====
        if uploaded_file and uploaded_file.type.startswith("image"):
            st.markdown("### 🖼️ Thumbnail Rating")
            thumb_score = 50 if uploaded_file.size > 100000 else 30
            st.write(f"Thumbnail Score: {thumb_score}/100")
            st.write("- Use bold text")
            st.write("- Include human faces")
            st.write("- Use bright contrast colors")

        st.divider()

        # ===== CHART =====
        st.markdown("### 📊 Score Breakdown")
        labels = ["Hook", "Emotion", "Question", "Length", "Audience"]
        values = [
            hook_score or 5,
            emotion_score or 5,
            question_score or 5,
            length_score or 5,
            audience_score or 5
        ]

        fig, ax = plt.subplots()
        ax.bar(labels, values)

        for i, v in enumerate(values):
            ax.text(i, v + 1, str(v), ha='center')

        st.pyplot(fig)

        st.divider()

        # ===== FEEDBACK =====
        st.write("### 📊 Feedback:")
        for f in feedback:
            st.write("-", f)

        st.divider()

        # ===== CAPTION =====
        st.markdown("### 📝 Caption Optimization")
        st.write("👉 Keep it short (5–10 words)")
        st.write("👉 Add curiosity + emotion")
        st.write("👉 Include a question")

        # ===== COMPETITOR =====
        st.markdown("### 🆚 Competitor Comparison")
        st.write("Top viral content usually scores above 75.")
        if final_score > 70:
            st.success("Your content is ABOVE average 🔥")
        else:
            st.warning("Your content is BELOW top viral content ⚠️")

        # ===== HASHTAGS =====
        st.markdown("### 🔥 Suggested Hashtags")
        hashtags = ["#viral", "#fyp", "#trending"]

        if "love" in text.lower():
            hashtags.append("#love")
        if "motivation" in text.lower():
            hashtags.append("#motivation")
        if "funny" in text.lower():
            hashtags.append("#funny")
        if "fitness" in text.lower():
            hashtags.append("#fitness")

        st.write(" ".join(hashtags))

        # ===== AUDIO =====
        st.markdown("### 🎵 Trending Audio")

        if "motivation" in text.lower():
            st.write("🎧 Motivation Beat 🔥")
        elif "sad" in text.lower():
            st.write("🎧 Emotional Piano 🎹")
        elif "funny" in text.lower():
            st.write("🎧 Meme Sound 😂")
        else:
            st.write("🎧 Viral Beat Drop")
            st.write("🎧 Chill Remix")
            st.write("🎧 Trending Reels Sound")

        # ===== IMPROVED =====
        improved = ""
        if not text.lower().startswith(("stop", "wait", "don't")):
            improved += "Stop scrolling! "
        improved += text
        if "?" not in text:
            improved += " Do you want to miss this?"
        improved += " 😳🔥 You won’t believe this!"

        st.markdown("### ✨ Improved Version")
        st.write(improved)

        # ===== DOWNLOAD =====
        report = f"""
Viral Score: {final_score}/100

Feedback:
{chr(10).join(feedback)}

Improved Version:
{improved}
"""
        st.download_button("📥 Download Report", report, file_name="virality_report.txt")


# ===== CHATBOT =====
st.divider()
st.markdown("## 🤖 AI Assistant")

user_query = st.text_input("Ask about improving your content:")

if user_query:
    query = user_query.lower()

    if "hook" in query:
        st.write("👉 Use hooks like: 'Stop scrolling!', 'Wait!', 'You won’t believe this!'")
    elif "viral" in query:
        st.write("👉 Viral content needs emotion, curiosity, and strong opening")
    elif "video" in query:
        st.write("👉 Keep videos under 30 sec & hook in first 3 seconds")
    elif "caption" in query:
        st.write("👉 Keep captions short + emotional + curiosity-driven")
    else:
        st.write("👉 Ask about hooks, captions, or viral tips!")
