/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if(head == NULL || head->next == NULL)
            return NULL;
        
        ListNode *first = head, *last = head;
        
        for(int i=0;i<n && last!=NULL; i++)
            last = last->next;
        
        if(last == NULL)
            return first->next;
        
        while(last->next != NULL){
            first = first->next;
            last = last->next;
        }
        ListNode* temp = first->next;
        first->next = first->next->next;
        delete(temp);
        return head;
        
    }
};