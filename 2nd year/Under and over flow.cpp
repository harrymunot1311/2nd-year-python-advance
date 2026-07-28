#include <iostream>
using namespace std;

#define MAX 6
  
class Queue {
    private:
    int arr[MAX];
    int front, rear;

    public:
    Queue(){
        front = -1;
        rear = -1;
    }
    // Enqueue Operation
    void enqueue(int value){
        if (rear == MAX - 1){
            cout << "Queue Overflow! Cannot insert " << value << endl;
            return;
        }
        if (front == -1)
            front = 0;

        rear++;
        arr[rear] = value;
        cout << value << "Inserted into the queue" << endl;    
    }

    //Dequeue Operation
    void dequeue(){
        if (front == -1 || front > rear){
            cout << "Queue Underflow! Queue is empty." << endl;
            return;
        }

        cout<< arr[front] << "deleted from the queue." << endl;
        front++;

        if (front > rear){
            front = rear = -1;
        }
    }
    // display operation
    void display (){
        if (front == -1){
            cout << "Queue is empty." << endl;
            return;
        }

        cout << "Queue elements : ";
        for (int i = front; i<= rear; i++){
            cout << arr[i] << "";
        }
        cout << endl;
    }
}

main (){
    Queue q;
    int choice, value;

    do{
        cout << "\n    Queue Operations     ";
        cout << "\n1. Enqueue";
        cout << "\n2. Dequeue";
        cout << "\n3. Display";
        cout << "\n4. Exit";
        cout << "\nEnter your choice : ";
        cin >> choice;

        switch (choice){
            case 1 :
                cout << "Enter value to insert : ";
                cin >> value;
                
        }
    }
}