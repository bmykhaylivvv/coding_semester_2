'''Implementation of the main simulation class'''

import random
from arrays import Array
from linkedqueue import Queue  # add/pop
from simpeople import TicketAgent, Passenger


class TicketCounterSimulation:
    '''Create a simulation object.'''

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0
        self._passengersTime = []
        self._currentTimes = []
        self.time_while_wait = [] # times when passengers arrived


    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)
            
    @staticmethod
    def find_waiting_time(times):
        '''
        Find total waiting time.
        '''
        reversed_times = times[::-1]
        total_waiting_time = 0
        for ind in range(len(times[::-1])-1):
            total_waiting_time += (reversed_times[ind] - reversed_times[ind+1]) 
        return total_waiting_time

    # Print the simulation results.
    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        total_waiting_time = self.find_waiting_time(self.time_while_wait)
        avgWait = total_waiting_time / numServed
        
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" %
              len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)
        
        # FOR DEBUG
        # print(f'All passenge r times: {self._passengersTime}')
        # print(f'Current TIMES {self._currentTimes}')

    def _handleArrival(self, curTime):
        '''
        Simulates arrival and creates passenger when condition executes.
        '''
        odd = random.random() 
        if odd <= self._arriveProb:
            self._numPassengers += 1

            #create an instance of passenger
            passenger = Passenger(self._numPassengers, curTime)
            self._passengerQ.add(passenger)
            # self._passengersTime.append(passenger.timeArrived()) # FOR DEBUG
            print(f'Time\t{curTime}: Passenger {passenger.idNum()} arrived')


    def _handleBeginService(self, curTime):
        '''
        Finds free agent and assigns passenger to agent. (Service begins.)
        '''
        for agent_num, agent in enumerate(self._theAgents):
            if agent.isFree() and not self._passengerQ.isEmpty():
                passenger = self._passengerQ.pop()
                self.time_while_wait.append(passenger.timeArrived())
                # self._currentTimes.append(curTime) # FOR DEBUG
                print(f'Time\t{curTime}: Agent {agent.idNum()} started serving passenger {passenger.idNum()}')

    def _handleEndService(self, curTime):
        '''
        Finishes service and set agent`s passenger to None.
        '''
        for agent_num, agent in enumerate(self._theAgents):
            if agent.isFinished(curTime):
                passenger = agent.stopService()
                print(f'Time\t{curTime}: Agent {agent.idNum()} stopped serving passenger {passenger.idNum()}')

if __name__ == "__main__":
    # random.seed(4500) # seed from the book
    TCSimulation = TicketCounterSimulation(2, 25, 2, 3)
    TCSimulation.run()
    TCSimulation.printResults()
