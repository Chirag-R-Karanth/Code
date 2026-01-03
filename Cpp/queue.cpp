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

void Queue::peek()
{
    cout<<"Enter the Place";
    int Place;
    cin>>Place;
    cout<<"Element at Place "<<Place<<" is "<<queue_array[Place];
}

int main()
{
  Queue queue;
  queue.push();
  queue.peek();
}
