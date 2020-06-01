class Solution {
    public int lengthOfLastWord(String s) {
       int track=0,flag=0;
        
        var h=s.strip();
       char arr[]=h.toCharArray();  
       for( int i=0; i<arr.length;i++)
       {
           if(arr[i]==' ')
           {
               track=i;
                flag=1;
           }       
       }
        if(flag==0)
        {
            return arr.length;
        }
        if(flag==1)
        {
            return arr.length-track-1;
        }
        
        
        return 0;
}
}