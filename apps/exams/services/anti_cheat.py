def register_tab_switch(
    attempt,
):

    attempt.tab_switch_count += 1

    attempt.save(update_fields=["tab_switch_count"])
