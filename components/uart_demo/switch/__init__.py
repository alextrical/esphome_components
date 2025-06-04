import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import DEVICE_CLASS_SWITCH

from .. import CONF_UART_DEMO_ID, UARTDemo, uart_demo_ns

DEPENDENCIES = ["uart_demo"]

CONF_THE_SWITCH = "the_switch"

TheSwitch = uart_demo_ns.class_("TheSwitch", switch.Switch)

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_UART_DEMO_ID): cv.use_id(UARTDemo),
    cv.Optional(CONF_THE_SWITCH): switch.switch_schema(
        TheSwitch,
        device_class=DEVICE_CLASS_SWITCH,
    ),
}

async def to_code(config):
    uart_demo_component = await cg.get_variable(config[CONF_UART_DEMO_ID])
    if the_switch_config := config.get(CONF_THE_SWITCH):
        s = await switch.new_switch(the_switch_config)
        await cg.register_parented(s, config[CONF_UART_DEMO_ID])
        cg.add(uart_demo_component.set_the_switch(s))
