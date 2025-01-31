class Environment:
    def __init__(self):
        # Create a 3x3 grid, where some positions are dirty
        self.grid = [
            'Safe', 'Vulnerable', 'Vulnerable',
            'Safe', 'Vulnerable', 'Safe','Vulnerable','Vulnerable','Safe'
        ]

    def get_percept(self, position):
        # Return the state of the current position
        return self.grid[position]

    def Scan(self, position):
        # Complete the task at the given position
        self.grid[position] = 'Patching'
       
     
    def display_grid(self, agent_position):
        # Display the current state of the grid in a 3x3 format
        print("\nCurrent Grid State:")
        grid_with_agent = self.grid[:]  # Copy the grid
        grid_with_agent[agent_position] = " 👽"  # Place the agent
        for i in range(0, 9, 3):
            print(" | ".join(grid_with_agent[i:i + 3]))
        print()  # Extra line for spacing


class SimpleReflexAgent:
    def __init__(self):
        self.position = 0  # Start at position 0

    def act(self, percept, grid):
        # If the current position is dirty, clean it
        if percept == 'Safe':
            
            return 'The Component is Safe'
        else:
            
        

            return 'The Component is NOT Safe..Going for Patching'
        

         
        
    
                 

    def move(self):
        # Move to the next position in the grid
        if self.position < 8:
            self.position += 1
   

def run_agent(agent, environment, steps):
    for step in range(steps):
         
        percept = environment.get_percept(agent.position)
        action = agent.act(percept, environment.grid)

        print(f"Step {step+1}: Position {agent.position} -> Percept: {percept}, Action: {action}")
        environment.display_grid(agent.position)  # Display the grid state

        if percept == 'Vulnerable':
            environment.Scan(agent.position)
      


        agent.move()


# Create instances of agent and environment
agent = SimpleReflexAgent()
environment = Environment()

# Run the agent in the environment for 9 steps (to cover the 3x3 grid)
run_agent(agent, environment, 9)
