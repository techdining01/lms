document.addEventListener(
    "visibilitychange",
    () => {

        if (
            document.hidden
        ) {

            fetch(
                "/exams/tab-switch/"
            )

        }

    }
)