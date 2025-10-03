#include "iostream"
using namespace std;

class Queue
{
    private : int front,back,queue_array[100];

    public:
        void push();
        //int peek();
        //int drop();
};

Queue:Queue
{
  front=back=-1;
}

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
  cout<<queue_array[back]
}

int main()
{
  Queue queue;
  queue.push();
}
