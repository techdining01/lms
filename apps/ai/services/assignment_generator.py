def generate_assignment(
    topic,
    level,
):

    prompt = f"""
    Create:

    10 Questions

    Answer Guide

    Marking Scheme

    Topic:
    {topic}

    Level:
    {level}
    """

    return prompt
