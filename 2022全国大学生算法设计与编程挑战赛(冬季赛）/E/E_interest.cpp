#include<bits/stdc++.h>
using namespace std;
int main(){
	int n,now;cin>>now>>n;
	for(int i=1;i<=n;i++){
		int x=min(now,50);
		now+=x/10+5;
	}cout<<now<<endl;
	return 0;
}

