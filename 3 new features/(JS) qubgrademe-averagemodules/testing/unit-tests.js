const chai = require('chai');
const assert = chai.assert;
const { calcAvg } = require('../src/app.js');

describe('Unit Test', () => {
  it('Should calculate average mark 50 - 1 Value', () => {

    let data = {
        body: {
            "Module1": "50",
            }
    }
    let result = calcAvg(data);
    assert.equal(result["avg"], "50");
  });

  it('Should calculate average mark 50 - 2 Values', () => {

    let data = {
        body: {
            "Module1": "20",
            "Module2": "80"
            }
    }
    let result = calcAvg(data);
    assert.equal(result["avg"], "50");
  });

  it('Should calculate average mark 75 - 3 Values', () => {

    let data = {
        body: {
            "Module1": "40",
            "Module2": "80",
            "Module3": "60"
            }
    }
    let result = calcAvg(data);
    assert.equal(result["avg"], "60");
  });

  it('Should calculate average mark 75 - 4 Values', () => {

    let data = {
        body: {
            "Module1": "40",
            "Module2": "80",
            "Module3": "70",
            "Module4": "50"
            }
    }
    let result = calcAvg(data);
    assert.equal(result["avg"], "60");
  });

  it('Should calculate average mark 75 - 5 Values', () => {

    let data = {
        body: {
            "Module1": "75",
            "Module2": "75",
            "Module3": "75",
            "Module4": "75",
            "Module5": "75"
            }
    }
    let result = calcAvg(data);
    assert.equal(result["avg"], "75");
  });

  it('Should calculate average mark 50 - 2 Values (1 Zero)', () => {

    let data = {
        body: {
            "Module1": "100",
            "Module2": "0"
            }
    }
    let result = calcAvg(data);
    assert.equal(result["avg"], "50");
  });

  it('Should calculate average mark 25 - 4 Values (3 Zero)', () => {

    let data = {
        body: {
            "Module1": "100",
            "Module2": "0",
            "Module3": "0",
            "Module4": "0",
            }
    }
    let result = calcAvg(data);
    assert.equal(result["avg"], "25");
  });
});