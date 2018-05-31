    #include <stdio.h>
    #include <string.h>
    #define N 500010
    int bt[N];
    char names[N][11];
    int query(int idx)
    {
    	int ans=0;
    	while(idx) ans+=bt[idx],idx&=idx-1;
    	return ans;
    }
    void update(int idx,int d)
    {
    	while(idx<N){ bt[idx]+=d;idx+=idx&-idx;};
    }
    int tms[N];
    int q[N];
    int main()
    {
        int t;
        scanf("%d",&t);
        while(t--)
        {
        	memset(bt,0,sizeof bt);
        	int n;
        	scanf("%d",&n);
        	for(int i=1;i<=n;++i) scanf("%s",&names[i]);
        	for(int i=1;i<=n;++i) scanf("%d",&tms[i]);
        	int mx=-1;
        	for(int i=1;i<=n;++i) 
        	{
        		update(i,1);
        	}
        	for(int i=0;i<n-1;++i) scanf("%d",&q[i]);
        	q[n-1]=1;
        	for(int i=0;i<n;++i)
        	{
        		int k=q[i];
        		int l=1,r=n;
        		while(l!=r)
        		{
        			int m = (l+r)/2;
        			int res = query(m);
        			if(res>=k) r=m;
        			else l = m+1;
        		}
        		if(mx<tms[l]) mx=tms[l];
        		update(l,-1);
        		printf("%s %d\n",names[l],mx);
        	}
        }
        return 0;
    }
 