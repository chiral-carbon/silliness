#include<iostream>
using namespace std;

int main()
{
	int M[26][9]={{0}}, n=1;
	for(int i=0;i<26;i++)
	{
		M[i][0]=65+i;
	}
	while(n<=8)
	{
		string s;
		cin>>s;
		int a[26]={0};
		for(int i=0;i<s.length();i++)
		{
			int x=s[i];
			a[x-65]++;
		}
		for(int i=0;i<26;i++)
			M[i][n]=a[i];
		n++;
	}
	cout<<endl;
	for(int i=0;i<26;i++)
	{
		for(int j=0;j<9;j++)
			cout<<M[i][j]<<"\t";
		cout<<endl;
	}
	return 0;
}
