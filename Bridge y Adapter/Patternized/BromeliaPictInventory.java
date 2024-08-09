package Patternized;

import java.util.List;
import java.util.ArrayList;
import Patternized.adapters.PhotoAPI;
import Patternized.ranking_strategies.RankStrategy;


public class BromeliaPictInventory {

    //Parametros para busquedas y filtros
    private List<PhotoAPI> photoAPIs;
    private RankStrategy rankStrategy;

    public BromeliaPictInventory(List<PhotoAPI> photoAPIs, RankStrategy rankStrategy) {
        this.photoAPIs = photoAPIs;
        this.rankStrategy = rankStrategy;
    }


    public List<Photo> searchAndRankPhotos(String query) {
        List<Photo> allPhotos = new ArrayList<>();

        // Buscar fotos en cada API usando el adaptador correspondiente
        for (PhotoAPI api : photoAPIs) {
            allPhotos.addAll(api.searchPhotos(query));
        }

        // Rankear las fotos usando la estrategia seleccionada
        return rankStrategy.rankPhotos(allPhotos);
    }

    //Elegir un algoritmo de ranking
    public void setRankStrategy(RankStrategy rankStrategy) {
        this.rankStrategy = rankStrategy;
    }
}
