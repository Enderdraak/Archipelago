{% from "macros.lua" import dict_to_recipe, dict_to_lua, variable_to_lua %}

local lib_cp = require("libs.custom-pack")


local previous_pack = "dummy"
local function add_custom_science_pack(internal_name, display_name, category, energy, ingredients, products, productivity)

    local icons = lib_cp.get_icons(ingredients) --TBD
    local localised_name = lib_cp.get_localised_name(display_name)

    local tool = {
        name = internal_name,
        type = "tool",
        icons = icons,
        localised_name = localised_name,
        localised_description = "item-description.science-pack",
        stack_size = 200,
        subgroup = "science-pack",
        order = "z["..internal_name.."]",
        durability = 1,
        durability_description_key = "description.science-pack-remaining-amount-key",
        durability_description_value = "description.science-pack-remaining-amount-value",
    }
    local recipe = {
        name = internal_name,
        type = "recipe",
        icons = icons,
        localised_name = localised_name,
        subgroup = "science-pack",
        order = "z["..internal_name.."]",
        category = category,
        energy_required = energy,
        ingredients = ingredients,
        results = products,
        allow_productivity = productivity
    }
    local technology = {
        name = internal_name,
        type = "technology",
        icons = icons,
        localised_name = localised_name,
        effects = {
            {
                recipe = internal_name,
                type = "unlock-recipe"
            }
        },
        prerequisites = {
            {previous_pack}
        }
    }

    if previous_pack == "dummy" then
        data:extend({tool,recipe})
    else
        data:extend({tool,recipe,technology})
    end
    previous_pack = internal_name
end

{%- for _, pack_data in custom_science_packs.items() %}
add_custom_science_pack(
    "{{pack_data.name}}",
    {{variable_to_lua(pack_data.custon_name)}},
    "{{pack_data.recipe.category.name}}",
    {{pack_data.recipe.energy}},
    {{dict_to_recipe(pack_data.recipe.ingredients)}},
    {{dict_to_recipe(pack_data.recipe.products)}},
    {{variable_to_lua(pack_data.recipe.productivity)}}

)
{%- endfor %}