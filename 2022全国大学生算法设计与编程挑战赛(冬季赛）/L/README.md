# 看错题
## Description
### 题目背景
小Y同学发现自己的数学思维真是太差了，自己写题目的时候总喜欢去写数据结构题，因为数据结构大都是模板，就是背了板子就能强行干题，但是数据结构只要有一点思维在里面，他就不会做了，因此他决定去做题网站写一写题。

巧合的是他看到了一道题，这道题要求的是，给定一颗线段树，每次区间加一个xx，如果每次在线段树区间加操作做完后，从根节点开始等概率的选择一个子节点进入，直到进入叶子结点为止，将一路经过的节点权值累加，最后能得到的期望值是多少？

不巧的是，小Y同学看错题辣，他把进入叶子节点看成了，依次选一个叶子节点进入，然后一直走到根节点，问最后得到的期望值是多少，巧合的是，他这么写了以后还把样例都过了，然后喜提WA声一片。

小Y同学很难受，于是把他看错的题意给你，看看你是否能做出这道题。
### 题目描述
首先题目描述里面，对于线段树的下放过程是这样的
> void build(int rt,int l,int r){
>
> if(l==r){tr[rt]=a[l];return ;}
>
> int mid=(l+r)>>1;
>
> build(ls,l,mid);
>
> build(rs,mid+1,r);
>
> tr[rt]=tr[ls]+tr[rs];
>
> }
>
> void update(int rt,int l,int r,int q,int v){
>
> if(l==r){tr[rt]+=v;return;}
>
> int mid=(l+r)>>1;
>
> if(q<=mid)update(ls,l,mid,q,v);
>
> else update(rs,mid+1,r,q,v);
>
> }

> //主函数中建树和下放的代码为
>
> build(1,1,n);
>
> for(int i=l;i<=r;i++)
>
> update(1,1,n,i,v);

小Y同学为了让题目更简单，对于n个整数，n是一个2^x的整数，来保证这个线段树是一棵满二叉树。

他现在想问你，每次给一段区间加上一个整数（每次操作对后续有影响），然后依次在线段树中选一个叶子节点，
一直走到根节点，将一路经过的节点权值累加，问把每一个叶子节点选择一遍后的全部的总和是多少。
## Input
第一行整数n,m,表示线段树维护的原序列的长度，询问次数。

第二行n(1≤n≤2^17)个数，表示原序列。

接下来m(1≤m≤100000)行，每行三个数l,r,x表示对区间[l,r]加上x
## Output
共m行，表示查询的权值和。
## Sample Input
8 2 

1 2 3 4 5 6 7 8

1 3 4

1 8 2
## Sample Output
720

960
