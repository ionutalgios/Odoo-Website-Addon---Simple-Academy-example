from openerp import fields, models

class Teachers(models.Model):
    _name = 'academy.teachers'
    name = fields.Char()
    department = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")

class Courses(models.Model):
    _name = 'academy.courses'
    name = fields.Char()
    description = fields.Html()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")

