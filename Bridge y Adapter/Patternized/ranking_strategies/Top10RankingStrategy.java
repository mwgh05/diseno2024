package Patternized.ranking_strategies;

import java.util.List;
import java.util.Comparator;
import Patternized.Photo;

public class Top10RankingStrategy implements RankStrategy {

    @Override
    public List<Photo> rankPhotos(List<Photo> photos) {
        // Ordenar por la cantidad de likes de mayor a menor
        photos.sort(Comparator.comparingInt(Photo::getLikes).reversed());

        // Retornar solo el top 10
        return photos.subList(0, Math.min(10, photos.size()));
    }
}
