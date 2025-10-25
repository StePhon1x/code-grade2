#include <iostream>
#include <iomanip>
#include <climits>
using namespace std;




int main() {
    int n;
    cin >> n;
    int arr[n];
    int max_n = INT_MIN, min_n = INT_MAX;
    double s=0;
    for(int i=0; i<n; i++){
        cin >> arr[i];
        if(arr[i] > max_n){
            max_n = arr[i];
        }
        if(arr[i] < min_n){
            min_n = arr[i];
        }
        
    }
    bool removed_max = false, removed_min = false;
    for(int i=0; i<n; i++){
        if (arr[i] == max_n && !removed_max) {
            removed_max = true;
            continue;
        }
        if (arr[i] == min_n && !removed_min) {
            removed_min = true;
            continue;
        }
        s += arr[i];
    }
    
    cout << fixed << setprecision(2) << s/(n-2) << endl;


    return 0;
}