const expect = require('chai').expect;
const sinon = require('sinon');
const got = require('got');
const test = require('firebase-functions-test')();

test.mockConfig({
    crossposttodevto: {
      apikey: 'test-api-key'
  }
});

describe("cross-post-to-devto", () => {
    let testFunctions;
    let consoleErrorStub;

    before(() => {
    testFunctions = require('../../../../../lib');
    });

    after(() => {
    consoleErrorStub.restore();
    test.cleanup();
    });

    it("calls the DEV API with correct parameters", async () => {

      const gotPostSpy = sinon.spy(got, 'post');
      consoleErrorStub = sinon.stub(console, 'error');

      const wrapped = test.wrap(testFunctions.firestore.posts.onCreate.crossPostToDevto);

      const snapshot = {
        data: () => ({
          title: 'Test Title',
          content: 'Test content'
        })
      };

      await wrapped(snapshot, {
        params: {
          slug: 'test-title'
        }
      });

      expect(gotPostSpy.calledOnce);
      expect(gotPostSpy.lastCall.firstArg).to.equal(" https://dev.to/api/articles ");
      expect(gotPostSpy.lastCall.lastArg).to.deep.equal({
        headers: { 'api-key': 'test-api-key' },
        json: {
          article: {
            title: 'Test Title',
            body_markdown: 'Test content',
            published: false
          }
        }
      });
      expect(consoleErrorStub.lastCall.firstArg.message).to.have.string("401 (Unauthorized)");
  });
});
