# -*- coding: utf-8 -*-
# from odoo import http


# class MyPets(http.Controller):
#     @http.route('/my_pets/my_pets', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_pets/my_pets/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_pets.listing', {
#             'root': '/my_pets/my_pets',
#             'objects': http.request.env['my_pets.my_pets'].search([]),
#         })

#     @http.route('/my_pets/my_pets/objects/<model("my_pets.my_pets"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_pets.object', {
#             'object': obj
#         })
