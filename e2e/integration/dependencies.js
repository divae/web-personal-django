describe('Dependencias del proyecto', function() {
    it('todos los enlaces del footer son accesibles', function(){
        cy.request('http://localhost:8000/static/vendor/jquery/jquery.min.js')
            .should((response) => {
            expect(response.status).to.eq(200)
        })         
    })
})