from threading import Semaphore


class DiningPhilosophers:
    def __init__(self):
        self.semlock = Semaphore(4)
        self.locks = [Semaphore(1) for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left, right = philosopher, (philosopher-1)%5
        with self.semlock:
            with self.locks[left], self.locks[right]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
