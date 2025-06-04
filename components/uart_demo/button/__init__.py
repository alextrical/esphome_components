import esphome.codegen as cg
from esphome.components import button
import esphome.config_validation as cv
from esphome.const import ENTITY_CATEGORY_NONE

from .. import CONF_UART_DEMO_ID, UARTDemo, uart_demo_ns

DEPENDENCIES = ["uart_demo"]
AUTO_LOAD = ['button']

CONF_THE_BUTTON = "the_button"

UARTDemoButton = uart_demo_ns.class_("UARTDemoButton", button.Button, cg.Component)

# Additional icons from https://pictogrammers.com/library/mdi/
ICON_NUMERIC_1 = "mdi:numeric-1"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_UART_DEMO_ID): cv.use_id(UARTDemo),
    cv.Optional(CONF_THE_BUTTON): button.button_schema(
        UARTDemoButton,
        icon=ICON_NUMERIC_1,
        entity_category=ENTITY_CATEGORY_NONE,
    ),
}

async def to_code(config):
    uart_demo_component = await cg.get_variable(config[CONF_UART_DEMO_ID])

    if conf := config.get(CONF_THE_BUTTON):
        btn = await button.new_button(conf)
        await cg.register_parented(btn, config[CONF_UART_DEMO_ID])
        cg.add(uart_demo_component.write_binary(btn))
