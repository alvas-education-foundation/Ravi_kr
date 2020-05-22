package sorting;

public class bubblesort {
	/* Bubble sort is the simplest sorting algorithm that works by
	  repeatedly swapping the adjacent elements if they are in wrong order */
	void sort(int arr[])
	{
		int n=arr.length;
		for(int i=0;i<n;i++) {
			for(int j=0;j<n-i-1;j++) {  //b j<n-1  -i removes unwanted compare
	
				if(arr[j]<arr[j+1])
				{
					int temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
				}
				
			}
		}
	}
	
	void print(int arr[]) {
		for(int i=0;i<arr.length;i++) {
		System.out.print(arr[i]+" ");
		}
	}
	
	public static void main(String[] args) {
		bubblesort ob=new bubblesort();
		int arr[]= {8,34,52,22,45,15};
		 ob.sort(arr);
		 ob.print(arr);
	}

}
