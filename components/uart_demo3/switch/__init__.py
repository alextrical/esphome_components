import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import DEVICE_CLASS_SWITCH, ENTITY_CATEGORY_NONE

from .. import CONF_UART_DEMO_ID, UARTDemo, uart_demo_ns

DEPENDENCIES = ["uart_demo"]

CONF_THE_SWITCH_1 = "the_switch_1"
CONF_THE_SWITCH_2 = "the_switch_2"

TheSwitch1 = uart_demo_ns.class_("TheSwitch1", switch.Switch)
TheSwitch2 = uart_demo_ns.class_("TheSwitch2", switch.Switch)

# Additional icons from https://pictogrammers.com/library/mdi/
ICON_NUMERIC_1 = "mdi:numeric-1"
ICON_NUMERIC_2 = "mdi:numeric-2"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_UART_DEMO_ID): cv.use_id(UARTDemo),
    cv.Optional(CONF_THE_SWITCH_1): switch.switch_schema(
        TheSwitch1,
        device_class=DEVICE_CLASS_SWITCH,
        icon=ICON_NUMERIC_1,
        entity_category=ENTITY_CATEGORY_NONE,
    ),
    cv.Optional(CONF_THE_SWITCH_2): switch.switch_schema(
        TheSwitch2,
        device_class=DEVICE_CLASS_SWITCH,
        icon=ICON_NUMERIC_2,
        entity_category=ENTITY_CATEGORY_NONE,
    ),
}

async def to_code(config):
    uart_demo_component = await cg.get_variable(config[CONF_UART_DEMO_ID])

    if conf := config.get(CONF_THE_SWITCH_1):
        s = await switch.new_switch(conf)
        await cg.register_parented(s, config[CONF_UART_DEMO_ID])
        cg.add(uart_demo_component.set_the_switch_1(s))
    if conf := config.get(CONF_THE_SWITCH_2):
        s = await switch.new_switch(conf)
        await cg.register_parented(s, config[CONF_UART_DEMO_ID])
        cg.add(uart_demo_component.set_the_switch_2(s))
