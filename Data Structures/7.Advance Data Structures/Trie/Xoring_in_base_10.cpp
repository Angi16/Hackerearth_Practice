    #include <vector>
    #include <list>
    #include <map>
    #include <set>
    #include <deque>
    #include <stack>
    #include <bitset>
    #include <algorithm>
    #include <functional>
    #include <numeric>
    #include <queue>
    #include <utility>
    #include <sstream>
    #include <iostream>
    #include <iomanip>
    #include <cstdio>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
    #include <cstring>
    #include <complex>
    #include <fstream>
     
    using namespace std;
     
    typedef long long LLN;
    typedef unsigned long long LLU;
     
    const double pi = 2.0 * acos(0.0);
    const double eps = 1.0e-7;
    const int dr[] = { -1, 0, 1, 0 }, dc[] = { 0, 1, 0, -1 };
    const int dr6[] = { 1, 1, 0, -1, -1, 0 }, dc6[] = { 0, 1, 1, 0, -1, -1 };
    const int dr8[] = { -1, -1, 0, 1, 1, 1, 0, -1 }, dc8[] = { 0, 1, 1, 1, 0, -1,
        -1, -1 };
     
    ////////////////////////////////////////////////////////////////////////////////
     
    int n, k, a[64][16], n1, n2, nodes, ptrs[10 << 20][10];
     
    void init(void) {
        nodes = 21;
    }
     
    inline void add(int a, int* v) {
        // printf("adding: "); for (int i = 0; i < 10; ++i) printf("%d", v[i]); puts("");
        while (*v >= 0) {
            if (ptrs[a][*v] <= 0) {
                ptrs[a][*v] = nodes++;
            }
            a = ptrs[a][*v];
            ++v;
        }
    }
     
    int query(int a, int* v) {
        // printf("querying: "); for (int i = 0; i < 10; ++i) printf("%d", v[i]); puts("");
        int x = 0;
        while (*v >= 0) {
            int d = 10;
            while (d-- > 0) {
                int e = d - *v;
                if (e < 0) e += 10;
                if (ptrs[a][e]) {
                    x = x * 10 + d;
                    a = ptrs[a][e];
                    break;
                }
            }
            if (d < 0) return -1;
            ++v;
        }
        return x;
    }
     
    inline void flat(int x, int* v) {
        for (int i = 10; i-- > 0; x /= 10) {
            v[i] = x % 10;
        }
        v[10] = -1;
    }
     
    void go1(int b, int c, int* v) {
        if (n1 - b + c + n2 < k) return;
        if (b < n1) {
            go1(b + 1, c, v);
            if (c + 1 <= k) {
                for (int i = 0; i < 10; ++i) {
                    v[i] += a[b][i];
                    if (v[i] >= 10) v[i] -= 10;
                }
                go1(b + 1, c + 1, v);
                for (int i = 0; i < 10; ++i) {
                    v[i] -= a[b][i];
                    if (v[i] < 0) v[i] += 10;
                }
            }
        } else {
            add(c, v);
        }
    }
     
    void dump(int a, int i, int* v) {
        if (i < 10) {
            for (int d = 0; d < 10; ++d) {
                if (ptrs[a][d] > 0) {
                    v[i] = d;
                    dump(ptrs[a][d], i + 1, v);
                }
            }
        } else {
            for (int j = 0; j < 10; ++j) printf("%d", v[j]);
            puts("");
        }
    }
     
    int ans;
     
    void go2(int b, int c, int* v) {
        if (n - b + c + n1 < k) return;
        if (b < n) {
            go2(b + 1, c, v);
            if (c + 1 <= k) {
                for (int i = 0; i < 10; ++i) {
                    v[i] += a[b][i];
                    if (v[i] >= 10) v[i] -= 10;
                }
                go2(b + 1, c + 1, v);
                for (int i = 0; i < 10; ++i) {
                    v[i] -= a[b][i];
                    if (v[i] < 0) v[i] += 10;
                }
            }
        } else {
            ans = max(ans, query(k - c, v));
        }
    }
     
    int main(void) {
      // freopen("input", "r", stdin);
      // freopen("output", "w", stdout);
     
      int kase = 1000000000;
      // scanf("%d", &kase);
     
      for (int ks = 1; ks <= kase && 2 == scanf("%d %d", &n, &k); ++ks) {
        // if (ks > 1) puts("");
        
        for (int i = 0, x; i < n && 1 == scanf("%d", &x); ++i) {
            flat(x, a[i]);
        }
        
        n1 = (n + 1) / 2;
        n2 = n - n1;
        init();
        
        int v[16] = {0};
        v[10] = -1;
        go1(0, 0, v);
        // printf("nodes = %d\n", nodes);
        // for (int i = 0; i <= n1; ++i) {
            // printf("XOR by %d number(s):\n", i);
            // dump(i, 0, v);
        // }
        
        int w[16] = {0};
        w[10] = -1;
        go2(n1, 0, w);
        printf("%d\n", ans);
      }
     
      return 0;
    }