/// <reference types="cypress" />
import Nav from "../../src/components/Nav.svelte";
import { mount } from "cypress-svelte-unit-test";

/* eslint-env mocha */
describe("Nav", () => {
  it("shows all nav items", () => {
    mount(Nav);
    cy.get("nav li").should("have.length", 3);
  });
  
  it("highlights the home nav item", () => {
    mount(Nav);
    cy.contains("nav [aria-current=page]", "home");
  });
});
