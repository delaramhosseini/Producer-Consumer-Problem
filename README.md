can you add a summary about shared buﬀer?
# Producer-Consumer Problem with a Shared Buffer

## Introduction
This project demonstrates a solution to the classic **Producer-Consumer problem** using a shared buffer, thread synchronization, and semaphores to manage concurrent access to the buffer. In this problem, producers generate data items and place them into a shared buffer, while consumers remove and process these items. The buffer has a limited capacity, and the program ensures that producers wait if the buffer is full, and consumers wait if the buffer is empty.

### Shared Buffer
A shared buffer is a common data structure used in concurrent programming, particularly in problems like the Producer-Consumer problem. It serves as a temporary storage area where multiple threads or processes can access and exchange data safely and efficiently. Here’s an overview of its key characteristics and functionalities:

#### Key Characteristics of a Shared Buffer:
1. **Limited Capacity:**
   - The shared buffer typically has a fixed size or capacity, which limits the number of items it can hold at any given time. This constraint is essential to prevent overflows or underflows and to manage the flow of data between producers and consumers.
2. **Concurrent Access:**
   - Multiple producers (which generate data) and consumers (which use the data) can access the buffer concurrently. The design ensures that they can operate simultaneously without interfering with each other, thus maximizing efficiency.
3. **Blocking Behavior:**
   - The buffer operates on a blocking principle:
        - Producers block when the buffer is full, meaning they cannot add more items until space is available.
        - Consumers block when the buffer is empty, meaning they cannot remove items until there are items present.
4. **Synchronization Mechanisms:**
   - To ensure safe access to the buffer and to prevent race conditions (where multiple threads attempt to read/write simultaneously), synchronization mechanisms are employed, such as:
        - Mutexes: These allow only one thread to access the buffer at a time.
        - Semaphores: These signal when it is safe to access the buffer, controlling the number of threads that can access it simultaneously.
5. **Data Consistency:**
   - The shared buffer maintains data integrity and consistency by ensuring that data produced by one thread can be reliably consumed by another, without data loss or corruption.

## Program Functionality

### Key Features:
- **Multiple Producers and Consumers**: The solution supports multiple producer and consumer threads running concurrently.
- **Thread Synchronization**: Synchronization mechanisms (semaphores or mutexes) are used to ensure no race conditions occur, preventing the buffer from being accessed simultaneously by multiple threads.
- **Termination Criteria**: The program terminates after a total of K data items have been produced and consumed.
- **State Printing**: The program outputs the state of each producer and consumer thread as they perform actions (waiting, producing, consuming), along with thread numbering and buffer status.

### Problem Description
- **Producers**: These threads produce items and add them to the shared buffer. If the buffer is full, producers must wait until space becomes available.
- **Consumers**: These threads consume items from the shared buffer. If the buffer is empty, consumers must wait until items are available.
- **Buffer**: The buffer can hold a maximum of N items, which producers and consumers access.
- **Thread Numbering**: Each producer and consumer is assigned a unique number, which is printed during state transitions.
- **Termination**: The program terminates when K items have been produced and consumed.

### Synchronization and Safety
To ensure proper synchronization and avoid data races, the following synchronization mechanisms are used:
- **Semaphores**: These ensure that no thread accesses the buffer when it's not allowed (full or empty).
- **Mutex**: A mutex is used to protect shared resources, ensuring only one thread accesses the buffer at a time.
- **Condition Variables**: Used to signal threads when they need to wake up (i.e., when the buffer is no longer full or empty).

### Implementation Overview

#### Thread Functions:
1. **Producers**:
   - Generate an item and attempt to add it to the buffer.
   - If the buffer is full, they wait until space becomes available.
   - Print their state, including the item produced and the total items produced so far.

2. **Consumers**:
   - Attempt to consume an item from the buffer.
   - If the buffer is empty, they wait until there are items available.
   - Print their state, including the item consumed and the total items consumed so far.

3. **Termination**:
   - The program stops after a total of K items have been produced and consumed.

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
