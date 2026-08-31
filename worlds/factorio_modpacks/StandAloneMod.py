import base64
import zlib


# build up the main setting needed during the connection phase.
# collect (almost) static info

# total package:
#       info:{
#           apworld: "<apworld name>",  #extract from generation
#           apversion: "<apworld version>",  #extract from generation
#           modversion: "<factorio mod version>",  #extract from generation
#           slotname: "<slot name>",  # extracted from connection
#           multiworld: "<multiworld name>"  #extract from generation
#           features: {   #list of all features that this mod will want to use.
#               new_locations:  'enabled/disabled'
#               starter_tech:  'enabled/disabled'
#               removed_technologies:  'enabled/disabled'
#               localized_items:  'enabled/disabled'   #read if this client can accommodate this
#               default_settings:  'enabled/disabled'
#
#               custom_recipes: 'enabled/disabled'  #TODO
#               hidden_technologies: 'enabled/disabled'  #TODO
#               samples: 'enabled/disabled'  #TODO
#               progressive: 'enabled/disabled'  #TODO
#               recipe_adjustment: 'enabled/disabled'  #TODO
#               traps: 'enabled/disabled'  #TODO
#               map_preset: 'enabled/disabled'  #TODO
#           }
#       }
#       new_locations: {  #get all location IDs from getDataPackage
#           knowledge: 0/1/2  #follow the yaml option: 0 = none (except revealed), 1 only advancement level. 2 revealed and hint out advancement. 3 hint everything.
#           locations: {
#               location_id: {  #use location scouts (use missing_locations and checked_locations to find out all locations.) to find all items connected to locations. use item_names to look up information about the items.
#                   location: <int of location ID/adress>
#                   item_name: "<name>"  #name of the item that gets send away.
#                   player: "<(aliased?) player name>"  #name of the player who gets the item (possibly changing during the async.)
#                   type: "science/crafting/duplicate"
#                   revealed: true/false  #overwrites the knowledge. Could even be made to check every startup to add icons and text during an async.
#                   classification: "advancement/useful/filler/trap"
#                   # type: science
#                   count: <int>  #count of science packs.
#                   science_packs: {<dict[name, quantity] of science packs>}  #science packs for tech.
#                   ? prerequisites: {<ID list of items that come before>}  #direct ID's mod will make it correctly. Can be missing. Then it is assumed to be not needed.
#                   # type: crafting
#                   craft: "<item/fluid-name>"  #what items needs to be crafted
#                   ? count: <int>  # optional, assumed 1 when missing.
#                   ? prerequisites: {<ID list of items that come before>}  #direct ID's mod will make it correctly. Can be missing. Then it is assumed to be not needed.
#                   # type: duplicate  #duplicates the tech in the existing tech tree.
#                   copy: "<tech-name>"
#                   ? count: <int>  #count of science packs.  nil means original cost.
#                   ? science_packs: {<list of science packs>}  #science packs for tech.  nil means original packs.
#                   ? prerequisites: {<ID list of items that come before>}  #direct ID's mod will make it correctly. Can be missing. Will place it on top of the duplicates that will be made from other techs.
#               }
#           }
#       }
#       starter_tech: {
#           recipes: {<list of recipes>} # all recipes that are in the starter tech. If enabled and left empty it will still not show up.
#       }
#       removed_technologies: {
#           technologies: {<list of technologies>} # all the technologies that are unlocked by default.
#       }
#       localized_items: { #info is already stored in the locations data. No duplicate info needed.
#       }
#       default_settings: { # deathlink, energy link, tech obscurity all get an extra option named 'yaml'. The info in this group will determent the behavior of that option.
#           ? deathlink: "true/false" # when missing it sees false.
#           ? energylink: "true/false" # when missing it sees false.
#           ? depth_obscurity: <int of depth> # when missing it sees 0.  (-1 is a the yaml option.)
#           ? layer_obscurity: "true/false" # when missing it sees false.
#           ? craft_obscurity: "true/false" # when missing it sees false.
#       }
#       
#       









