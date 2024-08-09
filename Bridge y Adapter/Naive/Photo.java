package Naive;

public class Photo {

    private String url;
    private String tags;
    private int likes;

    public Photo(String url, String tags, int likes) {
        this.url = url;
        this.tags = tags;
        this.likes = likes;
    }

    public String getUrl() {
        return url;
    }

    public String getTags() {
        return tags;
    }

    public int getLikes() {
        return likes;
    }
}
