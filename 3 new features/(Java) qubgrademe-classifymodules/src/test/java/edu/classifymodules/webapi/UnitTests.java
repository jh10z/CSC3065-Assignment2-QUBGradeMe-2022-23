package edu.classifymodules.webapi;

import edu.classifymodules.webapi.classifymodules.Modules;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class UnitTests {

    @Test
    void ClassifyOneValueAsFirst() {
        Modules modules = new Modules();
        modules.setM1_grade("100");
        assertEquals("1st", modules.getM1_grade());
    }

    @Test
    void ClassifyOneValueAsUpperSecond() {
        Modules modules = new Modules();
        modules.setM1_grade("60");
        assertEquals("2:1", modules.getM1_grade());
    }

    @Test
    void ClassifyOneValueAsLowerSecond() {
        Modules modules = new Modules();
        modules.setM1_grade("50");
        assertEquals("2:2", modules.getM1_grade());
    }

    @Test
    void ClassifyOneValueAsThird() {
        Modules modules = new Modules();
        modules.setM1_grade("40");
        assertEquals("3rd", modules.getM1_grade());
    }

    @Test
    void ClassifyOneValueAsFail() {
        Modules modules = new Modules();
        modules.setM1_grade("30");
        assertEquals("Failed", modules.getM1_grade());
    }

    @Test
    void ClassifyAllValuesAsFirst() {
        Modules modules = new Modules();
        modules.setM1_grade("70");
        modules.setM2_grade("70");
        modules.setM3_grade("70");
        modules.setM4_grade("70");
        modules.setM5_grade("70");
        assertEquals("1st", modules.getM1_grade());
        assertEquals("1st", modules.getM2_grade());
        assertEquals("1st", modules.getM3_grade());
        assertEquals("1st", modules.getM4_grade());
        assertEquals("1st", modules.getM5_grade());
    }

}
