import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ["uart"]

uart_demo_ns = cg.esphome_ns.namespace("uart_demo")
UARTDemo = uart_demo_ns.class_(
    "UARTDemo", cg.Component, uart.UARTDevice
)

CONF_UART_DEMO_ID = "UARTDemo_id"

CONFIG_SCHEMA = (
    cv.Schema({cv.GenerateID(): cv.declare_id(UARTDemo)})
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
