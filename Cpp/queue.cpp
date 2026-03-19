#include <iostream>

const int MAX_SIZE = 100;

class Queue
{
private:
    int queue_array[MAX_SIZE];
    int front;
    int rear;

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    bool isFull() {
        return rear == MAX_SIZE - 1;
    }

    bool isEmpty() {
        return front == -1 || front > rear;
    }

    void enqueue(int value) {
        if (isFull()) {
            std::cout << "Error: Queue is full. Cannot enqueue." << std::endl;
            return;
        }
        if (front == -1) {
            front = 0;
        }
        rear++;
        queue_array[rear] = value;
        std::cout << value << " has been enqueued." << std::endl;
    }

    void dequeue() {
        if (isEmpty()) {
            std::cout << "Error: Queue is empty. Cannot dequeue." << std::endl;
            return;
        }
        int value = queue_array[front];
        front++;
        if (front > rear) { // Reset queue when it becomes empty
            front = -1;
            rear = -1;
        }
        std::cout << value << " has been dequeued." << std::endl;
    }

    void peek() {
        if (isEmpty()) {
            std::cout << "Error: Queue is empty. Cannot peek." << std::endl;
            return;
        }
        std::cout << "Front element is: " << queue_array[front] << std::endl;
    }
};

int main() {
    Queue queue;
    int choice;
    int value;

    while (true) {
        std::cout << "\n--- Queue Menu ---" << std::endl;
        std::cout << "1. Enqueue (Push)" << std::endl;
        std::cout << "2. Dequeue (Pop)" << std::endl;
        std::cout << "3. Peek" << std::endl;
        std::cout << "4. Exit" << std::endl;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter the value to enqueue: ";
                std::cin >> value;
                queue.enqueue(value);
                break;
            case 2:
                queue.dequeue();
                break;
            case 3:
                queue.peek();
                break;
            case 4:
                std::cout << "Exiting program." << std::endl;
                return 0; // Use return 0 for a clean exit
            default:
                std::cout << "Invalid choice. Please try again." << std::endl;
                // Clear potential error flags from cin
                std::cin.clear();
                // Discard invalid input
                std::cin.ignore(10000, '\n');
                break;
        }
    }

    return 0;
}