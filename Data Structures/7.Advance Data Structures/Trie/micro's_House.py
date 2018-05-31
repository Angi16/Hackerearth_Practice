#include <iostream>
using namespace std;
 
int main()
{
    int n,m;
    cin>>n;
    cin>>m;
    long int arr[n][m];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin>>arr[i][j];
            //x=x^arr[i][j];
           // cout<<arr[i][j];
        }
    }
    
 
    long int max=0;
    long int m_max=0;
    long int ar[m];
    for( int d=0;d<m;d++)
    {
        ar[d]=0;
    }
 
    for( int h=0;h<20;h++)
    {
     for( int d=0;d<m;d++)
    {
        ar[d]=0;
    }
    for( int j=h;j<n;j++)
    {
        max=0;
    for( int k=0;k<m;k++)
    {
        
        ar[k]=ar[k]^arr[j][k];
      
       if(max<ar[k])
       {
           max=ar[k];
       }
       else if(max<(max^ar[k]))
       {
           max=max^ar[k];
       }
       if(max>m_max)
       {
           m_max=max;
       }
    }
  //  cout<<"m _max is "<<m_max<<endl;
    }
    }
 
    cout<<m_max<<endl;
    return 0;
}