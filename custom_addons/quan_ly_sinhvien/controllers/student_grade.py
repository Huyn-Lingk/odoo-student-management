from odoo import http
from odoo.http import request

class StudentGradeAPI(http.Controller):
    @http.route('/api/student/<int:student_id>/grade', type='http', auth='public', methods=['GET'], csrf=False)
    def get_student_grade(self, student_id):
        student = request.env['quanlysinhvien.student'].sudo().search([('id', '=', student_id)], limit=1)
        if not student:
            return request.make_json_response({'error': 'Không tìm thấy sinh viên'}, status=404)

        grade = request.env['quanlysinhvien.grade'].sudo().search([('student_id', '=', student_id)])
        
        result = []
        for rec in grade:
            result.append({
                'subject': rec.subject_id.name,
                'subject_code': rec.subject_id.code,
                'final_grade': rec.final_grade,
                'mid_term': rec.mid_term,
                'average': rec.average
            })

        return request.make_json_response({
            'student_name': student.name,
            'student_code': student.student_code,
            'grade': result
        })
