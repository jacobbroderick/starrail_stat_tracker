from ..model.character import FourStarCharacter, FiveStarCharacter
from .. import constants

class CharacterService():

    def calculate_materials(desired_level, character, level_type):
        basic_materials = 0
        trace_materials = 0
        acension_materials = 0
        tracks = 0
        current_level = character.basic_attack_level
        for i in range(current_level, desired_level - 1):
            if level_type == constants.LevelUpTypes.BASIC_ATTACK_TRACES:
                    basic_materials += character.basic_attack_level_up_materials[i].get(constants.MaterialTypes.BASIC.value,0)
                    trace_materials += character.basic_attack_level_up_materials[i].get(constants.MaterialTypes.TRACE.value, 0)
                    acension_materials += character.basic_attack_level_up_materials[i].get(constants.MaterialTypes.ACENSION.value, 0)
                    tracks += character.basic_attack_level_up_materials[i].get(constants.MaterialTypes.TRACKS.value, 0)
            if level_type == constants.LevelUpTypes.NORMAL_TRACES:
                    basic_materials += character.normal_level_up_materials[i].get(constants.MaterialTypes.BASIC.value,0)
                    trace_materials += character.normal_level_up_materials[i].get(constants.MaterialTypes.TRACE.value, 0)
                    acension_materials += character.normal_level_up_materials[i].get(constants.MaterialTypes.ACENSION.value, 0)
                    tracks += character.normal_level_up_materials[i].get(constants.MaterialTypes.TRACKS.value, 0)
        
        return {
            "basic": basic_materials,
            "traces": trace_materials,
            "ascension": acension_materials,
            "tracks": tracks
        }
