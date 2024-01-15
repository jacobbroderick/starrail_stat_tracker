from marshmallow import Schema, fields
from level_materials import LevelMaterials
from .. import constants


class Character(object):
    def __init__(self, name, level, skill_trace_level, talent_trace_level) -> None:
        self.name = name
        self.level = level
        self.skill_trace_level = skill_trace_level
    def __repr__(self) -> str:
        return 'Character {self.name}'.format(self=self)


class FourStarCharacter(Character):
    def __init__(self, name) -> None:
        self.basic_attack_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.CharacterTypes.FOUR_STAR_TYPE, constants.LevelUpTypes.BASIC_ATTACK_TRACES)
        self.basic_attack_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.CharacterTypes.FOUR_STAR_TYPE, constants.LevelUpTypes.NORMAL_TRACES)


class FiveStarCharacter(Character):
    def __init__(self, name) -> None:
        self.basic_attack_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.CharacterTypes.FIVE_STAR_TYPE, constants.LevelUpTypes.BASIC_ATTACK_TRACES)
        self.normal_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.CharacterTypes.FIVE_STAR_TYPE, constants.LevelUpTypes.NORMAL_TRACES)


class CharacterSchema(Schema):
    name = fields.Str()
    basic_attack_level_up_materials = fields.Dict()
    normal_level_up_materials = fields.Dict()