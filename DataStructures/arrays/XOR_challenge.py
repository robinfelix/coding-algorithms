from itertools import combinations
# C = 59139
# input_l = list(range(1,C+1))
# com_C = []
# for pair in combinations(input_l, 2):
#     A = pair[0]
#     B = pair[1]
#     xor = A^B
#     if xor == C:
#         mul = A*B
#         result,pos = 0,1
#         if mul > result:
#                 result = mul
#                 pos += 1

'''
Problem
You are given an Integer C such that the XOR of two integers (A,B) is C. In short A ⊕ B = C (⊕ denotes the bitwise XOR operation)

Out of all possible pairs of A and B, you have to find such two integers such that their product is maximum. 

Let's define L(A) = the length of A in its binary representation. Then, L(A) <= L(C) and L(B) <= L(C).

Input format 

Single Integer representing C (0⩽C⩽105).

Output format 

Ouptut the maximum product we can achieve under the given conditions.

Sample Input
13
Sample Output
70

Explanation
The binary representation of 13 is "1101".

We can use A=10 ("1010" in binary) and B=7 ("0111" in binary). This gives us the product 70. No other valid pair (A,B) can give us a larger product.
'''
'''
You would need basic XOR concept to understand this problem. The XORed result has either two kind of bits in binary representation.

If ith bit is 0 in C then ith bit of A & B should be either 0 or 1 in both the integers. Since we need maximized product so we will always set ith bit = 1 in A & B whenever ith bit is 0 in C.

Now interesting case comes when ith bit is 1 in C. We know that either one of A & B has ith bit set and other unset. If you list put every possible combinations you will notice that the sum of A & B remains constant. And when sum of A & B is constant we get maximum product when A & B are at close to each other.

Eg A+B = 6.
Possible Combinations :
A  B Product
1  5   5
2  4   8
3  3   9

So we get max product 9 when A and B are very close to each other. 

So to make A & B close to each other, we apply greedy approach and it goes as follows :

For MSB set bit in C we will set that bit in A and for all the other set bit in C, we will make that bit set in B. So that A and B are close to each other and product maximises.
'''
'''
#include<bits/stdc++.h>
#include<climits>
using namespace std;
 
#define debug(x,y) cout<<(#x)<<" " <<(#y)<<" is " << (x) <<" "<< (y) << endl
#define watch(x) cout<<(#x)<<" is " << (x) << endl 
#define fast ios_base::sync_with_stdio(false)
#define fie(i,a,b) for(i=a;i<b;i++)
#define MOD 1000000007
#define mod 998244353
#define PB push_back 
#define EB emplace_back
#define MP make_pair
#define FI first
#define SE second
#define ll long long 
#define lld long long int
#define ALL(x) (x).begin(),(x).end()
 
typedef vector<lld> vi;
typedef vector<vector<lld>> vii;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<pair<lld, lld>> vpi;
typedef long long LL;
 
string convert(lld n) {
    string s = "";
    while (n > 0) {
        if (n % 2 == 1) s = "1" + s;
        else s = "0" + s;
        n /= 2;
    }
    return s;
}
 
 
lld convertBack(string s) {
    lld n = 0 , p = 1;
    for (lld i = s.length() - 1; i >= 0; i--) {
        n += ((s[i] - '0') * p);
        p *= 2;
    }
    return n;
}
 
int main() {
    fast;
    cin.tie(0);
    lld n, i;
    //converting number to binary
    cin >> n;
    string s = convert(n);
    string a = "" , b = "";
    bool first = false;
    //greedy approach mentioned in editorial
    //brief explanation again here :
    //if ith bit is 0 in original number then, ith bit in A & B should be 1 to maximise product.
    //if ith bit is 1 in original number then the MSB of C should be set in A and all the other set bit in C should be set in B.
    //So that both the numbers A & B are close to each other in their magnitude which results in maximum product.
    for (i = 0; i < s.length(); i++) { 
        if (s[i] == '0') {
            a += "1";
            b += "1";
        }
        else {
            if (first) {
                a += "0";
                b += "1";
            }
            else {
                a += "1";
                b += "0";
                first = true;
            }
        }
    }
    //convert back from binary representation to their respective numbers.
    lld n1 = convertBack(a);
    lld n2 = convertBack(b);
    cout << n1*n2 << endl;
}
'''
print(result)