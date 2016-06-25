#include <iostream>

using namespace std;

class Solution {
    //Write your code here

};

class Node {
protected:
   void* data;
   Node* next;
public:
   void* getData(){return this->data;};
   Node* getNext(){return this->next;};
   void setData(void* data){this->data=data;};
   void setNext(Node* next){this->next=next;};
};

class CharNode:Node{
public:
   char getData(){return *((char*)this->data);};
   void setData(char* c){this->data = &c;};
};


class Stack{
private:
   Node* head;
public:
   


};

//Below text , assume it is read only

int main() {
    // read the string s.
    string s;
    getline(cin, s);
    
  	// create the Solution class object p.
    Solution obj;
    
    // push/enqueue all the characters of string s to stack.
    for (int i = 0; i < s.length(); i++) {
        obj.pushCharacter(s[i]);
        obj.enqueueCharacter(s[i]);
    }
    
    bool isPalindrome = true;
    
    // pop the top character from stack.
    // dequeue the first character from queue.
    // compare both the characters.
    for (int i = 0; i < s.length() / 2; i++) {
        if (obj.popCharacter() != obj.dequeueCharacter()) {
            isPalindrome = false;
            
            break;
        }
    }
    
    // finally print whether string s is palindrome or not.
    if (isPalindrome) {
        cout << "The word, " << s << ", is a palindrome.";
    } else {
        cout << "The word, " << s << ", is not a palindrome.";
    }
    
    return 0;
}