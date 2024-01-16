from marshmallow import Schema, fields
from .level_materials import LevelMaterials
from .. import constants


class Character(object):
    def __init__(self, name, level, skill_trace_level, talent_trace_level, ult_trace_level, basic_attack_level, path, rarity) -> None:
        self.name = name
        self.level = level
        self.skill_trace_level = skill_trace_level
        self.talent_trace_level = talent_trace_level
        self.ult_trace_level = ult_trace_level
        self.basic_attack_level = basic_attack_level
        self.path = path
        self.rarity = rarity
    def __repr__(self) -> str:
        return 'Character {self.name}'.format(self=self)


class CharacterSchema(Schema):
    name = fields.Str()
    basic_attack_level_up_materials = fields.Dict()
    normal_level_up_materials = fields.Dict()
    skill_trace_level = fields.Integer()
    talent_trace_level = fields.Integer()
    ult_trace_level = fields.Integer()
    basic_attack_level = fields.Integer()
    path = fields.Str()