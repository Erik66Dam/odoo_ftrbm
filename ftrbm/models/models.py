# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import *
from odoo.exceptions import ValidationError

class arbitro(models.Model):
    _name = 'ftrbm.arbitro'

    nombre = fields.Char(string = "Nombre", required = True, help = "El nombre de la árbitro o del árbitro")
    name = fields.Char(string = "DNI", required = True, help = "El DNI de la árbitro o del árbitro")

    apellidos = fields.Char(string = "Apellidos", required = True, help = "Primer y segundo apellido de la árbitro o del árbitro")
    edad = fields.Integer(string = "Edad", requiered = True, help = "Debe de ser mayor de 16 años")
    cuenta_bancaria = fields.Char(string = "Cuenta bancaria", required = True, help = "Cuenta bancaria de la árbitro o del árbitro")
    fecha_ingreso = fields.Date(string = "Fecha de Ingreso", default = fields.Date.today, help = "Fecha en la que ingresó")

    @api.constrains('edad')
    def _check_something(self):
        for arbitro in self:
            if arbitro.edad < 16:
                raise ValidationError("Árbitro demasiado joven, debe ser mayor de 16 años: %s" % arbitro.edad)
    _sql_constraints = [
             ('PK_NM', 'unique (name)','Ese DNI ya existe')]

class mesa(models.Model):
    _name = 'ftrbm.mesa'

    nombre = fields.Char(string = "Nombre", required = True,  help = "El nombre de la mesa o del mesa")
    name = fields.Char(string = "DNI", required = True, help = "El DNI de la mesa o del mesa")

    apellidos = fields.Char(string = "Apellidos", required = True, help = "Primer y segundo apellido de la mesa o del mesa")
    edad = fields.Integer(string = "Edad", requiered = True, help = "Debe de ser mayor de 16 años")
    cuenta_bancaria = fields.Char(string = "Cuenta bancaria", required = True, help = "Cuenta bancaria de la mesa o del mesa")
    fecha_ingreso = fields.Date(string = "Fecha de Ingreso", default = fields.Date.today, help = "Fecha en la que ingresó")

    @api.constrains('edad')
    def _check_something(self):
        for mesa in self:
            if mesa.edad < 16:
                raise ValidationError("Mesa demasiado joven, debe ser mayor de 16 años: %s" % mesa.edad)
    _sql_constraints = [
             ('PK_NM', 'unique (name)','Ese DNI ya existe')]

class entrenador(models.Model):
    _name = 'ftrbm.entrenador'

    nombre = fields.Char(string = "Nombre", required = True, help = "El nombre de la entrenadora o del entrenador")
    name = fields.Char(string = "DNI", required = True, help = "El DNI de la entrenadora o del entrenador")

    apellidos = fields.Char(string = "Apellidos", required = True, help = "Primer y segundo apellido de la entrenadora o del entrenador")
    edad = fields.Integer(string = "Edad", requiered = True, help = "Debe de ser mayor de 18 años")
    equipo = fields.Many2one("ftrbm.equipo", string="Equipo", help = "Equipo al que pertenece")

    @api.constrains('edad')
    def _check_something(self):
        for entrenador in self:
            if entrenador.edad < 18:
                raise ValidationError("Entrenador demasiado joven, debe ser mayor de 16 años: %s" % entrenador.edad)
    _sql_constraints = [
             ('PK_NM', 'unique (name)','Ese DNI ya existe')]

class jugador(models.Model):
    _name = 'ftrbm.jugador'

    nombre = fields.Char(string = "Nombre", required = True, help = "El nombre del jugador")
    name = fields.Char(string = "DNI", required = True, help = "El DNI del jugador")

    apellidos = fields.Char(string = "Apellidos", required = True, help = "Primer y segundo apellido del jugador")
    edad = fields.Integer(string = "Edad", requiered = True, help = "Debe de ser mayor de 16 años")
    equipo = fields.Many2one("ftrbm.equipo", string="Equipo", help = "Equipo al que pertenece")
    numero = fields.Integer(string = "Numero", required = True, help = "Número asignado para poder jugar")

    @api.constrains('edad')
    def _check_something(self):
        for jugador in self:
            if jugador.edad < 16:
                raise ValidationError("jugador demasiado joven, debe ser mayor de 16 años: %s" % jugador.edad)

    _sql_constraints = [
             ('PK_NM', 'unique (name)','Ese DNI ya existe')]

class equipo(models.Model):
    _name = 'ftrbm.equipo'
    name = fields.Char(string = "Nombre", required = True, help="nombre del equipo")
    club = fields.Char(string = "Club", required = True, help="Club en la que pertenece el equipo")
    poblacion = fields.Char(string = "Población", required = True, default="Logroño", help="Población en la que pertenece el equipo")
    fecha_creacion = fields.Date(string = "Fecha de creacion", required = True, default = fields.Date.today)

    _sql_constraints = [
             ('PK_NM', 'unique (name)','Ese EQUIPO ya existe')]


class encuentro(models.Model):
    _name = 'ftrbm.encuentro'
    name = fields.Char(string = "ID", required = True, help="ID del encuentro")
    poblacion = fields.Char(string = "Celebrado en", required = True, default="Logroño", help="Población en la que se celebra el encuentro")
    terreno = fields.Char(string = "Terreno de juego", required = True, default="POL. Ejemplo", help="Terreno de juego en que se celebra el encuentro")
    fecha = fields.Date(string = "Fecha", default = fields.Date.today, help = "Fecha en la que se realizó")

    equipoa = fields.Many2one("ftrbm.equipo", string="Equipo Local",requiered = True, help = "Equipo que juega de local")
    golesa = fields.Integer(string = "Goles Local", requiered = True, help = "Goles del equipo local")
    equipob = fields.Many2one("ftrbm.equipo", string="Equipo visitante",requiered = True, help = "Equipo que juega de visitante")

    golesb = fields.Integer(string = "Goles Visitante", requiered = True, help = "Goles del equipo visitante")

    arbitro1 = fields.Many2one("ftrbm.arbitro", string="Árbitro",requiered = True, help = "Árbitro que dirige el partido")
    arbitro2 = fields.Many2one("ftrbm.arbitro", string="Árbitro ayudante", help = "Árbitro ayudante que dirige el partido")
    mesa = fields.Many2one("ftrbm.mesa", string="Mesa", required = True, help = "Mesa ayudante que dirige el partido")

    @api.constrains('golesa')
    def _check_something(self):
        for encuentro in self:
            if encuentro.golesa < 0:
                raise ValidationError("Los goles no pueden ser menor de 0: %s" % encuentro.golesa)

    @api.constrains('golesb')
    def _check_something(self):
        for encuentro in self:
            if encuentro.golesb < 0:
                raise ValidationError("Los goles no pueden ser menor de 0: %s" % encuentro.golesb)

    _sql_constraints = [
             ('PK_NM', 'unique (name)','Ese ID ya existe')]
