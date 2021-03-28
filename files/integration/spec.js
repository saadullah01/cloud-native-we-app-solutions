describe("Sapper template app", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("has the correct <h1>", () => {
    cy.contains("h1", "Great success!");
  });

  it("has the correct heading", () => {
    // https://testing-library.com/docs/guide-which-query
    cy.findByRole("heading").should("contain", "Great success!");
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
  before(() => {
    cy.visit("/").then(contentWindow => {
      const firebaseAppOptions = contentWindow.firebase.app().options;
      cy.task("addBlogPost", {
        firebaseAppOptions,
        slug: "test-post",
        post: {
          content: "A test blog post",
          title: "Test post"
        }
      });
    });
    cy.visit("/blog");
  });

  it("has the correct <h1>", () => {
    cy.contains("h1", "Recent posts");
  });

  it("displays the test blog post", () => {
    cy.contains("[data-cy=blog-posts-list] a", "Test post");
  });
});