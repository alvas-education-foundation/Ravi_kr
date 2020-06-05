class Solution {
    public boolean isPalindrome(int x) {
        
        if(x<0)
            return false;
        
        
         int y=x, rem=0,rev=0;
       while(x!=0){
           rem=x%10;
           rev=(rev*10)+rem;
           x=x/10;
          
       } 
        if(rev==y)
           return true;
        else
            return false;
        
        
    }
}