package sorting;

public class selectionsort {
     /* it sorts an array by repeatedly finding the minimum element from 
      * unsorted part and putting it at the beginning.
            */
     void sort(int array[]) {	
          int n=array.length;
          
    	 for(int i=0;i<n-1;i++) {
    		 int min=i;
    		 for(int j=i+1;j<n;j++) {
    			 if(array[j]<array[min]) {
    				 min=j;
    			 }
    		   }
    		 
    			 int temp=array[min];     //swaping
    			 array[min]=array[i];
    			 array[i]=temp;	 
    		 } 
    	 }
     
     
     void print(int array[])
     {
    	 for(int i=0;i<array.length;i++)
    	 {
    		 System.out.print(array[i]+" ");
    	 }
    	 System.out.println();
     }
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
         int array[]={15,45,89,6,9,56,18,65};
         selectionsort ob=new selectionsort();
         ob.sort(array);
         ob.print(array);
    }

}
