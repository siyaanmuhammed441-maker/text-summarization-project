import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load Model
@st.cache_resource
def load_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    return tokenizer, model

tokenizer, model = load_model()

# Title
st.title("📝 Text Summarization App")
st.write("Enter a long article and click Generate Summary.")

# Input
article = st.text_area("Enter Text", height=300)

# Button
if st.button("Generate Summary"):

    if article.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_text = "summarize: " + article

        inputs = tokenizer(
            input_text,
            return_tensors="pt",
            max_length=512,
            truncation=True
        )

        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=120,
            min_length=30,
            num_beams=4,
            early_stopping=True
        )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        st.subheader("Generated Summary")
        st.success(summary)