package Patternized.adapters;

import java.util.List;
import Patternized.Photo;

public interface PhotoAPI {
    //Interfaz que instancia el metodo searchPhoto que solicita un query de busqueda para su implementación
    //con las APIS 
    List<Photo> searchPhotos(String query);
}
