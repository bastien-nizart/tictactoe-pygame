def switch_player(id_player: int) -> int:
    if id_player == 0:
        return 1
    return 0


def check_line(score) -> tuple:
    for line in score:
        if (line[0] == line[1]) and (line[1] == line[2]) and (line[0] != ''):
            return True, line[0]

    return False, None


def check_col(score) -> tuple:
    for i in range(3):
        if (score[0][i] == score[1][i]) and (score[1][i] == score[2][i]) and (score[0][i] != ''):
            return True, score[0][i]

    return False, None


def check_diagonal(score) -> tuple:
    if (score[0][0] == score[1][1]) and (score[1][1] == score[2][2]) and (score[0][0] != ''):
        return True, score[0][0]

    if (score[0][2] == score[1][1]) and (score[1][1] == score[2][0]) and (score[1][1] != ''):
        return True, score[1][1]

    return False, None


def check(score) -> tuple:
    cond, winner = check_line(score)
    if cond:
        return cond, winner

    cond, winner = check_col(score)
    if cond:
        return cond, winner

    cond, winner = check_diagonal(score)
    if cond:
        return cond, winner

    return False, None


def check_full(score) -> bool:
    for line in score:
        for case in line:
            if case == '':
                return False
    return True
