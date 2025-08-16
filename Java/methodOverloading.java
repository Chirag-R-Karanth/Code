package Initially.Java;
//package Initially;
//import Initially.Java.addition;
public class methodOverloading
{
        public static void main(String[] args)
    {
        addition add = new addition();
        System.out.println(add.add(10, 20)); // Calls the first add method
        System.out.println(add.add(10, 20, 30)); // Calls the second add method
        System.out.println(add.add(10.5, 20.5)); // Calls the third add method
    }
    
}