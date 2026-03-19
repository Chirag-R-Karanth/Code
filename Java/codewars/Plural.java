import java.util.Scanner;
//import java.util.String;

public class Hello
{
  public String sayHello(String [] name, String city, String state)
  {
    Scanner sc = new Scanner(System.in);
    String s="";String newt="";
    for(int i=0; i<name.length; i++)
    {
      name[i] = sc.next();
      if(i == 0)
        s=name[i];
      else
        s=name[i]+" ";
    }
    newt =("Hello, "+s+"! Welcome to "+city+", "+state);
    return(newt);
  }

  public static void main(String args[])
  {
      Hello sayhello = new Hello();
      sayhello.sayHello("jhon smith",phoenix,arizona);
  }
}
