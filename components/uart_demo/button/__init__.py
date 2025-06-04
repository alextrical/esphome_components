import esphome.codegen as cg
from esphome.components import button
import esphome.config_validation as cv
from esphome.const import ENTITY_CATEGORY_NONE

from .. import CONF_UART_DEMO_ID, UARTDemo, uart_demo_ns

DEPENDENCIES = ["uart_demo"]

CONF_THE_BUTTON_1 = "the_button_1"
CONF_THE_BUTTON_2 = "the_button_2"

TheButton1 = uart_demo_ns.class_("TheButton1", button.Button)
TheButton2 = uart_demo_ns.class_("TheButton2", button.Button)

# Additional icons from https://pictogrammers.com/library/mdi/
ICON_NUMERIC_1 = "mdi:numeric-1"
ICON_NUMERIC_2 = "mdi:numeric-2"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_UART_DEMO_ID): cv.use_id(UARTDemo),
    cv.Optional(CONF_THE_BUTTON_1): button.button_schema(
        TheButton1,
        icon=ICON_NUMERIC_1,
        entity_category=ENTITY_CATEGORY_NONE,
    ),
    cv.Optional(CONF_THE_BUTTON_2): button.button_schema(
        TheButton2,
        icon=ICON_NUMERIC_2,
        entity_category=ENTITY_CATEGORY_NONE,
    ),
}

async def to_code(config):
    for button_type in [CONF_THE_BUTTON_1, CONF_THE_BUTTON_2]:
        if conf := config.get(button_type):
            btn = await button.new_button(conf)
            await cg.register_parented(btn, config[CONF_UART_DEMO_ID])
