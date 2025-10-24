import random


def mock_ai_validation(sentence: str, target_word: str, difficulty: str) -> dict:
    """
    Mock AI validation - simulates scoring and feedback
    In production, this would connect to n8n/OpenAI
    """
    sentence_lower = sentence.lower()
    target_word_lower = target_word.lower()
    
    # Check if word is in sentence
    has_word = target_word_lower in sentence_lower
    
    # Calculate simple score
    word_count = len(sentence.split())
    
    if not has_word:
        return {
            "score": 0.0,
            "level": difficulty,
            "suggestion": f"Your sentence must include the word '{target_word}'. Please try again!",
            "corrected_sentence": f"Remember to use '{target_word}' in your sentence."
        }
    
    # Score based on length and complexity
    if word_count < 5:
        score = random.uniform(4.0, 6.0)
        suggestion = "Try to make your sentence longer and more descriptive."
    elif word_count < 10:
        score = random.uniform(6.5, 8.5)
        suggestion = "Good sentence! Consider adding more details or complex structures."
    else:
        score = random.uniform(8.0, 10.0)
        suggestion = "Excellent! Your sentence is well-structured and descriptive."
    
    # Adjust score based on difficulty
    if difficulty == 'Advanced' and word_count > 8:
        score = min(10.0, score + 0.5)
    
    return {
        "score": round(score, 1),
        "level": difficulty,
        "suggestion": suggestion,
        "corrected_sentence": sentence  # In production, AI would correct this
    }