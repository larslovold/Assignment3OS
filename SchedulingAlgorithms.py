# CPU Scheduling Algorithms: FCFS & Pre-emptive Priority Scheduling

import heapq

def fcfs():
    print("\n=== TEST FCFS Simulation ===")
    process_count = int(input("How many tasks to schedule?"))
    processes = []

      for i in range(process_count):
        task_id = input(f"Enter Task ID for Task {i + 1}: ")
        arrival = int(input("Enter Start Time: "))
        burst = int(input("Enter Duration: "))
        processes.append([task_id, arrival, burst])

    processes.sort(key=lambda x: x[1])
    time_now = 0
    wait_times = []
    turn_times = []
     for process in processes:
        task_id, arrival, burst = process
        if time_now < arrival:
            time_now = arrival
        waiting_time = time_now - arrival
        turnaround_time = waiting_time + burst
        wait_times.append(waiting_time)
        turn_times.append(turnaround_time)
        time_now += burst

    avg_waiting = sum(wait_times) / process_count
    avg_turnaround = sum(turn_times) / process_count

    print("\nFCFS Scheduling Results:")
    print(f"Mean Waiting Time: {avg_waiting:.2f}")
    print(f"Mean Turnaround Time: {avg_turnaround:.2f}")

    def priority_scheduling():
    print("\n=== Dynamic Priority Scheduling Simulation ===")
    process_count = int(input("Number of tasks to handle: "))
    processes = []

    for i in range(process_count):
        task_id = input(f"Enter Task ID for Task {i + 1}: ")
        arrival = int(input("Enter Start Time: "))
        burst = int(input("Enter Duration: "))
        priority = int(input("Enter Priority Level (Lower is better): "))
        processes.append([task_id, arrival, burst, priority])

    processes.sort(key=lambda x: (x[1], x[3]))  

    task_queue = []
    current_time = 0
    wait_times = {}
    turn_times = {}
    remaining_burst = {p[0]: p[2] for p in processes}

    while len(wait_times) < process_count:
        for process in processes:
            task_id, arrival, burst, priority = process
            if arrival <= current_time and task_id not in wait_times:
                heapq.heappush(task_queue, (priority, task_id, arrival, burst))

        if task_queue:
            priority, task_id, arrival, burst = heapq.heappop(task_queue)
            if current_time < arrival:
                current_time = arrival

            if remaining_burst[task_id] > 0:
                execution = min(remaining_burst[task_id], 1)
                remaining_burst[task_id] -= execution
                current_time += execution

                if remaining_burst[task_id] == 0:
                    wait_times[task_id] = current_time - arrival - burst
                    turn_times[task_id] = current_time - arrival
        else:
            current_time += 1

    avg_waiting = sum(wait_times.values()) / process_count
    avg_turnaround = sum(turn_times.values()) / process_count

    print("\nPriority Scheduling Results:")
    print(f"Mean Waiting Time: {avg_waiting:.2f}")
    print(f"Mean Turnaround Time: {avg_turnaround:.2f}")

    def priority_scheduling():
    print("\n=== Dynamic Priority Scheduling Simulation ===")
    process_count = int(input("Number of tasks to handle: "))
    processes = []

    for i in range(process_count):
        task_id = input(f"Enter Task ID for Task {i + 1}: ")
        arrival = int(input("Enter Start Time: "))
        burst = int(input("Enter Duration: "))
        priority = int(input("Enter Priority Level (Lower is better): "))
        processes.append([task_id, arrival, burst, priority])

    processes.sort(key=lambda x: (x[1], x[3]))  

    task_queue = []
    current_time = 0
    wait_times = {}
    turn_times = {}
    remaining_burst = {p[0]: p[2] for p in processes}

    while len(wait_times) < process_count:
        for process in processes:
            task_id, arrival, burst, priority = process
            if arrival <= current_time and task_id not in wait_times:
                heapq.heappush(task_queue, (priority, task_id, arrival, burst))

        if task_queue:
            priority, task_id, arrival, burst = heapq.heappop(task_queue)
            if current_time < arrival:
                current_time = arrival

            if remaining_burst[task_id] > 0
                execution = min(remaining_burst[task_id], 1)
                remaining_burst[task_id] -= execution
                current_time += execution

                if remaining_burst[task_id] == 0:
                    wait_times[task_id] = current_time - arrival - burst
                    turn_times[task_id] = current_time - arrival
        else:
            current_time += 1

    avg_waiting = sum(wait_times.values()) / process_count
    avg_turnaround = sum(turn_times.values()) / process_count

    print("\nPriority Scheduling Results:")
    print(f"Mean Waiting Time: {avg_waiting:.2f}")
    print(f"Mean Turnaround Time: {avg_turnaround:.2f}")

    def menu():
    while True:
        print("\n================================")
        print("  Task Scheduling Simulator  ")
        print("================================")
        print("1. FCFS Task Scheduling")
        print("2. Priority-Based Task Scheduling")
        print("3. Quit")
        print("================================")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            fcfs()
        elif choice == '2'
            priority_scheduling()
        elif choice == '3':
            print("\nThanks for using the Task Scheduler. See you next time!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")


if __name__ == "__main__":
    menu()
