package edu.classifymodules.webapi.classifymodules;

public class Modules {
    private String m1_grade;
    private String m2_grade;
    private String m3_grade;
    private String m4_grade;
    private String m5_grade;
    private boolean errorFlagged = false;
    private String errorMessage = "";

    //Public Getters
    public String getM1_grade() {
        return m1_grade;
    }
    public String getM2_grade() { return m2_grade; }
    public String getM3_grade() {
        return m3_grade;
    }
    public String getM4_grade() {
        return m4_grade;
    }
    public String getM5_grade() { return m5_grade; }
    protected boolean getErrorFlagged() { return errorFlagged; }
    protected String getErrorMessage() { return errorMessage; }

    //Public Setters
    public void setM1_grade(String m1_grade) { this.m1_grade = classifyGrade(1, m1_grade); }
    public void setM2_grade(String m2_grade) { this.m2_grade = classifyGrade(2, m2_grade); }
    public void setM3_grade(String m3_grade) { this.m3_grade = classifyGrade(3, m3_grade); }
    public void setM4_grade(String m4_grade) { this.m4_grade = classifyGrade(4, m4_grade); }
    public void setM5_grade(String m5_grade) { this.m5_grade = classifyGrade(5, m5_grade); }

    private String classifyGrade(int moduleNumber, String strScore) {
        //Error Handling - Type Conversion
        if (strScore == null) {
            return logError("Module " + moduleNumber + " cannot be null.");
        } else if (strScore == "") {
            return null;
        } else if (strScore.trim() == "") {
            return logError("Module " + moduleNumber + " value cannot be empty space.");
        }
        try {
            double score = Double.parseDouble(strScore);
            if(score > 100 || score < 0) {
                return logError("Module " + moduleNumber + " value must be within the range of 0 to 100 to be classified.");
            }
            else if (score >= 70) { return "1st"; }
            else if (score >= 60) { return "2:1"; }
            else if (score >= 50) { return "2:2"; }
            else if (score >= 40) { return "3rd"; }
            else { return "Failed"; }
        } catch (NumberFormatException nfe) {
            return logError("Module " + moduleNumber + " value is not a number.");
        }
    }

    private String logError(String msg) {
        errorFlagged = true;
        errorMessage += msg + "\n";
        return null;
    }
}
