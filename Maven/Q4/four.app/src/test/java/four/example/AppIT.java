package four.example;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class AppIT {
    @Test
    public void testdatabaseconnection(){
        System.out.println("-----RUNNING INTEGRATION TEST (Verify Phase)");
        boolean isDatabaseconnected=false;
        assertTrue(isDatabaseconnected,"The database connection is failed");
    }
}
