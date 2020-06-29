package lang;

public enum template {
        
    THIS_LINE(""),
    LAST_LINE("");

    private String hex;

    template(String iconHex) {
        this.hex = iconHex;
    }

    public String getHex() {
        return hex;
    }
}
