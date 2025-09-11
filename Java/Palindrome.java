import java.util.Scanner;

class Palindrome
{
  public static void main() 
  {
    char str[] = 'Chirag R Karanth';
    char revchar = '\0';
    String revstr = new String();
    for(int i=0; i<str.lenth(); i++)
    {
      revchar = str[i];
      revstr = revstr + revstr;
      revchar = '\0';
    }
  }
}
