'''Imitation of a day in the life using the state machine pattern.'''

import random

class State:
    '''State class for the state machine pattern.'''
    def __init__(self, name):
        '''Initializes the state with a name.'''
        self.name = name

    def entry(self):
        '''Prints the entry message for the state.'''
        print(f'Entering state: {self.name}')

    def execute(self):
        '''Executes the state's behaviour.'''
        pass

    def exit(self):
        '''Prints the exit message for the state.'''
        print(f'Exiting state: {self.name}')

    def __eq__(self, other):
        '''Compares two states based on their names.'''
        if not isinstance(other, State):
            return False
        return self.name == other.name

class Sleep(State):
    '''Sleep state class.'''
    def __init__(self):
        '''Initializes the sleep state.'''
        super().__init__('Sleep')

    def execute(self):
        '''Executes the sleep state.'''
        print('Sleeping...')

class Eat(State):
    '''Eat state class.'''
    def __init__(self):
        '''Initializes the eat state.'''
        super().__init__('Eat')

    def execute(self):
        '''Executes the eat state.'''
        print('Eating...')

class Work(State):
    '''Work state class.'''
    def __init__(self):
        '''Initializes the work state.'''
        super().__init__('Work')

    def execute(self):
        '''Executes the work state.'''
        print('Working...')

class Gym(State):
    '''Preparing for sleep state class.'''
    def __init__(self):
        '''Initializes the preparing for sleep state.'''
        super().__init__('Gym')

    def execute(self):
        '''Executes the preparing for sleep state.'''
        print('Going to the gym...')

class Rest(State):
    '''Rest state class.'''
    def __init__(self):
        '''Initializes the rest state.'''
        super().__init__('Rest')

    def execute(self):
        '''Executes the rest state.'''
        print('Having rest...')

class Day:
    '''Day class simulation.'''
    def __init__(self):
        self.hours = 0
        self.prev_state = None
        self.events = ['a small deseaese', 'an invitation for coffee', 'an unexpected work meeting']

    def check_random_event(self):
        '''Checks if a random event occurs.'''
        return random.random() <= 0.2

    def random_event(self, event):
        '''Simulates a random event.'''
        if event == 'a small deseaese':
            if self.prev_state == Sleep():
                print('Stay in bed! You are sick! :(')
            else:
                print('You have a small disease. :( You should sleep a bit today!')
            return Sleep()

        if event == 'an invitation for coffee':
            if self.prev_state == Rest():
                print('You are already resting, but you should go have coffee with your friend! :)')
            else:
                print('You have an invitation for coffee. You should go rest with your friend :)')
            return Rest()

        if event == 'an unexpected work meeting':
            if self.prev_state == Work():
                print('You are already working, but you should go to the meeting!')
            else:
                print('You have an unexpected work meeting. You should go to work now. ^_^')
            return Work()

    def get_state(self):
        '''Returns the state based on the hour.'''
        if self.hours < 8 or self.hours >= 23:
            return Sleep()
        if self.hours in (8, 14, 20):
            return Eat()
        if 9 <= self.hours < 14 or 15 <= self.hours < 18:
            return Work()
        if 18 <= self.hours < 20:
            return Gym()
        return Rest()

    def simulate_hour(self):
        '''Simulates an hour in the day.'''
        print(f'Hour: {self.hours}.00')
        if self.check_random_event():
            event = random.choice(self.events)
            state = self.random_event(event)
        else:
            state = self.get_state()

        if state != self.prev_state:
            if self.prev_state is not None:
                self.prev_state.exit()
            state.entry()
            state.execute()
            self.prev_state = state

        self.hours += 1

    def simulate_day(self):
        '''Simulates a day.'''
        while self.hours < 24:
            self.simulate_hour()
        print('The day is over!')

if __name__ == "__main__":
    day = Day()
    day.simulate_day()
