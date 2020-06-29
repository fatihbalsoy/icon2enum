public enum MDIcon {
        
%s

    private String hex;

    MDIcon(String iconHex) {
        this.hex = iconHex;
    }

    public String getHex() {
        return hex;
    }
}