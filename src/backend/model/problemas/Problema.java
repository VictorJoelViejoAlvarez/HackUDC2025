

public class Problema {
    private long id;
    private String title;
    private String description;
    private long competenciaId;

    public Problema(String title, String description, lonng competenciaId){
        this.title = title;
        this.description = description;
        this.competenciaId = competenciaId;
    }

    public Problema(long id, String title, String description, lonng competenciaId){
        this(title, description, competenciaId);
        this.id = id;
    }

    public long getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public long getCompetenciaId() {
        return competenciaId;
    }

    public void setCompetenciaId(long competenciaId) {
        this.competenciaId = competenciaId;
    }

    @Override
    public boolean equals(Object o){
        if(this == o) return true;
        if(o == null || getClass() != o.getClass()) return false;

        Problema problema = (Problema) o;

        if(this.id != problema.id) return false;
        if(!this.title.equals(problema.title)) return false;
        if(!this.description.equals(problema.description)) return false;
        return (this.competenciaId == problema.competenciaId);
    }

}