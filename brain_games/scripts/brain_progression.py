from brain_games.engine import game_engine
from brain_games.games.progression import task
from brain_games.games.progression import get_game_data


def main():
    game_engine(get_game_data, task)


if __name__ == '__main__':
    main()
