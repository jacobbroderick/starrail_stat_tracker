from flask import Flask
from flask import render_template
from app.model.character import FiveStarCharacter
from app.services.character import CharacterService
from . import app
from app import constants

@app.route("/")
def home():
    character = FiveStarCharacter(name="kafka", level = 70, skill_trace_level = 1, talent_trace_level = 1, ult_trace_level = 1, basic_attack_level = 1)
    level_materials = CharacterService.calculate_materials(10, character, constants.LevelUpTypes.NORMAL_TRACES)
    return level_materials

@app.route("/about/")
def about():
    return render_template("about.html")