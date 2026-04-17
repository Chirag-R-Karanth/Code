//centered star pattern
public class pattern
{
    public static void main(String [] args)
    {
        pattern p1 = new pattern();
        p1.forward();
        p1.backward();
    }

    public void forward()
    {
        for(int j =1; j<10; j+=2)
        {
            for(int i=1; i<j; i+=2)
            {

                System.out.print("*");
            }
            System.out.println();
        }
    }

    public void backward()
    {
        for(int j = 5; j>0; j-=2)
        {
            for(int i=0; i<j; i+=2)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
