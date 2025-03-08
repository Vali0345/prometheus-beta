from typing import List, Tuple

class ColorStackSorter:
    """
    A class to sort three stacks of colored balls with specific constraints.
    
    Constraints:
    - Only move one ball at a time
    - Maintain equal number of balls in each stack
    - Stacks contain Red, Blue, and Green balls
    """
    
    def __init__(self, red_stack: List[str], blue_stack: List[str], green_stack: List[str]):
        """
        Initialize the color stack sorter with three stacks of balls.
        
        :param red_stack: List of balls in the red stack
        :param blue_stack: List of balls in the blue stack
        :param green_stack: List of balls in the green stack
        """
        # Validate input stacks have equal length
        if not (len(red_stack) == len(blue_stack) == len(green_stack)):
            raise ValueError("All stacks must have equal number of balls")
        
        self.stacks = {
            'red': red_stack,
            'blue': blue_stack,
            'green': green_stack
        }
        self.moves = []
    
    def move_ball(self, source: str, destination: str) -> None:
        """
        Move a single ball from source stack to destination stack.
        
        :param source: Color of source stack
        :param destination: Color of destination stack
        :raises ValueError: If source stack is empty or invalid
        """
        if source not in self.stacks or destination not in self.stacks:
            raise ValueError("Invalid stack color")
        
        if not self.stacks[source]:
            raise ValueError(f"Cannot move ball from empty {source} stack")
        
        # Remove ball from source stack
        ball = self.stacks[source].pop()
        
        # Add ball to destination stack
        self.stacks[destination].append(ball)
        
        # Record the move
        self.moves.append((source, destination))
    
    def is_sorted(self) -> bool:
        """
        Check if the stacks are sorted (all red balls in red stack,
        blue balls in blue stack, green balls in green stack).
        
        :return: True if sorted, False otherwise
        """
        return (
            all(ball == 'red' for ball in self.stacks['red']) and
            all(ball == 'blue' for ball in self.stacks['blue']) and
            all(ball == 'green' for ball in self.stacks['green'])
        )
    
    def sort_stacks(self) -> List[Tuple[str, str]]:
        """
        Sort the stacks by moving balls between stacks.
        
        :return: List of moves made to sort the stacks
        """
        # Reset moves
        self.moves = []
        
        # If already sorted, return empty moves list
        if self.is_sorted():
            return self.moves
        
        # Sorting strategy:
        # 1. Identify the current state
        # 2. Move balls to their correct stacks
        
        # Continue moving balls until sorted
        while not self.is_sorted():
            # Check each stack
            for source in ['red', 'blue', 'green']:
                for destination in ['red', 'blue', 'green']:
                    if source != destination and self.stacks[source]:
                        # If source ball doesn't match source stack, move it
                        current_ball = self.stacks[source][-1]
                        if current_ball != source:
                            self.move_ball(source, destination)
                            break
        
        return self.moves