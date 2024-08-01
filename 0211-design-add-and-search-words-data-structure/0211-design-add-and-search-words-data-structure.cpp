struct trieNode{
    trieNode(){
        isWord = false;
        for(int i=0;i<26;i++)
            next[i]=NULL;
    }
    bool isWord;
    trieNode *next[26]; 
};
class WordDictionary {
public:
    trieNode *root;
    trieNode dummy;
    
    WordDictionary() {
        root = &dummy;    
    }
    
    void addWord(string word) {
        int n = word.size();
        trieNode *curr = root;
        for(int i=0;i<n;i++){
            if(!curr->next[word[i]-'a'])
                curr->next[word[i]-'a'] = new trieNode;
            
            curr = curr->next[word[i]-'a'];
        }
         curr->isWord = true;
    }
    
    bool searchHelper(string &word, int id, trieNode* root){
        int n = word.size();
        if(id==n && root)
            return root->isWord;
        if(!root) return false;
        
        trieNode *curr = root;
        bool temp=false;
        
        for(int i=id;i<n;i++){
            if(word[i]!='.'){
                if(!curr->next[word[i]-'a'])
                    return false;
                curr = curr->next[word[i]-'a'];               
            } else{
                for(int j=0;j<26;j++){
                    if(curr->next[j])
                        temp = searchHelper(word, i+1, curr->next[j]);
                    if(temp)
                        return true;
                }
                return false;
            }
            }
            return curr->isWord;
    }
    bool search(string word) {
        return searchHelper(word, 0, root);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */