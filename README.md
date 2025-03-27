
## Project Overview
This project implements two CPU Scheduling Algorithms:
1. **First Come First Serve (FCFS)** - A non-preemptive scheduling algorithm where tasks are executed in the order of their arrival.
2. **Preemptive Priority Scheduling** - A preemptive scheduling algorithm where tasks with higher priority are executed first. If a new task arrives with a higher priority, it interrupts the currently running task.

The program provides results including:
- Individual Waiting Time and Turnaround Time for each task.
- Average Waiting Time.
- Average Turnaround Time.
- Option to save results to a file with a custom filename.

---

## File Structure
```
- main.py (Main entry point of the program)
- fcfs.py (Implementation of FCFS Scheduling)
- priority_scheduling.py (Implementation of Priority Scheduling)
- utils.py (Utility functions for input handling and saving results)
```

---

## eatures
- Enhanced Input Validation: Ensures only valid integers are accepted for numeric inputs.
- Duplicate Task ID Prevention: Ensures Task IDs are unique to avoid conflicts.
- Custom File Naming: Users can choose filenames for saving results.
- Clear, Menu-driven Interface: Easy selection between scheduling algorithms.
- Robust Error Handling: Prevents the program from crashing due to incorrect inputs.

---

## How to Run the Program
1. Make sure all files are in the **same folder**.
2. Run the program by typing:
```bash
python main.py
```
or
```bash
py main.py
```

---

## Usage
### FCFS Scheduling
1. Select **FCFS Task Scheduling** from the menu.
2. Enter the number of tasks.
3. Provide Task ID, Start Time, and Duration for each task.
4. View the results and save them if desired.

### Preemptive Priority Scheduling
1. Select **Priority-Based Task Scheduling** from the menu.
2. Enter the number of tasks.
3. Provide Task ID, Start Time, Duration, and Priority for each task.
4. View the results and save them if desired.

---

## Example Output
```
Task ID    Waiting Time    Turnaround Time
A          0               5
B          3               6
C          6               8

Mean Waiting Time: 3.00
Mean Turnaround Time: 6.33
```

---

## Future Improvements
- Adding more scheduling algorithms (Round-Robin, SJF, etc.)
- Implementing graphical representations (Gantt charts).
- Improving the interface to allow batch processing of tasks from files.
