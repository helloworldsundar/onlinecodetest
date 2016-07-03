#include <iostream>

using namespace std;

class Solution {
    //Write your code here

};


/**
class : Node

represents Node Class with character instance
& next instance of Node

*/
class Node
{
public:
   char* m_data;
   Node* m_next;

   Node(){
      m_data=new char('\0');
      m_next=NULL;  
   }
   
   Node(char c){
      m_data=new char(c);
      m_next=NULL;  
   }
   
   char getData(){
       return *(m_data);
   }
   
   Node* getNext(){
       return m_next;
   }
   
   void setNext(Node* addr){
       m_next=addr;
   }
   
   void setData (char c){
       *m_data=c;
   }
};
/**
class : Stack

represents a Stack with LIFO implementation
*/
class Stack{
public:
   Node* m_top;

   Stack(){
      m_top = NULL;
   }
   
   void pushCharacter(char c){
       // create the new node and push it to the top
       Node* newNode = new Node(c);
       
       if (m_top == NULL){
           m_top = newNode;
       }
       else{
           Node* temp = m_top;
           m_top = new Node (c);
           m_top->setNext (temp);
       }
   }
   
   char popCharacter(void){
       
       if (m_top == NULL){
           return '\0';
       }
       // reduce the stack by one by popping one character
       Node* nextStack = m_top->getNext ();
       char stack_data = m_top->getData ();
       m_top = nextStack;
       return (stack_data);
   }
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
