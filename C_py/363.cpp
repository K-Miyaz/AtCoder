#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

// Palindrome check function
bool is_palindrome(const string &s) {
    return s == string(s.rbegin(), s.rend());
}

int main() {
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    // Set to hold unique permutations
    set<string> unique_permutations;
    sort(S.begin(), S.end());
    
    // Generate all unique permutations
    do {
        unique_permutations.insert(S);
    } while (next_permutation(S.begin(), S.end()));

    int ans = 0;

    for (const auto &perm : unique_permutations) {
        bool valid = true;
        
        // Check for palindromic substrings of length K
        for (int i = 0; i <= N - K; i++) {
            if (is_palindrome(perm.substr(i, K))) {
                valid = false;
                break;
            }
        }
        
        if (valid) {
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}
