
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public abstract class AbstractSqlPersonaDao implements SqlPersonaDao {

    @Override
    public void update(Connection connection, Persona persona) throws InstanceNotFoundException{

        String stringQuery = "UPDATE Persona " +
                "SET nombre = ?, apellido1 = ?, apellido2 = ?, " +
                "empleado = ?, telefono = ?, email = ? " +
                "WHERE id = ?";

        try(PreparedStatement preparedStatement = connection.prepareStatement(stringQuery)){

        }

    }

}