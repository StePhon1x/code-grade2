#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n], ans=0, maxs=-1;
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    for(int i=0; i<n-1; i++){
        if(a[i+1] - a[i] == 1){
            ans++;
        }
        else
            ans = 0;
        if(ans > maxs){
            maxs = ans;
        }
    }
    cout << ++maxs;


    return 0;
}