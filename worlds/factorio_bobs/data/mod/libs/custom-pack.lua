
local util = require("util")

local library = {}

function library.get_icons(ingredients, glass_ware)
    local icons = {}
    math.random
    return icons
end

function library.get_localised_name(custom_name)
    local localised_name = {"",{"custom-science-pack.prefix"}}
    for _, name in pairs(custom_name) do
        if Archipelago_localised_science_pack_terms[name] then
            table.insert(localised_name, {"custom-science-pack."..name})
        else
            table.insert(localised_name, name.." ")
        end
    end
    table.insert(localised_name, {"custom-science-pack.postfix"})
    return localised_name
end

return library