#include <iostream>
using namespace std;

class stack {
    private:
        int stack_array[1000], limit, top;
    public:
        stack(int l) { limit = l; top = -1; }
        void push(int value) {
            if (top >= limit - 1) {
                cout << "Overflow\n";
            } else {
                stack_array[++top] = value;
            }
        }
        void pop() {
            if (top < 0) {
                cout << "Underflow\n";
            } else {
                cout << "Popped: " << stack_array[top--] << endl;
            }
        }
        void peek() {
            if (top < 0) {
                cout << "Stack is empty\n";
            } else {
                cout << "Top: " << stack_array[top] << endl;
            }
        }
};

int main() {
    int lim;
    cout << "Enter stack size: ";
    cin >> lim;
    stack s(lim);

    int choice, value;
    while (true) {
        cout << "Menu: 1.Push 2.Pop 3.Peek 4.Exit\n";
        cin >> choice;
        switch (choice) {
            case 1:
                cout << "Enter value: ";
                cin >> value;
                s.push(value);
                break;
            case 2:
                s.pop();
                break;
            case 3:
                s.peek();
                break;
            case 4:
                return 0;
        }
    }
}
