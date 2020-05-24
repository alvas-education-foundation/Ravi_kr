package mypack;  
public class Employee implements java.io.Serializable{  
private int id;  
private String name;  
public Employee(){}  

public void setId(int id){
this.id=id;
}  
public int getId(){
return id;
}  
public void setName(String name){
this.name=name;
}  
public String getName(){
return name;
}  
}  

To access the JavaBean class, we should use getter and setter methods.
package mypack;  
public class Test{  
public static void main(String args[]){  
Employee e=new Employee();//object is created  
e.setName("Arjun");//setting value to the object  
System.out.println(e.getName());  
}
}  

