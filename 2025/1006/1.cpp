#include <iostream>
using namespace std;

// 所有质数（除了2和3）都可以表示为：6k+1(-1)
bool isPrime(int n) {
    if (n < 2) return false;           // 小于2的数不是质数
    if (n == 2 || n == 3) return true; // 2和3是质数
    if (n % 2 == 0 || n % 3 == 0) return false; // 排除能被2或3整除的数

    // 从5开始，只检查形如 6k ± 1 的数
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

bool isPrimePalindrome(int n){
    string s = to_string(n);
    int i = 0;
    int len = s.size();
    for(int i = 0; i < len/2; i++){
        if(s[i] != s[len-1-i]) return false;
    }
    return true;
}



int main()
{
    int a, b;
    cin >> a >> b;
    if(a <= 2){ if(b >= 2) cout << 2 << endl; a = 3; }
    if(a%2==0)a++;
    for(int i = a; i<=b; i++){
        if(i%2!=0){
            if(isPrime(i) && isPrimePalindrome(i)){
                    cout << i << endl;
                }
            }
        }   
    return 0;
}