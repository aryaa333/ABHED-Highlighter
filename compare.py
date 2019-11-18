
class Compare:
    def comp(self,file1,file2):

        a=input("enter string1:")
        b=input("enter string2:")

        c=a.split(' ')
        d=b.split(' ')
        v=0
        for i in range(len(c)):

                for j in range(len(d)):
                    if c[i]==d[j]:
                        print(c[i])

                        v += 1

        print(v)
        r=len(c)/v
        print(r)
