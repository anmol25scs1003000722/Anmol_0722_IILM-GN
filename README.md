# AI-Powered Text Summarizer 📝

This Python tool uses the **BART (Bidirectional and Auto-Regressive Transformers)** model to perform abstractive text summarization. It's designed to take long-form articles or scripts and condense them into concise, coherent summaries while maintaining the original context.

## 🚀 Features
* **Abstractive Summarization:** Unlike extractive tools that just copy sentences, this generates new, fluid text using `facebook/bart-large-cnn`.
* **Easy Configuration:** Quickly adjust summary length by changing `MAX_LENGTH` and `MIN_LENGTH` constants.
* **File-Based I/O:** Simple workflow—drop your text in one file, run the script, and get your summary in another.

## 🛠️ Prerequisites
Before running the script, ensure you have Python installed and the necessary libraries:

```bash
pip install transformers torch tensorflow
```

## 📖 How to Use
1.  **Prepare Input:** Create a file named `news.txt` in the same folder as the script.
2.  **Add Content:** Paste the text or article you want to summarize into `news.txt`.
3.  **Run the Script:**
    ```bash
    python summarizer.py
    ```
4.  **Check Results:** Your summary will be automatically generated and saved in `summary.txt`.

## ⚙️ Configuration
You can modify these variables directly in `summarizer.py` to fit your needs:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `INPUT_FILE` | `news.txt` | The source file to be read. |
| `OUTPUT_FILE` | `summary.txt` | The file where the summary is saved. |
| `MAX_LENGTH` | `150` | Maximum token length of the output. |
| `MIN_LENGTH` | `40` | Minimum token length of the output. |
