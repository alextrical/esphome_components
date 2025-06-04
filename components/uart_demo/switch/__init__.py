import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import DEVICE_CLASS_SWITCH, ENTITY_CATEGORY_NONE

from .. import CONF_UART_DEMO_ID, UARTDemo, uart_demo_ns

DEPENDENCIES = ["uart_demo"]
AUTO_LOAD = ['switch']

CONF_THE_SWITCH = "the_switch"

UARTDemoSwitch = uart_demo_ns.class_("UARTDemoSwitch", switch.Switch, cg.Component)

# Additional icons from https://pictogrammers.com/library/mdi/
ICON_NUMERIC_1 = "mdi:numeric-1"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_UART_DEMO_ID): cv.use_id(UARTDemo),
    cv.Optional(CONF_THE_SWITCH): switch.switch_schema(
        UARTDemoSwitch,
        device_class=DEVICE_CLASS_SWITCH,
        icon=ICON_NUMERIC_1,
        entity_category=ENTITY_CATEGORY_NONE,
    ),
}

async def to_code(config):
    uart_demo_component = await cg.get_variable(config[CONF_UART_DEMO_ID])

    if conf := config.get(CONF_THE_SWITCH):
        sw = await switch.new_switch(conf)
        await cg.register_parented(sw, config[CONF_UART_DEMO_ID])
        cg.add(uart_demo_component.write_binary(sw))
