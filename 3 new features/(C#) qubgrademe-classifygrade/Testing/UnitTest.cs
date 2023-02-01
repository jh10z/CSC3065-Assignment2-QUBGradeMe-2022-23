using classifygradeapi;

namespace Testing
{
    public class UnitTest
    {
        [Fact]
        public void ClassifyValueProvDistinction()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "70";
            classify.Module2 = "90";
            
            Assert.Equal("Provisional: Distinction", classify.Classification);
        }
        [Fact]
        public void ClassifyValueProvCommendation()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "50";
            classify.Module2 = "70";

            Assert.Equal("Provisional: Commendation", classify.Classification);
        }

        [Fact]
        public void ClassifyValueProvPass()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "30";
            classify.Module2 = "50";

            Assert.Equal("Provisional: Pass", classify.Classification);
        }

        [Fact]
        public void ClassifyValueProvMarginalFail()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "20";
            classify.Module2 = "40";

            Assert.Equal("Provisional: Mariginal Fail", classify.Classification);
        }

        [Fact]
        public void ClassifyValueProvFail()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "10";
            classify.Module2 = "30";

            Assert.Equal("Provisional: Fail", classify.Classification);
        }

        [Fact]
        public void ClassifyValueProvLowFail()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "0";
            classify.Module2 = "20";

            Assert.Equal("Provisional: Low Fail", classify.Classification);
        }

        [Fact]
        public void ClassifyAllValuesDistinction()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "70";
            classify.Module2 = "70";
            classify.Module3 = "70";
            classify.Module4 = "70";
            classify.Module5 = "70";

            Assert.Equal("Distinction", classify.Classification);
        }

        [Fact]
        public void ClassifyAllValuesCommendation()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "60";
            classify.Module2 = "60";
            classify.Module3 = "60";
            classify.Module4 = "60";
            classify.Module5 = "60";

            Assert.Equal("Commendation", classify.Classification);
        }

        [Fact]
        public void ClassifyAllValuesPass()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "50";
            classify.Module2 = "50";
            classify.Module3 = "50";
            classify.Module4 = "50";
            classify.Module5 = "50";

            Assert.Equal("Pass", classify.Classification);
        }

        [Fact]
        public void ClassifyAllValuesMarginalFail()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "30";
            classify.Module2 = "30";
            classify.Module3 = "30";
            classify.Module4 = "30";
            classify.Module5 = "30";

            Assert.Equal("Mariginal Fail", classify.Classification);
        }

        [Fact]
        public void ClassifyAllValuesFail()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "20";
            classify.Module2 = "20";
            classify.Module3 = "20";
            classify.Module4 = "20";
            classify.Module5 = "20";

            Assert.Equal("Fail", classify.Classification);
        }

        [Fact]
        public void ClassifyAllValuesLowFail()
        {
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "10";
            classify.Module2 = "10";
            classify.Module3 = "10";
            classify.Module4 = "10";
            classify.Module5 = "10";

            Assert.Equal("Low Fail", classify.Classification);
        }
    }
}