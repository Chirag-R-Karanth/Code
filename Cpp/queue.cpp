#include "iostream"
using namespace std;

class Queue
{
    private : int front,back,queue_array[100];

    public:
        void push();
        void peek();
        //int drop();
};

void Queue::push()
{
    cout<<"Enter the limit";
    int limit;
    cin>>limit;
    for(int i=0; i<limit; i++)
    {
      cin>>queue_array[i];
    }
}

int main()
{
  Queue queue;
  queue.push();
}
