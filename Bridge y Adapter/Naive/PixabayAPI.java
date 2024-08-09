package Naive;

import java.util.List;
import java.util.ArrayList;

public class PixabayAPI {

    public List<Photo> searchPhotos(String query) {
        // Solicitud HTTP a la API de Pixabay

        String apiUrl = "https://pixabay.com/api/?key=YOUR_API_KEY&q=" + query;

        // Respuesta de Pixabay (simulada)
        List<Photo> results = new ArrayList<>();

        // Añadir fotos simuladas a la lista
        results.add(new Photo("https://pixabay.com/photo1", "cat, cute", 100));
        results.add(new Photo("https://pixabay.com/photo2", "cat, funny", 150));
        results.add(new Photo("https://pixabay.com/photo3", "cat, black", 80));
        
        // Parsear el JSON de la respuesta 

        return results;  // Retornar la lista de fotos simuladas
    }
}