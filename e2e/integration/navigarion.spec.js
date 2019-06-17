describe('Navigation', function() {
  it('successfully loads', function() {
    cy.visit('/') 
    cy.visit('/about-me') 
    cy.visit('/contact') 
    cy.visit('/portfolio') 
  })
})