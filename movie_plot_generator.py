# Import necessary libraries
import streamlit as st
from transformers import pipeline
import random
import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK tokenizer (only once)
nltk.download('punkt')

# Load the DistilGPT-2 model for text generation
generator = pipeline("text-generation", model="distilgpt2")

# Define selectable options
genres = ["Sci-Fi", "Action", "Romance", "Mystery", "Comedy", "Fantasy", "Horror"]
settings = [
    "a futuristic cyberpunk city", 
    "a medieval kingdom", 
    "a post-apocalyptic wasteland", 
    "a haunted mansion", 
    "a space station on the edge of the galaxy", 
    "an underwater research facility", 
    "a parallel universe"
]
main_characters = [
    "a rogue detective", 
    "a time-traveling scientist", 
    "an undercover spy", 
    "a fearless warrior", 
    "a struggling artist", 
    "an AI gaining consciousness", 
    "a vampire hunter"
]
plot_twists = [
    "the world is a simulation", 
    "the villain is actually the hero", 
    "time starts running backward", 
    "aliens have been controlling everything", 
    "a hidden prophecy is revealed", 
    "the main character is a ghost", 
    "the past can be rewritten"
]
endings = [
    "the hero sacrifices themselves to save the world", 
    "the villain wins in an unexpected twist", 
    "a new adventure begins", 
    "the truth remains unknown", 
    "love conquers all", 
    "the world resets to the beginning", 
    "a shocking betrayal changes everything",
    "a cliffhanger leaves the audience in suspense"
]

# Streamlit UI
st.title("🎬 AI Movie Plot Generator")
st.write("Customize and generate a unique movie plot using AI! 🎥✨")

# User Selects Inputs
genre = st.selectbox("Choose a Genre", genres)
setting = st.selectbox("Choose a Setting", settings)
main_character = st.selectbox("Choose a Main Character", main_characters)
plot_twist = st.selectbox("Choose a Plot Twist", plot_twists)
ending = st.selectbox("Choose an Ending", endings)

# Improved AI Prompt for better plot generation
prompt = (
    f"In a world where {setting}, a {genre.lower()} story unfolds. At its heart is {main_character}, "
    f"who is thrust into an extraordinary situation that changes everything. When a hidden truth emerges—{plot_twist}—"
    f"the journey takes a dangerous turn. As betrayal and revelations shake the foundation of reality, choices must be made. "
    f"Allies and enemies blur, and the fate of everything hangs in the balance. In a final, breathtaking showdown, "
    f"{ending} marks the climax of a story that will never be forgotten. The journey begins when..."
)

# Generate a movie plot when button is clicked
if st.button("Generate Movie Plot"):
    output = generator(prompt, max_length=200, num_return_sequences=1, temperature=0.9, top_p=0.95)
    
    # Extract and format generated text
    generated_text = output[0]['generated_text']
    sentences = sent_tokenize(generated_text)  # Ensure proper sentence splitting
    formatted_plot = " ".join(sentences[:6])  # Take first 6 sentences for depth

    # Generate a dynamic movie title (Ensuring originality)
    title_adjectives = ["Dark", "Eternal", "Lost", "Fateful", "Forbidden", "Shadowed", "Crimson"]
    title_nouns = ["Legacy", "Echoes", "Destiny", "Reckoning", "Awakening", "Cipher", "Prophecy"]
    movie_title = f"{random.choice(title_adjectives)} {random.choice(title_nouns)}"

    # Display results
    st.subheader("🎬 Generated Movie Details")
    st.write(f"**Title:** {movie_title}")
    st.write(f"**Genre:** {genre}")
    st.write(f"**Plot:** {formatted_plot}")
