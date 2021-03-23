const posts = require('../../src/routes/blog/_posts');

describe("Sapper template app", () => {
    beforeEach(() => {
      cy.visit("/");
    });
  
    it("has the correct <h1>", () => {
      cy.contains("h1", "Great success!");
    });
  
    it("navigates to /about", () => {
      cy.get("nav a").contains("about").click();
      cy.url().should("include", "/about");
    });
  
    it("navigates to /blog", () => {
      cy.get("nav a").contains("blog").click();
      cy.url().should("include", "/blog");
    });
});

describe('Blog posts', () => {
    beforeEach(() => {
     cy.visit('/blog')
    });
  
    it("has the correct <h1>", () => {
      cy.contains("h1", "Recent posts");
    });
  
    posts.forEach(post => {
      it(`lists the "${post.title}" blog post`, () => {
        cy
          .contains('[data-cy=blog-posts-list] li a', post.title)
          .should('have.attr', 'href', `blog/${post.slug}`)
      })
    });
  });