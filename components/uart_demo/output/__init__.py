import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output

from .. import CONF_UART_DEMO_ID, UARTDemo, uart_demo_ns

DEPENDENCIES = ["uart_demo"]
AUTO_LOAD = ['output']

CONF_THE_BIN_OUTPUT = "the_bin_output"
CONF_THE_FLT_OUTPUT = "the_flt_output"

UARTDemoBOutput = uart_demo_ns.class_("UARTDemoBOutput", output.BinaryOutput)
UARTDemoFOutput = uart_demo_ns.class_("UARTDemoFOutput", output.FloatOutput)

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_UART_DEMO_ID): cv.use_id(UARTDemo),
    cv.Optional(CONF_THE_BIN_OUTPUT): output.BINARY_OUTPUT_SCHEMA.extend({
        cv.GenerateID(CONF_UART_DEMO_ID): cv.declare_id(UARTDemoBOutput)
    }),
    cv.Optional(CONF_THE_FLT_OUTPUT): output.FLOAT_OUTPUT_SCHEMA.extend({
        cv.GenerateID(CONF_UART_DEMO_ID): cv.declare_id(UARTDemoFOutput)
    }),
}

async def to_code(config):
    uart_demo_component = await cg.get_variable(config[CONF_UART_DEMO_ID])

    # if conf := config.get(CONF_THE_BIN_OUTPUT):
    #     conf = await switch.new_switch(conf)
    #     await cg.register_parented(conf, config[CONF_UART_DEMO_ID])
    #     cg.add(uart_demo_component.write_binary(conf))

    # if CONF_THE_SWITCH in config:
    #     sw = await switch.new_switch(config[CONF_THE_SWITCH])
    #     cg.add(sw.set_parent(var))

    # if CONF_THE_BIN_OUTPUT in config: #fixme
    #     conf = config[CONF_THE_BIN_OUTPUT]
    #     out = cg.new_Pvariable(conf[CONF_ID])
    #     await output.register_output(out, conf)
    #     cg.add(out.set_parent(var))

    # if CONF_THE_FLT_OUTPUT in config:  #fixme
    #     conf = config[CONF_THE_FLT_OUTPUT]
    #     out = cg.new_Pvariable(conf[CONF_ID])
    #     await output.register_output(out, conf)
    #     cg.add(out.set_parent(var))