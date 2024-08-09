package Naive;

import java.util.List;
import java.util.ArrayList;

public class UnsplashAPI {

    public List<Photo> searchPhotos(String query) {
        // Solicitud HTTP a la API de Unsplash

        String apiUrl = "https://api.unsplash.com/search/photos?query=" + query + "&client_id=YOUR_ACCESS_KEY";

        // Respuesta de Unsplash (simulada)
        List<Photo> results = new ArrayList<>();

        // Añadir fotos simuladas a la lista
        results.add(new Photo("https://unsplash.com/photo1", "cat, nature", 200));
        results.add(new Photo("https://unsplash.com/photo2", "cat, sunset", 180));
        results.add(new Photo("https://unsplash.com/photo3", "cat, portrait", 220));
        
        // Parsear el JSON de la respuesta

        return results;  // Retornar la lista de fotos simuladas
    }
}