#include <stdio.h>
int main()
{
    int n,m,i,j,k,cnt,ans,temp;
    int card[6],sum[300000],minus[300000];
    cnt=1;
    ans=0;
    scanf("%d %d",&n,&m);
    for(i=1;i<=n;i++)
    {
        scanf("%d",&card[i]);
    }
    for(i=1;i<=n;i++)
    {
        for(j=i+1;j<=n;j++)
        {
            for(k=j+1;k<=n;k++)
            {
                sum[cnt]=card[i]+card[j]+card[k];
                cnt+=1;
            }
        }
    }
    for(i=1;i<cnt;i++)
    {
        minus[i]=m-sum[i];
    }
    for(i=1;i<cnt;i++)
    {
        for(j=i+1;j<cnt;j++)
        {
            if(minus[i]>minus[j])
            {
                temp=minus[i];
                minus[i]=minus[j];
                minus[j]=temp;
            }
        }
    }
    for(i=1;i<cnt;i++)
    {
        if(minus[i]>=0)
        {
            ans=i;
            break;
        }
    }
    printf("%d",sum[ans]);
    return 0;
}
