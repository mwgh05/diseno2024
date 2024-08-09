package Patternized.ranking_strategies;

import java.util.List;
import Patternized.Photo;

public interface RankStrategy {
    //Interfaz que instancia el metodo rankPhotos para los diferentes algoritmos de ranking de fotos
    List<Photo> rankPhotos(List<Photo> photos);
}

