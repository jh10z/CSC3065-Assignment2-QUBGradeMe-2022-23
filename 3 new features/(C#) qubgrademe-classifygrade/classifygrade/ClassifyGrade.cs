using System.Text.Json.Serialization;

namespace classifygradeapi
{
    public class ClassifyGrade
    {
        private double module1, module2, module3, module4, module5;
        private int moduleCount = 0;
        private bool errorFlagged = false;
        private string errorMessage = "";

        public string Module1
        {
            set { module1 = convertToDouble(1, value); }
        }

        public string Module2
        {
            set { module2 = convertToDouble(2, value); }
        }

        public string Module3
        {
            set { module3 = convertToDouble(3, value); }
        }

        public string Module4
        {
            set { module4 = convertToDouble(4, value); }
        }

        public string Module5
        {
            set { module5 = convertToDouble(5, value); }
        }

        public bool GetErrorFlagged
        {
            get { return errorFlagged; }
        }

        public string GetErrorMessage
        {
            get { return errorMessage; }
        }

        public string Classification
        {
            get 
            {
                if (moduleCount > 0 && moduleCount < 5)
                {
                    return "Provisional: " + calcGrade(sumModules() / moduleCount);
                }
                else if (moduleCount < 1)
                {
                    return logError("Error: To use functionality, please enter at least one mark.");
                }
                return calcGrade(sumModules() / moduleCount); 
            }
        }
        private string calcGrade(double score)
        {
            if (score >= 70 && score <= 100)
            {
                return "Distinction";
            }
            else if (score >= 60)
            {
                return "Commendation";
            }
            else if (score >= 40)
            {
                return "Pass";
            }
            else if (score >= 30)
            {
                return "Mariginal Fail";
            }
            else if (score >= 20)
            {
                return "Fail";
            }
            else if (score >= 0)
            {
                return "Low Fail";
            }
            return "Invalid";
        }
        private double sumModules() => module1 + module2 + module3 + module4 + module5;

        private string logError(string message)
        {
            errorFlagged = true;
            errorMessage += message + "\n";
            return message;
        }

        private double convertToDouble(int moduleNum, string score)
        {
            if (score == null || score == string.Empty)
            {
                return 0.0;
            }
            else if (score.Trim() == string.Empty)
            {
                logError("Module " + moduleNum + " value is empty spaced.");
                return 0;
            }
            else
            {
                try
                {
                    double scoreDouble = Convert.ToDouble(score);
                    if (scoreDouble >= 0 && scoreDouble <= 100)
                    {
                        moduleCount++;
                        return scoreDouble;
                    }
                    else
                    {
                        logError("Module " + moduleNum + " value must be between 0 and 100.");
                        return 0;
                    }
                }
                catch (FormatException)
                {
                    logError("Module " + moduleNum + " is not a number.");
                    return 0;
                }

            }
        }
    }
}