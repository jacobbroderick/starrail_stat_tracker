from flask import Flask, request
from flask import render_template
from app.model.character import Character
from app.services.character import calculate_materials
import json
from . import app
from app.constants import CharacterTypes, LevelUpTypes

@app.route("/")
def home():
    character = Character(name="kafka", level = 70, skill_trace_level = 1, talent_trace_level = 1, ult_trace_level = 1, basic_attack_level = 1)
    level_materials = calculate_materials(10, character, LevelUpTypes.NORMAL_TRACES)
    return level_materials

@app.route("/levelup/calculate", methods=['POST'])
def level_up_calculate():
    request_data = request.get_json()
    character = Character(name=request_data['name'], level=request_data['level']
                                  , skill_trace_level=int(request_data['skill_trace_level'])
                                  , talent_trace_level=int(request_data['talent_trace_level'])
                                  , ult_trace_level=int(request_data['ult_trace_level'])
                                  , basic_attack_level=int(request_data['basic_attack_level'])
                                  , path=request_data['path']
                                  , rarity=request_data['rarity'])
    level_materials = calculate_materials(10, character, LevelUpTypes.NORMAL_TRACES.value)
    return json.dumps(character.__dict__)


@app.route("/about/")
def about():
    return render_template("about.html")