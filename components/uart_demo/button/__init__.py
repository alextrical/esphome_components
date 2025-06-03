import esphome.codegen as cg
from esphome.components import button
import esphome.config_validation as cv
# from esphome.const import DEVICE_CLASS_BUTTON

from .. import CONF_UART_DEMO_ID, UARTDemo, uart_demo_ns

DEPENDENCIES = ["uart_demo"]

CONF_THE_BUTTON = "the_button"

TheButton = uart_demo_ns.class_("TheButton", button.Button)

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_UART_DEMO_ID): cv.use_id(UARTDemo),
    cv.Optional(CONF_THE_BUTTON): button.button_schema(
        TheButton,
    ),
}

async def to_code(config):
    uart_demo_component = await cg.get_variable(config[CONF_UART_DEMO_ID])
    if the_button_config := config.get(CONF_THE_BUTTON):
        b = await button.new_button(the_button_config)
        await cg.register_parented(b, config[CONF_UART_DEMO_ID])
        cg.add(uart_demo_component.set_the_button(b))
