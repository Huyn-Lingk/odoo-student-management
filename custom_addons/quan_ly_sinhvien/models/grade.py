from odoo import models, fields, api

class StudentGrade(models.Model):
    _name = 'quanlysinhvien.grade'
    _description = 'Student Grade Information'
    
    # Relation
    student_id = fields.Many2one('quanlysinhvien.student', string='Sinh viên', required=True)
    subject_id = fields.Many2one('quanlysinhvien.subject', string='Môn học', required=True)
    
    final_grade = fields.Float(string='Điểm cuối kỳ', required=True)
    mid_term = fields.Float(string='Điểm giữa kỳ', required=True)    
    average = fields.Float(string='Điểm trung bình', compute='_compute_average', store=True)
    
    @api.depends('mid_term', 'final_grade')
    def _compute_average(self):
        for rec in self:
            if rec.mid_term or rec.final_grade:
                rec.average = rec.mid_term * 0.4 + rec.final_grade * 0.6
            else:
                rec.average = 0