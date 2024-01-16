from marshmallow import Schema, fields
from .level_materials import LevelMaterials
from .. import constants


class Character(object):
    def __init__(self, name, level, skill_trace_level, talent_trace_level, ult_trace_level, basic_attack_level) -> None:
        self.name = name
        self.level = level
        self.skill_trace_level = skill_trace_level
        self.talent_trace_level = talent_trace_level
        self.ult_trace_level = ult_trace_level
        self.basic_attack_level = basic_attack_level
    def __repr__(self) -> str:
        return 'Character {self.name}'.format(self=self)


class FourStarCharacter(Character):
    def __init__(self,name, level, skill_trace_level, talent_trace_level, ult_trace_level, basic_attack_level) -> None:
        self.basic_attack_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.CharacterTypes.FOUR_STAR_TYPE, constants.LevelUpTypes.BASIC_ATTACK_TRACES)
        self.normal_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.CharacterTypes.FOUR_STAR_TYPE, constants.LevelUpTypes.NORMAL_TRACES)
        super().__init__(name, level, skill_trace_level, talent_trace_level, ult_trace_level, basic_attack_level)


class FiveStarCharacter(Character):
    def __init__(self, name, level, skill_trace_level, talent_trace_level, ult_trace_level, basic_attack_level) -> None:
        self.basic_attack_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.CharacterTypes.FIVE_STAR_TYPE, constants.LevelUpTypes.BASIC_ATTACK_TRACES)
        self.normal_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.CharacterTypes.FIVE_STAR_TYPE, constants.LevelUpTypes.NORMAL_TRACES)
        super().__init__(name, level, skill_trace_level, talent_trace_level, ult_trace_level, basic_attack_level)

class CharacterSchema(Schema):
    name = fields.Str()
    basic_attack_level_up_materials = fields.Dict()
    normal_level_up_materials = fields.Dict()
    skill_trace_level = fields.Integer()
    talent_trace_level = fields.Integer()
    ult_trace_level = fields.Integer()
    basic_attack_level = fields.Integer()