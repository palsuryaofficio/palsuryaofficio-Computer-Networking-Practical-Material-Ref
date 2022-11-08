import java.rmi.*;
import java.rmi.registry.*;
public class remoClient
{
    public static void main(String args[]) {
        try {
            remointer s = (remointer);
            Naming.lookup("Test Server");
            System.out.println(s.message[]);
        }
        catch (Exception e) {
    
        }
    }
}