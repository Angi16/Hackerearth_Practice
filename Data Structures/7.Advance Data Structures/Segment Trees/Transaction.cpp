#include <bits/stdc++.h>
using namespace std;
 
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,n,a) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define aLL(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;
const int mod=1000000007;
LL powmod(LL a,LL b) {LL res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
int in(){ int x; scanf("%d",&x); return x; }
const int N = 1e5 + 100;
int t, q, ans[N], fen[N];
PII a[N];
pair<PII,int> qu[N];
void add(int p){
    p++;
    for(; p < N; p+=p&-p)
        fen[p]++;
}
int get(int p){
    int ret = 0;
    for(; p; p -= p&-p ) ret += fen[p];
    return ret;
}
int b[N];
int32_t main(){
    t = in(), q = in();
    rep(i,0,t) a[i] = PII(in(),i), b[i] = a[i].fi;
    sort(a,a+t);
    int s,ss;
   rep(i,0,q)
        s = in(), ss = in()-1,qu[i] = make_pair(PII(s,ss),i);
   sort(qu,qu+q);
    int i = t-1;
    int mxr = -1, sz = 0;
    b[N-1] = -1;
    for(int j = q-1; j>-1; j--){
       while(i>-1 && a[i].fi>=qu[j].fi.fi){
           add(a[i].se ); 
           mxr = max(a[i].se,mxr);
           sz++;
          i--; 
       }
       if( sz <= qu[j].fi.se ) ans[qu[j].se] = N-1;
       else{
           int l = -1, r = mxr+1;
           while( r-l > 1 ){
               int mid = (l+r)/2;
               if( get(mid)>qu[j].fi.se ) r = mid;
               else l = mid;
           } 
           ans[qu[j].se] = l;
       } 
    } 
    for(i = 0;i < q; i++) cout << b[ans[i]] << '\n';
}