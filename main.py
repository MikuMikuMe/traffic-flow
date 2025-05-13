Creating a traffic light optimization system using real-time data and predictive analytics is a complex task, often involving advanced algorithms and a deep understanding of transportation systems. However, I can help you create a simplified version in Python, which simulates the optimization process. This example will focus on the structure and components you would need, along with some basic functionality. For a real-world implementation, you would need additional libraries and real-time data sources.

Here is a basic outline of the program:

```python
import random
import time

class TrafficLight:
    def __init__(self, id):
        self.id = id
        self.green_duration = 30  # seconds
        self.red_duration = 30    # seconds
        self.state = 'RED'        # Initial state
    
    def switch(self):
        # Switches the state of the traffic light
        self.state = 'GREEN' if self.state == 'RED' else 'RED'

    def get_current_duration(self):
        # Returns the duration for the current state
        return self.green_duration if self.state == 'GREEN' else self.red_duration

class TrafficFlowOptimizer:
    def __init__(self):
        self.traffic_lights = []
        self.traffic_data = {}  # Dictionary to hold traffic data

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    def receive_real_time_data(self):
        # Simulates receiving traffic data periodically
        for traffic_light in self.traffic_lights:
            # Simulating the number of cars at each traffic light
            self.traffic_data[traffic_light.id] = random.randint(0, 100)

    def optimize_traffic_lights(self):
        # Simplified optimization that adjusts green light duration based on traffic data
        for traffic_light in self.traffic_lights:
            try:
                cars_waiting = self.traffic_data[traffic_light.id]
                # If more cars are waiting, increase green light duration
                if cars_waiting > 50:
                    traffic_light.green_duration = 45
                else:
                    traffic_light.green_duration = 30
            except KeyError as e:
                print(f"Error: Traffic data for light {traffic_light.id} is unavailable. {e}")
            except Exception as e:
                print(f"Unexpected error occurred while optimizing light {traffic_light.id}: {e}")

    def run_simulation(self, cycles=5):
        for _ in range(cycles):
            self.receive_real_time_data()
            self.optimize_traffic_lights()
            for traffic_light in self.traffic_lights:
                print(f"Traffic Light {traffic_light.id} is {traffic_light.state} for {traffic_light.get_current_duration()} seconds.")
                time.sleep(traffic_light.get_current_duration())  # Simulate time passing
                traffic_light.switch()  # Change the light state

# Main execution block
if __name__ == '__main__':
    optimizer = TrafficFlowOptimizer()
    
    # Creating and adding traffic lights to the optimizer
    for i in range(4):  # Simulating 4 intersections
        tl = TrafficLight(id=i + 1)
        optimizer.add_traffic_light(tl)
    
    optimizer.run_simulation()
```

### Key Components of the Program:
1. **TrafficLight Class**: Represents a traffic light with a `green_duration` and a `red_duration`. The `switch` method toggles between green and red states.
2. **TrafficFlowOptimizer Class**: Manages multiple traffic lights and contains logic to simulate real-time traffic data and optimize traffic lights based on that data.
3. **Optimization Logic**: Adjusts the duration of the green light based on simulated traffic data.
4. **Error Handling**: Handles missing data for traffic lights, and logs unexpected errors during optimization.

### Important Considerations:
- **Real-time Data**: In a real-world scenario, you would replace random traffic data with real-time data from sensors or cameras.
- **Algorithm Complexity**: More sophisticated algorithms, such as those based on machine learning or traffic engineering principles, can be implemented for better optimization.
- **Integration with Traffic Systems**: The program would need to interface with actual traffic lights, likely requiring more complex software and communication protocols.

This example provides a basic framework and demonstrates how you can further extend it with real-time data handling, complex optimization algorithms, and integration with physical traffic systems.