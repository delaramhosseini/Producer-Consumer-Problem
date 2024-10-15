# Producer-Consumer Problem with a Shared Buffer

## Introduction
This project demonstrates a solution to the classic **Producer-Consumer problem** using a shared buffer, thread synchronization, and semaphores to manage concurrent access to the buffer. In this problem, producers generate data items and place them into a shared buffer, while consumers remove and process these items. The buffer has a limited capacity, and the program ensures that producers wait if the buffer is full, and consumers wait if the buffer is empty.

### Key Features:
- **Multiple Producers and Consumers**: The solution supports multiple producer and consumer threads running concurrently.
- **Thread Synchronization**: Synchronization mechanisms (semaphores or mutexes) are used to ensure no race conditions occur, preventing the buffer from being accessed simultaneously by multiple threads.
- **Termination Criteria**: The program terminates after a total of `K` data items have been produced and consumed.
- **State Printing**: The program outputs the state of each producer and consumer thread as they perform actions (waiting, producing, consuming), along with thread numbering and buffer status.

## Problem Description
- **Producers**: These threads produce items and add them to the shared buffer. If the buffer is full, producers must wait until space becomes available.
- **Consumers**: These threads consume items from the shared buffer. If the buffer is empty, consumers must wait until items are available.
- **Buffer**: The buffer can hold a maximum of `N` items, which producers and consumers access.
- **Thread Numbering**: Each producer and consumer is assigned a unique number, which is printed during state transitions.
- **Termination**: The program terminates when `K` items have been produced and consumed.

## Synchronization and Safety
To ensure proper synchronization and avoid data races, the following synchronization mechanisms are used:
- **Semaphores**: These ensure that no thread accesses the buffer when it's not allowed (full or empty).
- **Mutex**: A mutex is used to protect shared resources, ensuring only one thread accesses the buffer at a time.
- **Condition Variables**: Used to signal threads when they need to wake up (i.e., when the buffer is no longer full or empty).

## Implementation Overview

### Thread Functions:
1. **Producers**:
   - Generate an item and attempt to add it to the buffer.
   - If the buffer is full, they wait until space becomes available.
   - Print their state, including the item produced and the total items produced so far.

2. **Consumers**:
   - Attempt to consume an item from the buffer.
   - If the buffer is empty, they wait until there are items available.
   - Print their state, including the item consumed and the total items consumed so far.

3. **Termination**:
   - The program stops after a total of `K` items have been produced and consumed.

### Example Output:
Below is an example of the output when the program runs with the following parameters:
- **Buffer Size (N)**: 2
- **Total Items (K)**: 5
- **Number of Producers**: 5
- **Number of Consumers**: 2

```bash
Producer 0, produced 56. Total items produced: 1
Producer 1, produced 52. Total items produced: 2
Buffer is full. Producer 2 is waiting...
Buffer is full. Producer 3 is waiting...
Buffer is full. Producer 4 is waiting...
Consumer 0, consumed 56. Total items consumed: 1
Consumer 1, consumed 52. Total items consumed: 2
Producer 3 has waited to push item: 12
Producer 3, produced 12. Total items produced: 3
Producer 0, produced 45. Total items produced: 4
Consumer 0, consumed 12. Total items consumed: 3
Producer 4 has waited to push item: 57
Producer 4, produced 57. Total items produced: 5
Producer 1 is done.
Consumer 1, consumed 45. Total items consumed: 4
Producer 2 is done.
Consumer 0, consumed 57. Total items consumed: 5
Producer 4 is done.
Producer 3 is done.
Producer 0 is done.
Consumer 1 is done.
Consumer 0 is done.
