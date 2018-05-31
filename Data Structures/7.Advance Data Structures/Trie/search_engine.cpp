using namespace std;
 
#define si(a)				scanf("%d",&a)
#define sl(a)				scanf("%lld",&a)
#define pi(a)				printf("%d\n",a)
#define pl(a)				printf("%lld\n",a)
 
typedef long long			ll;
typedef vector<int>			vi;
typedef pair<int, int>		ii;
typedef vector<vi>			vvi;
typedef vector<ii>			vii;
 
#define fast_io				ios_base::sync_with_stdio(false);cin.tie(NULL)
#define SET(a,b)			memset(a,b,sizeof(a))	
#define forall(i,a,b)		for(int i=a; i<b; i++)
#define forrev(i,a,b)		for(int i=a; i>=b; i--)
#define forr(it,container)  for(auto it=container.begin(); it!=container.end(); it++)
#define w(t)				int t;si(t);while(t--)
 
#define TRACE
 
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1) {
	cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) {
	const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1 << " | ";__f(comma + 1, args...);
}
#else
#define trace(...)
#endif
 
int trie[26 * 1000005], nxt[1000005][26], counter=1;
 
void insert(string s, int w)
{
	int cur = 1;
	for (int i = 0;i < int(s.size());i++)
	{
		trie[cur] = max(trie[cur], w);
		int to = s[i] - 'a';
		if (!nxt[cur][to])
			nxt[cur][to] = ++counter;
		cur = nxt[cur][to];
	}
	trie[cur] = max(trie[cur], w);
}
 
int query(string s)
{
	int cur = 1;
	for (int i = 0;i < int(s.size());i++)
	{
		int to = s[i] - 'a';
		if (nxt[cur][to] == -1)
			return -1;
		cur = nxt[cur][to];
	}
	return trie[cur];
}
 
int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	fast_io;
	int n, q;
	cin >> n >> q;
	forall(i, 0, n)
	{
		string s;int w;
		cin >> s >> w;
		insert(s, w);
	}
	while (q--)
	{
		string s;
		cin >> s;
		int ans = query(s);
		if (ans == 0)cout << "-1\n";
		else cout << ans << "\n";
	}
	return 0;
}