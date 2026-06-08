from rules.scoring import CARD_POINTS


def get_skat_points(state):

    total = 0

    for card in state.skat:

        total += CARD_POINTS[
            card.rank
        ]

    return total


def get_declarer_points(state):

    return (
        state.scores[
            state.declarer
        ]
        +
        get_skat_points(
            state
        )
    )


def get_defender_points(state):

    total = 0

    for player in range(3):

        if player != state.declarer:

            total += (
                state.scores[player]
            )

    return total


def get_declarer_margin(state):

    return (
        get_declarer_points(
            state
        )
        -
        61
    )


def declarer_won(state):

    return (
        get_declarer_points(
            state
        )
        >=
        61
    )


def defenders_won(state):

    return (
        get_defender_points(
            state
        )
        >=
        60
    )