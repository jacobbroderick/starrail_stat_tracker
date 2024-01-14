from marshmallow import Schema, fields
from enum import Enum

class LevelMaterials(object):
    def __init__(self):
        self.level
    
    # Returns the amount of level up materials for each type of character type/stattype combo
    def GetLevelUpMaterialCounts(trace_type: str,chracter_type: int ) -> None:
        basic_attack_materials_five = {
            1: {
                "basic": 3,
                "trace": 3
                },
            2: {
                "basic": 9,
                "trace": 9
                },
            3: {
                "basic": 12,
                "trace": 15
            },
            4: {
                "basic": 27,
                "trace": 27
            },
            5: {
                "basic": 36,
                "trace": 72
            }


        }

        trace_materials_five = {
            1: {
                "basic": 3
            },
            2: {
                "basic": 8,
                "trace": 3
            },
            3: {
                "basic": 9,
                "trace": 9
            },
            4: {
                "basic": 12,
                "trace": 15
            },
            5: {
                "basic": 24,
                "trace": 21
            },
            6: {
                "basic": 27,
                "trace": 27
            },
            7: {
                "basic": 36,
                "trace": 45,
                "ascension": 1
            },
            8:{
                "trace": 72,
                "ascension": 1,
                "tracks": 1
            },
            9: {
                "trace": 96,
                "ascension": 1,
                "tracks": 1
            }
        }
        pass


class LevelMaterialsSchema(Schema):
    level_type = fields.Str()

    



