class Environment:
    def __init__(self):
        # Create a 3x3 grid, where some positions are dirty
        self.grid = [
            'UnderLoaded', 'OverLoaded', 'Balanced',
            'OverLoaded', 'Balanced', 
        ]

    def get_percept(self, position):
        # Return the state of the current position
        return self.grid[position]

    def overloaded(self, position):
        # Clean the room at the given position
        self.grid[position] = 'UnderLoaded'
    def underloaded(self, position):
        # Clean the room at the given position
        self.grid[position] = 'Balanced'
    def balance(self, position):
        # Clean the room at the given position
        self.grid[position] = 'Balanced'    
     
    def display_grid(self, agent_position):
        # Display the current state of the grid in a 3x3 format
        print("\nCurrent Grid State:")
        grid_with_agent = self.grid[:]  # Copy the grid
        grid_with_agent[agent_position] = " 👽"  # Place the agent
        for i in range(0, 5, 3):
            print(" | ".join(grid_with_agent[i:i + 3]))
        print()  # Extra line for spacing


class SimpleReflexAgent:
    def __init__(self):
        self.position = 0  # Start at position 0

    def act(self, percept, grid):
        # If the current position is dirty, clean it
        if percept == 'OverLoaded':
            grid[self.position] = 'UnderLoaded'
            return 'load is moved to underloaded'
        elif percept == 'UnderLoaded':
            grid[self.position] = 'Balanced'
            return 'load is moved to Balanced'
        
        else:
            return 'Load is Balance'          

    def move(self):
        # Move to the next position in the grid
        if self.position < 4:
            self.position += 1
   

def run_agent(agent, environment, steps):
    for step in range(steps):
         
        percept = environment.get_percept(agent.position)
        action = agent.act(percept, environment.grid)

        print(f"Step {step+1}: Position {agent.position} -> Percept: {percept}, Action: {action}")
        environment.display_grid(agent.position)  # Display the grid state

        if percept == 'OverLoaded':
            environment.overloaded(agent.position)
        elif percept == 'UnderLoaded':
            environment.underloaded(agent.position)
        else:
            environment.balance(agent.position)


        agent.move()


# Create instances of agent and environment
agent = SimpleReflexAgent()
environment = Environment()

# Run the agent in the environment for 9 steps (to cover the 3x3 grid)
run_agent(agent, environment, 5)
