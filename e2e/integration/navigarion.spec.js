describe('Navigation', function() {
  it('todos los enlaces del menú son accesibles', function(){

    cy.visit('/')

    cy.get('[data-cy=navbar-about_me]').click()
    cy.location().should((location) => {
      expect(location.pathname).to.eq('/about-me/')
    })

    cy.get('[data-cy=navbar-portfolio]').click()
    cy.location().should((location) => {
      expect(location.pathname).to.eq('/portfolio/')
    })

    cy.get('[data-cy=navbar-contact]').click()
    cy.location().should((location) => {
      expect(location.pathname).to.eq('/contact/')
    })

    cy.get('[data-cy=navbar-home]').click()
    cy.location().should((location) => {
      expect(location.pathname).to.eq('/')
    })
    
  })
})