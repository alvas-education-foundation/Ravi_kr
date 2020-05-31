class Solution {
    public int reverse(int x) {
        int rem=0,rev=0,prev_rev=0;
       while(x!=0){
           rem=x%10;
           rev=(rev*10)+rem;
           x=x/10;
          if ((rev - rem) /  10 != prev_rev) 
        { 
            
            return 0; 
        } 
           prev_rev=rev;
       } 
        return rev;
    }
}