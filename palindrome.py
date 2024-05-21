def palindrome(s):
    s=s.lower()
    count=len(s)
    p_str=""
    for i in range(count-1,-1,-1):
        p_str+=s[i]
    print("palindrome" if(s==p_str) else "not palindrome")

if __name__ =='__main__':
    s=input("Enter a string\n")
    palindrome(s)
