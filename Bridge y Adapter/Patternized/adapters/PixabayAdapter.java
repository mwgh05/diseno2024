package Patternized.adapters;

import java.util.List;
import java.util.ArrayList;
import Patternized.Photo;

public class PixabayAdapter implements PhotoAPI {

    @Override
    public List<Photo> searchPhotos(String query) {
        // Simulación de la llamada a la API de Pixabay
        String apiUrl = "https://pixabay.com/api/?key=YOUR_API_KEY&q=" + query;

        // Simulación de la respuesta de Pixabay
        List<Photo> results = new ArrayList<>();
        results.add(new Photo("https://pixabay.com/photo1", "cat, cute", 100));
        results.add(new Photo("https://pixabay.com/photo2", "cat, funny", 150));
        results.add(new Photo("https://pixabay.com/photo3", "cat, black", 80));
        
        return results;
    }
}
