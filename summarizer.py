from transformers import pipeline

# --- Configuration ---
INPUT_FILE = "news.txt"  
OUTPUT_FILE = "summary.txt"
MAX_LENGTH = 150  # You can adjust this for shorter/longer summaries
MIN_LENGTH = 40   # Minimum length of the summary

def run_summarization():
    """Reads input, summarizes it using BART, and saves the output."""
    
    # 1. Read the article from the input file
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            article = f.read()
        if not article.strip():
             print(f"ERROR: Input file '{INPUT_FILE}' is empty. Please add text.")
             return
        print(f"Successfully loaded essay from {INPUT_FILE}.")
        
    except FileNotFoundError:
        print(f"ERROR: The file '{INPUT_FILE}' was not found. Make sure it exists.")
        return
    
    # 2. Load the summarization model
    # Uses 'facebook/bart-large-cnn', which is excellent for abstractive summarization
    print("Loading AI model (BART)...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # 3. Generate the summary
    print(f"Generating summary (Max Length: {MAX_LENGTH}, Min Length: {MIN_LENGTH})...")
    summary_result = summarizer(
        article, 
        max_length=MAX_LENGTH, 
        min_length=MIN_LENGTH, 
        do_sample=False
    )
    summary_text = summary_result[0]["summary_text"]

    # 4. Save the summary to the output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print(f"\n--- SUCCESS! Summary saved to '{OUTPUT_FILE}' ---")
    print(f"Output character count: {len(summary_text)}")

if __name__ == "__main__":
    run_summarization()