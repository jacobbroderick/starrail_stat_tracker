from marshmallow import Schema, fields
from level_materials import LevelMaterials
from .. import constants

class Character(object):
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return 'Character {self.name}'.format(self=self)
    
class FourStarCharacter(Character):
    def __init(self, name) -> None:
        self.basic_attack_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.FOUR_STAR_TYPE, constants.BASIC_ATTACK_TRACES)
        self.basic_attack_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.FOUR_STAR_TYPE, constants.NORMAL_TRACES)
    

class FiveStarCharacter(Character):
    def __init(self, name) -> None:
        self.basic_attack_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.FIVE_STAR_TYPE, constants.BASIC_ATTACK_TRACES)
        self.normal_level_up_materials = LevelMaterials.GetLevelUpMaterialCounts(constants.FIVE_STAR_TYPE, constants.NORMAL_TRACES)



    
class CharacterSchema(Schema):
    name = fields.Str()
    basic_attack_level_up_materials = fields.Dict()
    normal_level_up_materials = fields.Dict()