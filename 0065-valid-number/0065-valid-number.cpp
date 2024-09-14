class Solution {
public:
    bool isNumber(string s) {
        
          int n = s.size();
        int i = 0;

        // Skip leading spaces
        while (i < n && isspace(s[i])) i++;

        // Check for empty string after removing spaces
        if (i == n) return false;

        // Check for sign
        if (s[i] == '+' || s[i] == '-') i++;

        bool isNumeric = false;
        // Process digits before decimal point
        while (i < n && isdigit(s[i])) {
            i++;
            isNumeric = true;
        }

        // Process decimal point
        if (i < n && s[i] == '.') {
            i++;
            // Process digits after decimal point
            while (i < n && isdigit(s[i])) {
                i++;
                isNumeric = true;
            }
        }

        // If no digits found so far, it's invalid
        if (!isNumeric) return false;

        // Process exponent if present
        if (i < n && (s[i] == 'e' || s[i] == 'E')) {
            i++;
            if (i == n) return false; // Exponent must be followed by digits

            // Check for sign after exponent
            if (s[i] == '+' || s[i] == '-') i++;

            bool isExponentNumeric = false;
            while (i < n && isdigit(s[i])) {
                i++;
                isExponentNumeric = true;
            }

            if (!isExponentNumeric) return false;
        }

        // Skip trailing spaces
        while (i < n && isspace(s[i])) i++;

        // If we've processed all characters, it's a valid number
        return i == n;
        
    }
};