def match_keywords(prompt: str, resume_text: str) -> str:
    keywords = [word.strip().lower() for word in prompt.split()]
    resume_words = resume_text.lower()

    matched = [kw for kw in keywords if kw in resume_words]
    unmatched = [kw for kw in keywords if kw not in resume_words]

    result = f"✅ Matched keywords: {', '.join(matched)}\n"
    result += f"❌ Missing keywords: {', '.join(unmatched)}"

    return result
