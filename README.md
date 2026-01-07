When provided input text data, this script runs an analysis of Chinese characters within the file.

Created to track my language-learning progress. I use it to see how many unique characters I've learned, by uploading my full Anki decks.

To use:
- To extract individual characters from an Anki deck, run anki_deck_extractor.py
- For other texts, run chinese_text_metrics.py

Current features:
- Character extraction and junk removal
- Tracking a count of total unique characters
- Tracking how many times each character was used
- Differentiation between simplified and traditional character sets

Wishlist features:
- Complexity estimation: comparison with the top 1000 most frequently-used Chinese characters

__Sample Metrics Output__
- Input file contained over 13,000 unique words across 21,672 cards
<img width="691" height="333" alt="ChineseMetricsFullScreenshot" src="https://github.com/user-attachments/assets/5ec632ad-8ec9-48fb-b78c-fd02f4eefd28" />
<img width="258" height="498" alt="ChineseMetricsFullOutput" src="https://github.com/user-attachments/assets/868637ac-281c-4e91-8708-bab220b5a198" />
