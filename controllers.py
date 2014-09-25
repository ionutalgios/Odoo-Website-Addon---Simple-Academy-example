# -*- coding: utf-8 -*-
from openerp import http

class Academy(http.Controller):
        
    @http.route('/academy/', auth='public', website=True)
    def academy(self):
        Teachers = http.request.env['academy.teachers']
        Courses = http.request.env['academy.courses']
        return http.request.render('academy.academy', {'teachers': Teachers.search([]),'courses': Courses.search([])})
