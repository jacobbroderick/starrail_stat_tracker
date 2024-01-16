from ..model.level_materials import get_level_up_material_counts
from .. import constants


def calculate_materials(desired_level, character, level_type):
    basic_materials = 0
    trace_materials = 0
    acension_materials = 0
    tracks = 0
    current_level = character.basic_attack_level
    level_up_materials = get_level_up_material_counts(level_type, character.rarity)
    for i in range(current_level, desired_level - 1):
            basic_materials += level_up_materials[i].get(constants.MaterialTypes.BASIC.value,0)
            trace_materials += level_up_materials[i].get(constants.MaterialTypes.TRACE.value, 0)
            acension_materials += level_up_materials[i].get(constants.MaterialTypes.ACENSION.value, 0)
            tracks += level_up_materials[i].get(constants.MaterialTypes.TRACKS.value, 0)
    
    return {
        "basic": basic_materials,
        "traces": trace_materials,
        "ascension": acension_materials,
        "tracks": tracks
    }
