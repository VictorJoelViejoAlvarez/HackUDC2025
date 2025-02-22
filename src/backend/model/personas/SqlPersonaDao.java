
import java.sql.Connection;
import java.util.List;

public interface SqlPersonaDao {

    public Persona create(Connection connection, Persona persona);

    public void update(Connection connection, Persona persona) throws InstanceNotFoundException;

    public Persona findById(Connection connection, long id) throws InstanceNotFoundException;

    public List<Persona> findByName(Connection connection, String name, String surname1, String surname2);
}