using classifygradeapi;
using classifygradeapi.Controllers;
using FluentAssertions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.VisualStudio.TestPlatform.ObjectModel.Engine.ClientProtocol;
using System.Net;

namespace Testing
{
    public class IntegrationTest
    {

        [Fact]
        public void PostTwoValueProvDistinction()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "70";
            classify.Module2 = "90";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.OK);
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.Value.Should().BeOfType<ClassifyGrade>()
                .Which.Classification.Should().Be("Provisional: Distinction");
        }

        [Fact]
        public void PostAllValuesDistinction()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "70";
            classify.Module2 = "90";
            classify.Module3 = "90";
            classify.Module4 = "90";
            classify.Module5 = "90";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.OK);
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.Value.Should().BeOfType<ClassifyGrade>()
                .Which.Classification.Should().Be("Distinction");
        }

        [Fact]
        public void PostOneValueOneStringEmptyCommendation()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "60";
            classify.Module2 = "";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.OK);
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.Value.Should().BeOfType<ClassifyGrade>()
                .Which.Classification.Should().Be("Provisional: Commendation");
        }

        [Fact]
        public void PostOneNonNumericValueInputValidation()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "I am a string.";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<BadRequestObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.BadRequest);
            response.Result.Should().BeOfType<BadRequestObjectResult>()
                .Which.Value.Should().Be("Module 1 is not a number.\n");
        }

        [Fact]
        public void PostOneOutOfUpperEdgeBoundsValue()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "101";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<BadRequestObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.BadRequest);
            response.Result.Should().BeOfType<BadRequestObjectResult>()
                .Which.Value.Should().Be("Module 1 value must be between 0 and 100.\n");
        }

        [Fact]
        public void PostOneInUpperEdgeBoundsValue()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "100";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.OK);
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.Value.Should().BeOfType<ClassifyGrade>()
                .Which.Classification.Should().Be("Provisional: Distinction");
        }

        [Fact]
        public void PostOneOutOfLowerEdgeBoundsValue()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "-1";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<BadRequestObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.BadRequest);
            response.Result.Should().BeOfType<BadRequestObjectResult>()
                .Which.Value.Should().Be("Module 1 value must be between 0 and 100.\n");
        }

        [Fact]
        public void PostOneInLowerEdgeBoundsValue()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "0";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.OK);
            response.Result.Should().BeOfType<OkObjectResult>()
                .Which.Value.Should().BeOfType<ClassifyGrade>()
                .Which.Classification.Should().Be("Provisional: Low Fail");
        }

        [Fact]
        public void PostOneEmptySpacedValue()
        {
            ClassifyGradeController controller = new ClassifyGradeController();
            ClassifyGrade classify = new ClassifyGrade();
            classify.Module1 = "    ";

            //Post Method
            ActionResult<ClassifyGrade> response = controller.Post(classify);

            //Response
            response.Result.Should().BeOfType<BadRequestObjectResult>()
                .Which.StatusCode.Should().Be((int)HttpStatusCode.BadRequest);
            response.Result.Should().BeOfType<BadRequestObjectResult>()
                .Which.Value.Should().Be("Module 1 value is empty spaced.\n");
        }
    }
}