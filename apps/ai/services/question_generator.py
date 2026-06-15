def generate_questions(
    topic,
    difficulty,
):

    prompt = f"""
    Generate 20 CBT Questions

    Topic:
    {topic}

    Difficulty:
    {difficulty}
    """

    return prompt
