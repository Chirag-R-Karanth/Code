package Initially.Java;

class Box
{
    double len,bre,hei;
    Box(double l, double b, double h)
    {
        len = l;
        bre = b;
        hei = h;
    }

    Box(double l)
    {
        len = l;
        bre = l;
        hei = l;
    }
    Box()
    {
        len=bre=hei=0;
    }

    double volume()
    {
        /*len = l;
        bre = b;
        hei = h;*/
        return len*bre*hei;
    }
    
}
public class constructorOverloading 
{
    public static void main(String[] args)
    {
        Box b1=new Box(10,20,30);
        Box b2=new Box();
        Box b3=new Box(10);
        System.out.println("3 inputs"+b1.volume());
        System.out.println("no Inputs:"+b2.volume());
        System.out.println("One input:"+b3.volume());
    }   
}
