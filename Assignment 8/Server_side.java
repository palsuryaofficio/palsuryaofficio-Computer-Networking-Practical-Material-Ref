import java.rmi.*;
import java.rmi.server.*;
public class remoServer extends UnicastRemoteObject
implements remointer
{
    public remoServer() throws Remote Exception {
        return "Hi";
    }
    public static void main (String args[]) {
        try {
            remoServer r = new remoServer();
            Naming.rebind("Test Server", r);
            System.out.println("The server is ready");
        }
        catch (Exception e) {

        }
    }
}