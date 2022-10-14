def game_once(player, computer):
    if player == computer:
        return 'tie'
    else:
        if judge(player,computer):
            return 'player'
        else:
            return 'computer'

def judge(player,computer):
    if player=='rock':
        if computer=='scissors':
            return True
        if computer=='paper':
            return False
    elif player=='scissors':
        if computer=='paper':
            return True
        if computer=='rock':
            return False
    elif player=='paper':
        if computer=='rock':
            return True
        if computer=='scissors':
            return False

def is_end(player_score, computer_score):
    """
        return : if game is over(bool), winner (string)
    """
    if player_score >= 5:
        return True, "player"
    elif computer_score >= 5:
        return True, "computer"
    else:
        return False, None