def render_template(
    template,
    context,
):

    content = template.body

    for key, value in context.items():
        content = content.replace(
            f"{{{{{key}}}}}",
            str(value),
        )

    return content
