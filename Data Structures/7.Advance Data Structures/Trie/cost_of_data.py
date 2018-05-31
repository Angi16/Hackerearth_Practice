n = int(input())
res = 1
st = []
for i in range(n):
    st.append(input())
mxst = max([len(s) for s in st])
for i in range(mxst):
    res+= len(set([s[:i+1] for s in st if len(s) > i]))
print(res)