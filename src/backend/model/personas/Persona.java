

public class Persona {
    private long idPersona;
    private String nombre;
    private String apellido1;
    private String apellido2;
    private boolean enEmpresa;
    private int telefono;
    private String email;

    public Persona(String nombre, String apellido1, String apellido2, int telefono, String email){
        this.nombre = nombre;
        this.apellido1 = apellido1;
        this.apellido2 = apellido2;
        enEmpresa = true;
        this.telefono = telefono;
        this.email = email;

        /*quizás hacer comprobaciones de la estructura del email
         *El telefono lo más seguro es que tenga que ser un string, si el numero enpieza por 0 se guardaran menos de 9 cifras
         */
    }

    public Persona(long id, String nombre, String apellido1, String apellido2, int telefono, String email){
        this(nombre, apellido1, apellido2, telefono, email);
        this.idPersona = id;
    }

    public long getIdPersona(){
        return idPersona;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido1() {
        return apellido1;
    }

    public String getApellido2() {
        return apellido2;
    }

    public boolean isEnEmpresa() {
        return enEmpresa;
    }

    public int getTelefono() {
        return telefono;
    }

    public String getEmail() {
        return email;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setApellido1(String apellido1) {
        this.apellido1 = apellido1;
    }

    public void setApellido2(String apellido2) {
        this.apellido2 = apellido2;
    }

    public void setEnEmpresa(boolean enEmpresa) {
        this.enEmpresa = enEmpresa;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public boolean equals(Object o){
        if(this == o) return true;
        if(o == null || getClass() != o.getClass()) return false;

        Persona persona = (Persona) o;

        if(this.idPersona != persona.idPersona) return false;
        if(!this.nombre.equals(persona.nombre)) return false;
        if(!this.apellido1.equals(persona.apellido1)) return false;
        if(!this.apellido2.equals(persona.apellido2)) return false;
        if(!this.email.equals(persona.email)) return false;
        if(this.telefono != persona.telefono) return false;
        return (this.enEmpresa == persona.enEmpresa);
    }

}