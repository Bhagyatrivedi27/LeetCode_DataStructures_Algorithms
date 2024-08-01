struct trieNode{
    trieNode() {
        isWord = false;
        int i;
        for(int i=0;i<26;i++)
            next[i] = NULL;
    }
    bool isWord;
    trieNode *next [26];
};

class Trie {
public:
    trieNode *root;
    trieNode dummy;
    Trie() {
        root = &dummy;
    }
    
    void insert(string word) {
        int n = word.size(), i;
        trieNode *curr = root;
        
        for(i=0;i<n;i++){
            if(!curr->next[word[i]-'a']){
                curr->next[word[i]-'a'] = new trieNode;
            }
            curr = curr->next[word[i]-'a'];
        }
        
        curr->isWord = true;
        
    }
    
    bool search(string word) {
        int n = word.size(), i;
        trieNode *curr = root;
        
        for(int i=0;i<n;i++){
            if(!curr->next[word[i]-'a'])
                return false;
            curr = curr->next[word[i]-'a'];
        }
        return curr->isWord;
    }
    
    bool startsWith(string prefix) {
          int n = prefix.size(), i;
        trieNode *curr = root;
        
        for(int i=0;i<n;i++){
            if(!curr->next[prefix[i]-'a'])
                return false;
            curr = curr->next[prefix[i]-'a'];
        }
        
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */