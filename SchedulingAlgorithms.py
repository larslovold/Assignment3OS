import heapq

def save_results(filename, results):
    """
    Save results to a text file.
    """
    with open(filename, 'w') as file:
        file.write(results)
    print(f"\nResults have been saved to {filename}.")

def get_positive_integer(prompt):
    """
    Helper function to get a valid positive integer from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def get_filename():
    """
    Prompt the user to enter a filename or use the default.
    """
    filename = input("Enter filename to save the results (Leave blank for default): ").strip()
    return filename if filename else "Results.txt"

def fcfs():
    try:
        print("\n=== Simple FCFS Simulation ===")
        process_count = get_positive_integer("How many tasks to schedule? ")
        processes = []
        task_ids = set()

        for i in range(process_count):
            while True:
                task_id = input(f"Enter Task ID for Task {i + 1}: ")
                if task_id in task_ids:
                    print("Task ID already exists! Please enter a unique Task ID.")
                else:
                    task_ids.add(task_id)
                    break
            arrival = get_positive_integer("Enter Start Time: ")
            burst = get_positive_integer("Enter Duration: ")
            processes.append([task_id, arrival, burst])

        processes.sort(key=lambda x: x[1])
        time_now = 0
        wait_times = []
        turn_times = []
        results = "Task ID\tWaiting Time\tTurnaround Time\n"

        for process in processes:
            task_id, arrival, burst = process
            if time_now < arrival:
                time_now = arrival
            waiting_time = time_now - arrival
            turnaround_time = waiting_time + burst
            wait_times.append(waiting_time)
            turn_times.append(turnaround_time)
            time_now += burst
            results += f"{task_id}\t{waiting_time}\t{turnaround_time}\n"

        avg_waiting = sum(wait_times) / process_count
        avg_turnaround = sum(turn_times) / process_count

        results += f"\nMean Waiting Time: {avg_waiting:.2f}\nMean Turnaround Time: {avg_turnaround:.2f}\n"
        print(results)

        if input("Do you want to save the results to a file? (y/n): ").lower() == 'y':
            filename = get_filename()
            save_results(filename, results)

    except ValueError:
        print("\nInvalid input! Please enter numbers only where required.\n")

def priority_scheduling():
    try:
        print("\n=== Dynamic Priority Scheduling Simulation ===")
        process_count = get_positive_integer("Number of tasks to handle: ")
        processes = []
        task_ids = set()

        for i in range(process_count):
            while True:
                task_id = input(f"Enter Task ID for Task {i + 1}: ")
                if task_id in task_ids:
                    print("Task ID already exists! Please enter a unique Task ID.")
                else:
                    task_ids.add(task_id)
                    break
            arrival = get_positive_integer("Enter Start Time: ")
            burst = get_positive_integer("Enter Duration: ")
            priority = get_positive_integer("Enter Priority Level (Lower is better): ")
            processes.append([task_id, arrival, burst, priority])

        processes.sort(key=lambda x: (x[1], x[3]))  

        task_queue = []
        current_time = 0
        wait_times = {}
        turn_times = {}
        remaining_burst = {p[0]: p[2] for p in processes}
        results = "Task ID\tWaiting Time\tTurnaround Time\n"

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
                        results += f"{task_id}\t{wait_times[task_id]}\t{turn_times[task_id]}\n"
            else:
                current_time += 1

        avg_waiting = sum(wait_times.values()) / process_count
        avg_turnaround = sum(turn_times.values()) / process_count

        results += f"\nMean Waiting Time: {avg_waiting:.2f}\nMean Turnaround Time: {avg_turnaround:.2f}\n"
        print(results)

        if input("Do you want to save the results to a file? (y/n): ").lower() == 'y':
            filename = get_filename()
            save_results(filename, results)

    except ValueError:
        print("\nInvalid input! Please enter numbers only where required.\n")

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
        elif choice == '2':
            priority_scheduling()
        elif choice == '3':
            print("\nThanks for using the Task Scheduler. See you next time!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")


if __name__ == "__main__":
    menu()