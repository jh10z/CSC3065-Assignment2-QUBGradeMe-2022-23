const express = require('express')
const cors = require('cors')
const app = express()
const port = 8000

app.use(cors())
app.use(express.json());

function calcAvg(req) {
  let module_sum = 0, module_count = 0;  
  let errorMessage = ""; 
  let errorCode = 200;
  data = req.body;
  if(data["Module1"] == "" && data["Module2"] == ""&& data["Module3"] == "" && data["Module4"] == "" && data["Module5"] == "") {
    errorMessage += "Error: To use functionality, please enter at least one mark. \n"
    errorCode = 400;
  }
  for (const key in data) {
      if(data.hasOwnProperty(key)) {
          if(data[key] == "") {
            continue;
          }

          if(isNaN(data[key]))  {
            errorMessage += "Module " + key[6] + " value is not a number. \n"
            errorCode = 400;
          } else if (data[key] < 0 || data[key] > 100) {
            errorMessage += "Module " + key[6] + " value is not within 0 to 100. \n"
            errorCode = 400;
          } 
          else {
            module_sum += parseFloat(data[key]);
            module_count++;
          }
      }
  }
  return {"avg": module_sum/module_count, "code": errorCode, "message": errorMessage};
}

app.post('/', (req, res) => {
  let ans = calcAvg(req);

  if (ans["code"] == 400) {
    res.status(400).send(ans["message"]);
  } else {
    res.json({average: ans["avg"]})
  }
})

app.listen(port, () => {
  console.log(`Server listening on port ${port}`)
})

module.exports = { app, calcAvg };