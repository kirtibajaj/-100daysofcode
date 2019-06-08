def conversion(n):
    convertword=""
    ones=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty']
    tens=['Zero','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    if (n==0):
        return "Zero"
    if n<0:
          n=int(str(n)[1:])
          return "minus"+conversion(n)
    if ((n//1000)>0):
        convertword+=conversion(n//1000)+"thousand"
        n%=1000
    if ((n//100)>0):
        convertword+=conversion(n//100)+"Hundred"
        n%=100
    if n>0:
        if n<20:
            convertword+=ones[n]
        else:
            convertword+=tens[n//10]
            if (n%10)>0:
                convertword+=ones[n%10]
    return convertword
def main():
    a,b=map(int,input().split())
    if a==0 and b==0:
        print("1")
        exit(0)
    if a<=90000 and b<=90000:
        x=a
        y=b
        while(a!=b):
            m=a
            n=b
            if(a>=99999 or b>=99999):
                print("Out of bounds")
                break
            haha1=conversion(m)
            haha2=conversion(n)
            if(haha1>haha2):
                m=b
                n=a
            else:
                m=a
                n=b
            x=a+m
            y=b+n
            a=x
            b=y
            if(x==y):
                print(x)
                break
        else:
            print(a)
if __name__ == '__main__':
    main()
