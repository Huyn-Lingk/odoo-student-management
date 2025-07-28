from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudentClass(models.Model):
    _name = 'qlsv.class'
    _description = 'Lớp học'

    name = fields.Char(string='Tên lớp', required=True)
    class_code = fields.Char(string='Mã lớp', required=True)
    student_ids = fields.One2many('qlsv.student', 'class_id', string='Danh sách sinh viên')

    @api.constrains('class_code', 'name')
    def _check_class_code_unique(self):
        for rec in self:
            if self.search_count([('class_code', '=', rec.class_code), ('id', '!=', rec.id)]):
                raise ValidationError('Mã lớp này đã tồn tại! Vui lòng nhập mã lớp khác.')