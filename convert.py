#!/usr/bin/env python
# -*- coding: utf-8 -*-

# comverter.py by:
#	Cristhofer Travieso <cristhofert97@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# alenght with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

dic = {}

lenght = {"Metro": 1, "Km": 1000, "cm": 0.01, "Yarda": 1.09361, "Pie": 3.28084,
          "Brazas": 0.5468}
speed = {}
area = {}
weight = {}
volume = {}
time = {}


def convert_lenght(number, unit, to_unit):

    _unit = number * lenght[unit]
    return _unit * lenght[to_unit]


def convert_time(number, unit, to_unit):

    _unit = number * time[unit]
    return _unit * time[to_unit]


def convert_volume(number, unit, to_unit):

    _unit = number * volume[unit]
    return _unit * volume[to_unit]


def convert_area(number, unit, to_unit):

    _unit = number * area[unit]
    return _unit * area[to_unit]


def convert_weight(number, unit, to_unit):

    _unit = number * weight[unit]
    return _unit * weight[to_unit]


def convert_speed(number, unit, to_unit):

    _unit = number * speed[to_unit]
    return _unit * speed[to_unit]


def return_list(type_u):
    if type_u == "lenght":
        dic = lenght
    elif type_u == "volume":
        dic = volume
    elif type_u == "area":
        dic = area
    elif type_u == "weight":
        dic = weight
    elif type_u == "speed":
        dic = speed
    elif type_u == "time":
        dic = time

    return dic.key()