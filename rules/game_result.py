def declarer_won(state):

    return (
        state.scores[
            state.declarer
        ]
        >=
        61
    )