#include <iostream>
using namespace std;
typedef long long int ll;
int m(int x)
{
	return (x*(x-1));
}
int main()
{
	ll sum=0;
	for(int i=1;i<=26;i++)
	{
		int x;
		cin>>x;
		sum+=m(x);
	}
	cout<<sum<<endl;
	return 0;
}
