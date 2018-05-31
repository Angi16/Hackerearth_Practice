int main()
{   int arr[100005],cnt[100005],n,i,j,temp,k,var;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    scanf("%d",&k);
    for(j=0;j<n;j++)
    {
        var=arr[j];
        cnt[var]++;
    }
    for(i=0;i<100005;i++)
    {
        if(cnt[i]==k)
        {
            printf("%d",i);
            break;
        }
    }
    return 0;
}
Language: C