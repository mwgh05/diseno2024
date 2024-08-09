package Naive;

import java.util.List;
import java.util.ArrayList;

public class BromeliaPictInventory {

    private PixabayAPI pixabayAPI;
    private UnsplashAPI unsplashAPI;

    public BromeliaPictInventory() {
        this.pixabayAPI = new PixabayAPI();
        this.unsplashAPI = new UnsplashAPI();
    }

    public List<Photo> searchAndRankPhotos(String query) {
        // Búsqueda en Pixabay
        List<Photo> pixabayPhotos = pixabayAPI.searchPhotos(query);

        // Búsqueda en Unsplash
        List<Photo> unsplashPhotos = unsplashAPI.searchPhotos(query);

        // Combinar los resultados de ambas API
        List<Photo> combinedPhotos = new ArrayList<>();
        combinedPhotos.addAll(pixabayPhotos);
        combinedPhotos.addAll(unsplashPhotos);

        // Rankear las fotos 
        return rankPhotosResult(combinedPhotos);
    }

    private List<Photo> rankPhotosResult(List<Photo> photos) {
        // Rankear fotos por alguna criteria (likes para la simulacion)
        photos.sort((p1, p2) -> Integer.compare(p2.getLikes(), p1.getLikes()));

        // Retornar el top 10
        return photos.subList(0, Math.min(10, photos.size()));
    }
}