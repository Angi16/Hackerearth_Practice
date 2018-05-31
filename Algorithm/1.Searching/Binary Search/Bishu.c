
#include<stdio.h>
int main()
{
int n,i,q,pwr;
scanf("%d",&n);
int arr[n];
for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
}
scanf("%d",&q);
while(q--)
{
 
int count=0,sum=0;
scanf("%d",&pwr);
for(i=0;i<n;i++)
{
	if(arr[i]<=pwr)
	{
		count++;
		sum+=arr[i];
	}
}
printf("%d %d\n",count,sum);
}
return 0;
}