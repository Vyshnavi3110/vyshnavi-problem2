#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,k;
    int sum=0,maxsum=0;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
       cin>>a[i];
    }
    cin>>k;
    for(int i=0;i<n;i++)
    {
    for(int j=i;j<k;j++)
    {
      sum+=a[j];
    
   }
   
 maxsum=max(maxsum,sum)-10;
 
    }
    
    cout<<maxsum;

}
