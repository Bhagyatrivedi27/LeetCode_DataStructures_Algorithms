class Solution {
public:
     bool existHelper(vector<vector<char>>&board, vector<vector<bool>>&visited, int startI, int startJ, string &word, int startWord){
        int n = board.size(), m = board[0].size();
        if(startWord == word.size()) return true;
        if(startI < 0 || startI>=n || startJ < 0 or startJ >= m)
            return false;
        
        
        if(visited[startI][startJ]) return false;
        
        
        if(board[startI][startJ] != word[startWord])
            return false;
        
        visited[startI][startJ] = true;
        
        //recurrence 
      bool t1 = existHelper(board,visited, startI-1, startJ, word, startWord+1) ||                   existHelper(board,visited, startI+1, startJ, word, startWord+1) ||
        existHelper(board,visited, startI, startJ-1, word, startWord+1) ||
        existHelper(board,visited, startI, startJ+1, word, startWord+1);
        
        visited[startI][startJ] = false;
        return t1;
    }
    bool exist(vector<vector<char>>& board, string word) {
       int n= board.size(), m= board[0].size();
        vector<vector<bool>>visited(n,vector<bool>(m,false));
        bool t1;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(board[i][j] == word[0]){
                   t1 = existHelper(board, visited, i, j, word, 0);
                    if(t1)
                        return true;
                }
            }
        }
        return false;
    }
};