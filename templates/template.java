//
//	HEAD_LINE
//

package templates;

public enum template {
    
    // MARK: - ALPHA_LINE
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
