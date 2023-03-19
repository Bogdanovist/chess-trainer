import chess

USER = 'bogdanovist'

def make_state_key(fen):
    return ' '.join(fen.split(' ')[:-2])

def parse_games(games, play_as):
    move_tree = dict()
    for game in games:
        if game['players'][play_as]['user']['name'] == USER:
            parse_game(move_tree,game)
    
    return move_tree


def parse_game(move_tree, game):

    board = chess.Board()
    last_state = make_state_key(board.fen())
    
    if last_state in move_tree:
        move_tree[last_state]['cnt'] += 1
    else:
        move_tree[last_state] = {'cnt':1, 'children':{}}
        
    for move in game['moves'].split(' '):
        board.push_san(move)
        board_state = make_state_key(board.fen())

        if board_state in move_tree:
            move_tree[board_state]['cnt'] += 1
        else:
            move_tree[board_state] = {'cnt':1, 'children':{}}
        
        if last_state:
            if move in move_tree[last_state]['children']:
                move_tree[last_state]['children'][move] += 1
            else:
                move_tree[last_state]['children'][move] = 1
            
        last_state = board_state