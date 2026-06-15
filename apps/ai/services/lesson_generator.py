def generate_lesson(
    topic,
    level,
):

    prompt = f"""
    Generate:

    Objectives

    Lesson Note

    Examples

    Exercises

    Homework

    Topic:
    {topic}

    Level:
    {level}
    """

    return prompt
