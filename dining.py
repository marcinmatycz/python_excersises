import threading
import time



# function with a problem
def eating(forks, phil_number, phil_name):
    print(phil_name, "is going to eat")

    forks[(phil_number - 1) % len(forks)].acquire()
    print(phil_name, "took first fork")

    time.sleep(0.5)
    forks[phil_number % len(forks)].acquire()
    print(phil_name, "took second fork and is eating")

    time.sleep(1)
    forks[(phil_number - 1) % len(forks)].release()
    time.sleep(0.5)
    forks[phil_number % len(forks)].release()

    print(phil_name, "have finished his dinner")

# function with a solution
def eatingWithWaiter(forks, phil_number, phil_name, permissions):
    print(phil_name, "is going to eat and asks waiter if he can take forks")

    while(True):
        if not permissions[(phil_number - 1) % len(forks)].locked() and not permissions[(phil_number + 1) % len(forks)].locked():
            permissions[(phil_number - 1) % len(forks)].acquire()
            permissions[(phil_number + 1) % len(forks)].acquire()
            break
        time.sleep(0.5)

    print("Waiter granted permission to", phil_name)

    forks[(phil_number - 1) % len(forks)].acquire()
    print(phil_name, "took first fork")

    time.sleep(0.5)
    forks[phil_number % len(forks)].acquire()
    print(phil_name, "took second fork and is eating")

    time.sleep(1)
    forks[(phil_number - 1) % len(forks)].release()
    time.sleep(0.5)
    forks[phil_number % len(forks)].release()

    print(phil_name, "have finished his dinner")
    permissions[(phil_number - 1) % len(forks)].release()
    permissions[(phil_number + 1) % len(forks)].release()


philosophers = ['Artur Schopenhauer', 'John Locke', 'David Hume', 'Sun Tsu', 'Jean-Jacques Rousseau']

forks = []
for i in range(len(philosophers)):
    forks.append(threading.Lock())

permissions = []
for i in range(len(philosophers)):
    permissions.append(threading.Lock())

t = []

for i in range(len(philosophers)):
    #t.append(threading.Thread(target = eating, args=(forks, i, philosophers[i])))
    t.append(threading.Thread(target = eatingWithWaiter, args=(forks, i, philosophers[i], permissions)))
    t[i].start()

for thread in t:
    thread.join()