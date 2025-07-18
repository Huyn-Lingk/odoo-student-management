from odoo import http
from odoo.http import request
from datetime import datetime

class StudentController(http.Controller):

    @http.route('/report/student/<int:student_id>', type='http', auth='user')
    def student_report(self, student_id):
        report = request.env.ref('quan_ly_sinhvien.action_report_student_profile')
        student = request.env['quanlysinhvien.student'].browse(student_id)

        return report.report_action(student, data={'now': datetime.now()})
    
    @http.route('/student', type='http', auth='user', website=True)
    def student_list_show(self, **kwargs):
        student = request.env['quanlysinhvien.student'].search([])
        print("Danh sách sinh viên:", student)
        return request.render('quan_ly_sinhvien.student_list_template', {
        'students': student,
        })
