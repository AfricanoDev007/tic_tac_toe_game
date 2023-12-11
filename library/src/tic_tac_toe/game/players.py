import abc
import time
import random

from logic.exceptions import InvalidMove
from models import Mark, GameState, Move

class Player(metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark) -> None:
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It is other player is turn")

    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """ Return the current player's move in the given game state """


class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark, delay_seconds: float = 0.25) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computeer_move(game_state)

    @abstractmethod
    def get_computeer_move(self, game_state: GameState) -> Move | None:
        """Return the computer's move in the given game state. """

class RandomComputerPlayer(ComputerPlayer):
    def get_computeer_move(self, game_state: GameState) -> Move |None:
        try:
            return random.choice(game_state.possible_moves)
        except IndexError:
            return None