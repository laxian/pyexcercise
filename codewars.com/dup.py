w='abcdeaB'

print(sorted(w))
print(list(sorted(w).count(c) for c in sorted(w)))
print(
    len(
        set(
            (
                list(
                    filter(
                        lambda i: i>1,
                        list(
                            sorted(w.upper()).count(c) for c in set(sorted(w.upper()))
                        )
                    )
                )
            )
        )
    )
)

print(
    list(
        filter(
            lambda x: x>1, list(w.upper().count(c) for c in set(sorted(w.upper())))
        )
    )
)