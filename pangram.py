def panagram(s):
    s=s.lower()
    set_a=sorted(set('abcdefghijklmnopqrstuvwxyz '))
    set_s=sorted(set(s))
    print("panagram" if(set_a==set_s) else "not panagram")

if __name__ =='__main__':
    s=input("enter the string")
    panagram(s)
