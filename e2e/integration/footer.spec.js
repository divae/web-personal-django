describe('Footer', function() {
    const email = 'stlmedrano@gmail.com'
    const github = 'https://github.com/divae'
    const linkedin = 'https://www.linkedin.com/in/estela-medrano-jim%C3%A9nez-52563776/'
    const twitter = 'https://twitter.com/EstelaYoMisma'

    it('todos los enlaces del footer son accesibles', function(){
  
      cy.visit('/')
  
      cy.get('[data-cy=footer-email]')
        .should('have.attr', 'href')
        .should('contain', email) 

      cy.get('[data-cy=footer-github]')
        .should('have.attr', 'href')
        .should('contain', github)
        
      cy.get('[data-cy=footer-linkedin]')
        .should('have.attr', 'href')
        .should('contain', linkedin)
        
      cy.get('[data-cy=footer-twitter]')
        .should('have.attr', 'href')
        .should('contain', twitter)
      })
      
  })