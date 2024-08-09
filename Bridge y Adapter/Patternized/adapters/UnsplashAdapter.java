package Patternized.adapters;

import java.util.List;
import java.util.ArrayList;
import Patternized.Photo;

public class UnsplashAdapter implements PhotoAPI {

    @Override
    public List<Photo> searchPhotos(String query) {
        // Simulación de la llamada a la API de Unsplash
        String apiUrl = "https://api.unsplash.com/search/photos?query=" + query + "&client_id=YOUR_ACCESS_KEY";

        // Simulación de la respuesta de Unsplash
        List<Photo> results = new ArrayList<>();
        results.add(new Photo("https://unsplash.com/photo1", "cat, nature", 200));
        results.add(new Photo("https://unsplash.com/photo2", "cat, sunset", 180));
        results.add(new Photo("https://unsplash.com/photo3", "cat, portrait", 220));
        //Lista de fotos como valor de retorno
        return results;
    }
}


