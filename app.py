import streamlit as st
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="AI Virality Analyzer", page_icon="🔥", layout="centered")

# 🎨 PREMIUM UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}
h1 {
    text-align: center;
    font-size: 40px;
    color: white;
}
.stTextArea textarea {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
}
.stButton button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    border-radius: 12px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("AI Virality Analyzer 🦋")
st.write("Analyze text, images, and videos for viral potential")

# ✍️ Text input
text = st.text_area("Enter your content", height=150)

# 📁 File upload
uploaded_file = st.file_uploader("Upload Image or Video", type=["jpg", "png", "mp4"])

# Show uploaded content
if uploaded_file:
    if uploaded_file.type.startswith("image"):
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    elif uploaded_file.type.startswith("video"):
        st.video(uploaded_file)

# 🚀 Analyze
if st.button("🚀 Analyze"):
    if text.strip() == "" and not uploaded_file:
        st.warning("⚠️ Please enter content or upload a file")
    else:
        score = 0
        feedback = []

        # ===== TEXT ANALYSIS =====
        hook_score = 0
        emotion_score = 0
        question_score = 0
        length_score = 0
        audience_score = 0

        if text.strip() != "":
            st.markdown("## ✍️ Text Analysis")

            if text.lower().startswith(("stop", "wait", "don't", "do you")):
                hook_score = 3
                feedback.append("✅ Strong hook")
            else:
                feedback.append("❌ Add strong hook")

            if any(word in text.lower() for word in ["amazing", "shocking", "secret", "life"]):
                emotion_score = 2
                feedback.append("✅ Emotional words present")
            else:
                feedback.append("❌ Add emotional words")

            if "?" in text:
                question_score = 2
                feedback.append("✅ Question added")
            else:
                feedback.append("❌ Add a question")

            if len(text) < 80:
                length_score = 2
                feedback.append("✅ Good length")
            else:
                feedback.append("❌ Make it shorter")

            if "you" in text.lower():
                audience_score = 1
                feedback.append("✅ Targets audience")
            else:
                feedback.append("❌ Use 'you'")

        # ===== FILE ANALYSIS =====
        file_score = 0

        if uploaded_file:
            st.markdown("## 📁 File Analysis")

            if uploaded_file.type.startswith("image"):
                file_score = 2
                feedback.append("🖼️ Image boosts engagement")
                feedback.append("👉 Use bright colors & text")

            elif uploaded_file.type.startswith("video"):
                file_score = 3
                feedback.append("🎥 Video highly engaging")
                feedback.append("👉 Hook in first 3 sec")
                feedback.append("👉 Keep under 30 sec")

        # ===== FINAL SCORE =====
        score = hook_score + emotion_score + question_score + length_score + audience_score + file_score
        final_score = min(score, 10)

        st.subheader(f"🔥 Viral Score: {final_score}/10")
        st.progress(final_score / 10)

        st.divider()

        # ===== CHART =====
        st.markdown("### 📊 Content Strength Analysis")

        labels = ["Hook", "Emotion", "Question", "Length", "Audience"]
        values = [hook_score, emotion_score, question_score, length_score, audience_score]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title("Virality Factors")
        st.pyplot(fig)

        st.divider()

        # ===== FEEDBACK =====
        st.write("### 📊 Feedback:")
        for f in feedback:
            st.write("-", f)

        st.divider()

        # ===== IMPROVEMENT =====
        improved = ""

        if text.strip() != "":
            if hook_score == 0:
                improved += "Stop scrolling! 😳🔥 "

            improved += text

            if question_score == 0:
                improved += " Do you want to miss this?"

            improved += " Don't miss this!"
        else:
            improved = "Add catchy caption + strong hook!"

        st.write("### ✨ Suggested Improvement:")
        st.write(f"👉 {improved}")
# ================= CHATBOT =================
st.divider()
st.markdown("## 🤖 AI Assistant")

user_query = st.text_input("Ask about improving your content:")

if user_query:
    response = ""

    query = user_query.lower()

    if "hook" in query:
        response = "👉 Start with strong hooks like: 'Stop scrolling!', 'Wait!', 'You won’t believe this!'"

    elif "viral" in query:
        response = "👉 Viral content needs emotion, curiosity, and a strong first line."

    elif "improve" in query:
        response = "👉 Add emojis 😳🔥, ask questions, and keep content short and engaging."

    elif "video" in query:
        response = "👉 Keep videos short (<30s), add captions, and grab attention in first 3 seconds."

    elif "image" in query:
        response = "👉 Use bright colors, bold text, and human faces for better engagement."

    else:
        response = "👉 Try asking about hooks, captions, videos, or how to go viral!"

    st.write("🤖:", response)