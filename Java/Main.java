package Initially.Java;

public class Main
{
    public static void main(String[] args)
    {
        getterSetter getset=new getterSetter();
        getset.setAge(25);
        getset.setId(101);
        getset.setName("John Doe");

        System.out.println("age:"+getset.getAge());
        System.out.println("ID:"+getset.getId());
        System.out.println("Name:"+getset.getName());
    }
}