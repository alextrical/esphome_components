import esphome.codegen as cg
from esphome.components import binary_sensor
import esphome.config_validation as cv
# from esphome.const import ENTITY_CATEGORY_NONE

from .. import CONF_UART_DEMO_ID, UARTDemo, uart_demo_ns

DEPENDENCIES = ["uart_demo"]
AUTO_LOAD = ['binary_sensor']

CONF_THE_BIN_OUTPUT = "the_bin_output"

UARTDemoBOutput = uart_demo_ns.class_("UARTDemoBOutput", output.BinaryOutput)

# Additional icons from https://pictogrammers.com/library/mdi/
ICON_NUMERIC_1 = "mdi:numeric-1"
ICON_NUMERIC_2 = "mdi:numeric-2"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_UART_DEMO_ID): cv.use_id(UARTDemo),
      cv.Optional(CONF_THE_BIN_OUTPUT): output.BINARY_OUTPUT_SCHEMA(
        the_binsensor,
        icon=ICON_NUMERIC_1,
        entity_category=ENTITY_CATEGORY_NONE,
      ),
}

async def to_code(config):
        if conf := config.get(CONF_THE_BIN_OUTPUT):
            sens = await binary_sensor.new_binary_sensor(conf)
            await cg.register_parented(sens, config[CONF_UART_DEMO_ID])