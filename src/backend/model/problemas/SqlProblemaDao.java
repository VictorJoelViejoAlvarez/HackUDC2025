

public interface SqlProblemaDao {

    public Problema create(Connection connection, Problema problema);

    public void update(Connection connection, Problema problema) throws  InstanceNotFoundException;

    public Problema findById(Connection connection, long id) throws InstanceNotFoundException;

    public List<Problema> findByName(Connection connection, String title);

}