# -*- coding: utf-8 -*

from odoo import models, fields, api

class Student(models.Model):
    _name = 'quanlysinhvien.student'
    _description = 'Student Information'
    
    name = fields.Char(string='Tên', required=True)
    birth_date = fields.Date(string='Ngày sinh', required=True, default=fields.Date.context_today)
    email = fields.Char(string='Email', required=True)
    # Fixing
    student_code = fields.Char(string='Mã sinh viên', required=True)
    gender = fields.Selection([ 
                               ('Nam', 'Male'),
                               ('Nữ', 'Female'),
                               ('Khác', 'Others')],
                              string='Giới tính',
                              default='other',
                              required=True)
    class_name = fields.Char(string='Lớp', required=True)
    phone = fields.Char(string='Số điện thoại', required=True)
    
    @api.onchange('name')
    def _onchange_name_generate_code(self):
        if not self.student_code:
            self.student_code = self.env['ir.sequence'].next_by_code('quanlysinhvien.student')
            print("Mã sinh viên được set là:", self.student_code)

    
    # @api.model
    # def create(self, vals):
    #     if not vals.get('student_code'):
    #         vals['student_code'] = self.env['ir.sequence'].next_by_code('quanlysinhvien.student') or '/'
    #     return super(Student, self).create(vals)
