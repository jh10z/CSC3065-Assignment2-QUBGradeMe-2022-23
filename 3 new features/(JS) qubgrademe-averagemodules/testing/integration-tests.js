const chai = require('chai');
const chaiHttp = require('chai-http');
const assert = chai.assert;

const { app } = require('../src/app.js');
chai.use(chaiHttp);

describe('Integration Test', () => {
  it('Get average of 50 from endpoint (two values)', (done) => {
    req = {
        "Module1": "20",
        "Module2": "80"
    }
    chai.request(app).post("/").send(req).end((err, res) => {
      assert.equal(res.statusCode, 200);
      assert.equal(res.body["average"], 50);
      done();
    });
  });

  it('Get error response and message from sending word instead of value', (done) => {
    req = {
        "Module1": "test"
    }
    chai.request(app).post("/").send(req).end((err, res) => {
        assert.equal(res.statusCode, 400);
        assert.equal(res.text, "Module 1 value is not a number. \n");
      done();
    });
  });

  it('Get average with empty string and one value', (done) => {
    req = {
        "Module1": "10",
        "Module2": ""
    }
    chai.request(app).post("/").send(req).end((err, res) => {
      assert.equal(res.statusCode, 200);
      assert.equal(res.body["average"], 10);
      done();
    });
  });

  it('Get error response and message from sending nothing', (done) => {
    req = {
      "Module1": "",
      "Module2": "",
      "Module3": "",
      "Module4": "",
      "Module5": ""
    }
    chai.request(app).post("/").send(req).end((err, res) => {
      assert.equal(res.statusCode, 400);
      assert.equal(res.text, "Error: To use functionality, please enter at least one mark. \n");
      done();
    });
  });

  it('Get average of 100 from inner upper bounds', (done) => {
    req = {
      "Module1": "100"
    }
    chai.request(app).post("/").send(req).end((err, res) => {
      assert.equal(res.statusCode, 200);
      assert.equal(res.body["average"], 100);
      done();
    });
  });

  it('Get average of 0 from lower upper bounds', (done) => {
    req = {
      "Module1": "0"
    }
    chai.request(app).post("/").send(req).end((err, res) => {
      assert.equal(res.statusCode, 200);
      assert.equal(res.body["average"], 0);
      done();
    });
  });

  it('Get error response and message from sending outer upper bounds', (done) => {
    req = {
      "Module1": "101"
    }
    chai.request(app).post("/").send(req).end((err, res) => {
      assert.equal(res.statusCode, 400);
      assert.equal(res.text, "Module 1 value is not within 0 to 100. \n");
      done();
    });
  });

  it('Get error response and message from sending outer lower bounds', (done) => {
    req = {
      "Module1": "-1"
    }
    chai.request(app).post("/").send(req).end((err, res) => {
      assert.equal(res.statusCode, 400);
      assert.equal(res.text, "Module 1 value is not within 0 to 100. \n");
      done();
    });
  });
});