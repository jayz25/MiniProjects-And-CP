#include<string>
#include<iostream>
#include<vector>
using namespace std;
int findSet(int arr[], int n, int k, int m) {

vector<int> remainder_set[k];

// calculate remainder set array

// and push element as per their remainder

for (int i = 0; i < n; i++) {

int rem = arr[i] % k;

remainder_set[rem].push_back(arr[i]);

}

// check whether sizeof any remainder set

// is equal or greater than m

for (int i = 0; i < k; i++) {

if (remainder_set[i].size() >= m) {

cout <<m<< "\n";

for (int j = 0; j < m; j++){

 cout << remainder_set[i][j] << "\n";  

     

}

return 1;

}

}

return 0;

}
int main()
{
    int n,k;

   cin>>n>>k;
   cin.ignore(numeric_limits<streamsize>::max(), '\n');

int arr[n];

for(int i=0;i<n;i++)

   cin>>arr[i];

int z;

int m = sizeof(arr)/sizeof(int);

for(int i=m;i>0;i--)

{

   z=findSet(arr, n, k, i);

   if(z==1)

   break;

}
    return 0;
}