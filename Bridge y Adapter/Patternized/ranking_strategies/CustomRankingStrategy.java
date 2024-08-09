package Patternized.ranking_strategies;

import java.util.List;
import Patternized.Photo;

public class CustomRankingStrategy implements RankStrategy {

    @Override
    public List<Photo> rankPhotos(List<Photo> photos) {
        // Implementación personalizada de ranking
        // Clase de ejemplo para la creación de rankings personalizados por el usuario
        
        // Retornar Top 10
        return photos.subList(0, Math.min(10, photos.size()));
    }
}
