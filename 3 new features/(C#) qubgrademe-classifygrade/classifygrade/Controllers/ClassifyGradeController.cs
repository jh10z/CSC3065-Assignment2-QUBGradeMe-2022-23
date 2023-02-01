using Microsoft.AspNetCore.Mvc;

namespace classifygradeapi.Controllers
{
    [ApiController]
    [Route("/")]
    public class ClassifyGradeController : ControllerBase
    {
        [HttpPost]
        public ActionResult<ClassifyGrade> Post(ClassifyGrade classifyGrade)
        {
            if(classifyGrade.GetErrorFlagged)
            {
                return BadRequest(classifyGrade.GetErrorMessage);
            }
            else
            {
                return Ok(classifyGrade);
            }
        }
    }
}